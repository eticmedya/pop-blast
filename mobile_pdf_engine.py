#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Engine - TTF Parser + PDF Builder + Layout
Claude Code ile Mobil Uygulama Rehberi | @aykutuces
"""
import struct, zlib, os

# ── Font Paths ──────────────────────────────────────────────
FONT_REG       = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD      = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO      = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

# ── Page Constants ──────────────────────────────────────────
PW, PH  = 595.28, 841.89   # A4
ML, MR  = 62.0, 62.0
MT, MB  = 52.0, 48.0
HDR_H   = 26.0
FTR_H   = 26.0
CW      = PW - ML - MR     # 471.28 pt content width

# ── Colors (normalized RGB) ─────────────────────────────────
NAVY        = (0.102, 0.169, 0.290)
ORANGE      = (1.000, 0.420, 0.208)
WHITE       = (1.000, 1.000, 1.000)
BLACK       = (0.000, 0.000, 0.000)
GRAY_BG     = (0.945, 0.945, 0.955)
GRAY_LINE   = (0.740, 0.740, 0.750)
GRAY_DARK   = (0.310, 0.310, 0.330)
CODE_BG     = (0.110, 0.110, 0.150)
CODE_FG     = (0.870, 0.870, 0.830)
INFO_BG     = (0.875, 0.935, 1.000)
INFO_BD     = (0.180, 0.480, 0.900)
WARN_BG     = (1.000, 0.948, 0.820)
WARN_BD     = (0.880, 0.580, 0.090)
TIP_BG      = (0.875, 1.000, 0.890)
TIP_BD      = (0.090, 0.680, 0.300)
NAVY_LIGHT  = (0.200, 0.310, 0.470)

# ════════════════════════════════════════════════════════════
# TTF PARSER
# ════════════════════════════════════════════════════════════
def _u16(d,o): return struct.unpack_from('>H',d,o)[0]
def _i16(d,o): return struct.unpack_from('>h',d,o)[0]
def _u32(d,o): return struct.unpack_from('>I',d,o)[0]

class TTFFont:
    def __init__(self, path):
        with open(path,'rb') as f:
            self.data = f.read()
        self._load()

    def _load(self):
        d = self.data
        n = _u16(d,4)
        self.tbl = {}
        for i in range(n):
            b = 12+i*16
            self.tbl[d[b:b+4].decode('latin-1')] = (_u32(d,b+8), _u32(d,b+12))

        h = self.tbl['head'][0]
        self.upm  = _u16(d,h+18)
        self.bbox = [_i16(d,h+36),_i16(d,h+38),_i16(d,h+40),_i16(d,h+42)]

        a = self.tbl['hhea'][0]
        self.asc    = _i16(d,a+4)
        self.desc   = _i16(d,a+6)
        self.num_hm = _u16(d,a+34)

        if 'OS/2' in self.tbl:
            o = self.tbl['OS/2'][0]
            self.t_asc  = _i16(d,o+68)
            self.t_desc = _i16(d,o+70)
            self.cap_h  = _i16(d,o+88)
        else:
            self.t_asc=self.asc; self.t_desc=self.desc; self.cap_h=self.asc

        self.n_glyph = _u16(d, self.tbl['maxp'][0]+4)
        self.cmap    = self._cmap()
        self.wid     = self._hmtx()

    def _cmap(self):
        d=self.data; co=self.tbl['cmap'][0]
        n=_u16(d,co+2); best=None; bp=-1
        for i in range(n):
            b=co+4+i*8
            pl,en=_u16(d,b),_u16(d,b+2)
            so=co+_u32(d,b+4)
            if _u16(d,so)!=4: continue
            pr=3 if(pl==3 and en==1) else(2 if(pl==0 and en==3) else 1)
            if pr>bp: bp,best=pr,so
        return self._cm4(best) if best else {}

    def _cm4(self,off):
        d=self.data; sg=_u16(d,off+6)//2
        ea=off+14; sa=ea+2+sg*2; da=sa+sg*2; ra=da+sg*2
        cm={}
        for i in range(sg-1):
            end,st,dl,ro=_u16(d,ea+i*2),_u16(d,sa+i*2),_i16(d,da+i*2),_u16(d,ra+i*2)
            for c in range(st,end+1):
                if ro==0:
                    g=(c+dl)&0xFFFF
                else:
                    ix=ra+i*2+ro+(c-st)*2
                    g=_u16(d,ix) if ix+2<=len(d) else 0
                    if g: g=(g+dl)&0xFFFF
                if g: cm[c]=g
        return cm

    def _hmtx(self):
        d=self.data; ho=self.tbl['hmtx'][0]; w={}
        for i in range(min(self.num_hm,self.n_glyph)):
            w[i]=_u16(d,ho+i*4)
        lw=w.get(self.num_hm-1,500)
        for i in range(self.num_hm,self.n_glyph): w[i]=lw
        return w

    def glyph(self,cp):  return self.cmap.get(cp,0)
    def pdfw(self,gid):  return round(self.wid.get(gid,500)*1000/self.upm)
    def measure(self,text,sz):
        return sum(self.pdfw(self.glyph(ord(c))) for c in text)*sz/1000
    def asc_pt(self,sz):  return self.t_asc*sz/self.upm
    def desc_pt(self,sz): return abs(self.t_desc)*sz/self.upm
    def bbox_pdf(self):   return [round(v*1000/self.upm) for v in self.bbox]
    def cap_pdf(self):    return round(self.cap_h*1000/self.upm)

# ════════════════════════════════════════════════════════════
# RAW PDF OBJECT BUILDER
# ════════════════════════════════════════════════════════════
class _PObj:
    def __init__(self,oid): self.oid=oid; self.d={}; self.s=None

class PDFBuilder:
    def __init__(self):
        self._objs=[]; self._nid=1; self.root_id=1

    def obj(self):
        o=_PObj(self._nid); self._nid+=1; self._objs.append(o); return o

    @staticmethod
    def _fd(d):
        if not d: return b'<<>>'
        out=[b'<<']
        for k,v in d.items():
            vb=v if isinstance(v,bytes) else str(v).encode('latin-1')
            out.append(b'  '+k.encode('latin-1')+b' '+vb)
        out.append(b'>>')
        return b'\n'.join(out)

    def write(self,fp):
        fp.write(b'%PDF-1.7\n%\xe2\xe3\xcf\xd3\n')
        off={}
        for o in self._objs:
            off[o.oid]=fp.tell()
            fp.write(f'{o.oid} 0 obj\n'.encode())
            if o.s is not None:
                dd=dict(o.d); dd['/Length']=len(o.s)
                fp.write(self._fd(dd)); fp.write(b'\nstream\n')
                fp.write(o.s); fp.write(b'\nendstream\n')
            else:
                fp.write(self._fd(o.d)); fp.write(b'\n')
            fp.write(b'endobj\n\n')
        xr=fp.tell(); cnt=self._nid
        fp.write(f'xref\n0 {cnt}\n'.encode())
        fp.write(b'0000000000 65535 f \n')
        for oid in range(1,cnt):
            fp.write(f'{off.get(oid,0):010d} 00000 n \n'.encode())
        fp.write(b'trailer\n')
        fp.write(f'<</Size {cnt}/Root {self.root_id} 0 R>>\n'.encode())
        fp.write(f'startxref\n{xr}\n%%EOF\n'.encode())

# ════════════════════════════════════════════════════════════
# DOCUMENT — layout engine
# ════════════════════════════════════════════════════════════
class Doc:
    FK   = ['reg','bold','mono','mbold']
    FN   = ['F1','F2','F3','F4']
    FP   = [FONT_REG,FONT_BOLD,FONT_MONO,FONT_MONO_BOLD]
    FPDF = ['DejaVuSans','DejaVuSans-Bold','DejaVuSansMono','DejaVuSansMono-Bold']

    def __init__(self):
        print("Fontlar yukleniyor...")
        self.f    = {k:TTFFont(p) for k,p in zip(self.FK,self.FP)}
        self.fm   = {k:n for k,n in zip(self.FK,self.FN)}
        self.used = {k:set() for k in self.FK}
        self._pages=[]; self._sec=''; self._pgn=0
        self._stm=[]; self._y=0.0; self._open=False

    # ── page lifecycle ───────────────────────────────────────
    def new_page(self, section=None):
        if self._open: self._close_page()
        if section is not None: self._sec=section
        self._pgn+=1; self._stm=[]; self._open=True
        self._y = PH - HDR_H - MT
        self._header()
        print(f"\r  Sayfa {self._pgn}...", end='', flush=True)

    def _close_page(self):
        self._footer()
        self._pages.append(''.join(self._stm).encode('latin-1','replace'))
        self._open=False

    def _header(self):
        self._fill(*NAVY)
        self._rect(0, PH-HDR_H, PW, HDR_H, 'f')
        self._fill(*ORANGE)
        self._rect(0, PH-HDR_H-2, PW, 2, 'f')
        self._fill(*WHITE)
        sec = self._sec[:85] if self._sec else ''
        self._txy(sec,'bold',7.5, ML, PH-HDR_H+8)
        title="Claude Code Mobil Rehberi  |  @aykutuces"
        tw=self.f['bold'].measure(title,7.5)
        self._txy(title,'bold',7.5, PW-MR-tw, PH-HDR_H+8)

    def _footer(self):
        fy=MB-12
        self._stroke(*NAVY); self._lw(0.4)
        self._line(ML,fy+13,PW-MR,fy+13)
        self._fill(*NAVY)
        self._txy("Claude Code ile Mobil Uygulama Rehberi  |  @aykutuces",
                  'reg',7.5, ML, fy)
        ps=f"Sayfa {self._pgn}"
        pw=self.f['bold'].measure(ps,8.5)
        self._txy(ps,'bold',8.5, PW-MR-pw, fy)

    # ── stream primitives ────────────────────────────────────
    def _e(self,cmd): self._stm.append(cmd+'\n')
    def _fill(self,r,g,b):   self._e(f'{r:.4f} {g:.4f} {b:.4f} rg')
    def _stroke(self,r,g,b): self._e(f'{r:.4f} {g:.4f} {b:.4f} RG')
    def _lw(self,w):          self._e(f'{w:.2f} w')
    def _line(self,x1,y1,x2,y2): self._e(f'{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S')
    def _rect(self,x,y,w,h,op='f'):
        self._e(f'{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}')

    def _enc(self,text,fk):
        font=self.f[fk]; parts=[]
        for ch in text:
            gid=font.glyph(ord(ch)); self.used[fk].add(gid)
            parts.append(f'{gid:04X}')
        return '<'+''.join(parts)+'>'

    def _txy(self,text,fk,sz,x,y):
        if not text: return
        enc=self._enc(text,fk)
        self._e(f'BT /{self.fm[fk]} {sz:.2f} Tf {x:.2f} {y:.2f} Td {enc} Tj ET')

    # ── space guard ──────────────────────────────────────────
    def _need(self,pts):
        if self._y-pts < MB+8:
            self.new_page(); return True
        return False

    # ── word-wrap text ───────────────────────────────────────
    def text(self, txt, fk='reg', sz=11, color=BLACK,
             indent=0, lh=None, after=5):
        if not txt.strip(): self._y-=sz*0.4; return
        font=self.f[fk]; max_w=CW-indent
        lh=lh or sz*1.48; sw=font.measure(' ',sz)
        words=txt.split(); lines=[]; cur=[]; cw=0
        for w in words:
            ww=font.measure(w,sz)
            if cur and cw+sw+ww>max_w:
                lines.append(' '.join(cur)); cur=[w]; cw=ww
            else:
                if cur: cw+=sw
                cw+=ww; cur.append(w)
        if cur: lines.append(' '.join(cur))
        self._need(lh*len(lines)+after)
        self._fill(*color)
        for ln in lines:
            if self._y-lh<MB+8:
                self.new_page(); self._fill(*color)
            self._txy(ln,fk,sz,ML+indent,self._y)
            self._y-=lh
        self._y-=after

    # ── headings ─────────────────────────────────────────────
    def h1(self,txt, newpage=False):
        if newpage: self.new_page()
        self._need(58)
        self._fill(*NAVY)
        self._rect(ML-10,self._y-36,CW+20,46,'f')
        self._fill(*ORANGE)
        self._rect(ML-10,self._y-36,5,46,'f')
        self._fill(*WHITE)
        self._txy(txt,'bold',17,ML+4,self._y-22)
        self._y-=54

    def h2(self,txt):
        self._need(44)
        self._fill(*ORANGE)
        self._rect(ML-10,self._y-30,5,40,'f')
        self._fill(*NAVY)
        self._txy(txt,'bold',13,ML+4,self._y-18)
        self._y-=40

    def h3(self,txt):
        self._need(30)
        self._fill(*NAVY)
        self._txy(txt,'bold',11.5,ML,self._y)
        tw=self.f['bold'].measure(txt,11.5)
        self._stroke(*ORANGE); self._lw(1.2)
        self._line(ML,self._y-3,ML+tw,self._y-3)
        self._y-=24

    def h4(self,txt):
        self._need(22)
        self._fill(*GRAY_DARK)
        self._txy(txt,'bold',10.5,ML,self._y)
        self._y-=18

    # ── info / warning / tip boxes ───────────────────────────
    def box(self, txt, btype='info', title=None):
        font=self.f['reg']; sz=10; iw=CW-24
        sw=font.measure(' ',sz)
        words=txt.split(); lines=[]; cur=[]; cw=0
        for w in words:
            ww=font.measure(w,sz)
            if cur and cw+sw+ww>iw:
                lines.append(' '.join(cur)); cur=[w]; cw=ww
            else:
                if cur: cw+=sw
                cw+=ww; cur.append(w)
        if cur: lines.append(' '.join(cur))
        th=15 if title else 0
        bh=len(lines)*13+th+18
        self._need(bh+8)
        cfg={
            'info':    (INFO_BG,  INFO_BD, '[iPUCU]'),
            'warning': (WARN_BG,  WARN_BD, '[DiKKAT]'),
            'tip':     (TIP_BG,   TIP_BD,  '[PRO TUYO]'),
            'note':    (GRAY_BG,  GRAY_DARK,'[NOT]'),
        }.get(btype,(GRAY_BG,GRAY_DARK,'[NOT]'))
        bg,bd,lbl=cfg
        top=self._y
        self._fill(*bg)
        self._rect(ML,top-bh+6,CW,bh,'f')
        self._fill(*bd)
        self._rect(ML,top-bh+6,4,bh,'f')
        label=title if title else lbl
        self._fill(*bd)
        self._txy(label,'bold',9,ML+10,top-6)
        self._y=top-(th if th else 14)
        self._fill(*BLACK)
        for ln in lines:
            self._txy(ln,'reg',sz,ML+10,self._y)
            self._y-=13
        self._y-=11

    # ── code block ────────────────────────────────────────────
    def code(self, txt, lang=''):
        lines=txt.split('\n')
        bh=len(lines)*12+18
        self._need(bh+8)
        top=self._y
        self._fill(*CODE_BG)
        self._rect(ML,top-bh+4,CW,bh,'f')
        if lang:
            self._fill(0.55,0.55,0.55)
            lw=self.f['mono'].measure(lang,7.5)
            self._txy(lang,'mono',7.5,PW-MR-lw,top-4)
        self._y=top-10
        self._fill(*CODE_FG)
        for ln in lines:
            if self._y-12<MB+8: self.new_page(); self._fill(*CODE_FG)
            while ln and self.f['mono'].measure(ln,8)<CW-16:
                break
            else:
                while ln and self.f['mono'].measure(ln,8)>CW-16: ln=ln[:-1]
            self._txy(ln,'mono',8,ML+8,self._y)
            self._y-=12
        self._y-=10

    # ── table ─────────────────────────────────────────────────
    def table(self, headers, rows, widths=None):
        n=len(headers)
        if widths is None: widths=[CW/n]*n
        rh=17; hh=21; th=hh+len(rows)*rh+4
        self._need(th+8)
        x,y=ML,self._y
        self._fill(*NAVY)
        self._rect(x,y-hh+4,CW,hh,'f')
        self._fill(*WHITE); cx=x+5
        for i,h in enumerate(headers):
            self._txy(str(h),'bold',8.5,cx,y-14); cx+=widths[i]
        y-=hh
        for ri,row in enumerate(rows):
            self._fill(*(GRAY_BG if ri%2==0 else WHITE))
            self._rect(x,y-rh+4,CW,rh,'f')
            self._stroke(*GRAY_LINE); self._lw(0.2)
            self._line(x,y-rh+4,x+CW,y-rh+4)
            self._fill(*BLACK); cx=x+5
            for i,cell in enumerate(row):
                if i>=len(widths): break
                cs=str(cell)
                fn=self.f['reg']
                while cs and fn.measure(cs,8.5)>widths[i]-6: cs=cs[:-1]
                self._txy(cs,'reg',8.5,cx,y-11); cx+=widths[i]
            y-=rh
        self._stroke(*GRAY_LINE); self._lw(0.4)
        self._rect(x,y,CW,self._y-y,'S')
        self._y=y-8

    # ── bullet list ───────────────────────────────────────────
    def bullets(self, items, fk='reg', sz=11, indent=14):
        for item in items:
            font=self.f[fk]; iw=CW-indent-4; sw=font.measure(' ',sz); lh=sz*1.42
            words=item.split(); lines=[]; cur=[]; cw=0
            for w in words:
                ww=font.measure(w,sz)
                if cur and cw+sw+ww>iw:
                    lines.append(' '.join(cur)); cur=[w]; cw=ww
                else:
                    if cur: cw+=sw
                    cw+=ww; cur.append(w)
            if cur: lines.append(' '.join(cur))
            self._need(lh*len(lines)+3)
            self._fill(*ORANGE)
            self._txy('-','bold',sz,ML+indent-10,self._y)
            self._fill(*BLACK)
            for i,ln in enumerate(lines):
                self._txy(ln,fk,sz,ML+indent,self._y); self._y-=lh
        self._y-=3

    def sp(self,pts=8): self._y-=pts

    # ── section cover page ───────────────────────────────────
    def section_cover(self, num, title, subtitle='', desc=''):
        self.new_page(f'Bolum {num} - {title}')
        mid=PH*0.52
        # Decorative strip
        self._fill(*ORANGE)
        self._rect(0,PH-HDR_H-4,PW,4,'f')
        # Big navy block
        self._fill(*NAVY)
        self._rect(0,mid-65,PW,130,'f')
        # Thin orange accent line
        self._fill(*ORANGE)
        self._rect(0,mid+63,PW,3,'f')
        self._rect(0,mid-67,PW,3,'f')
        # Section number
        nt=f'BOLUM {num}'
        self._fill(*ORANGE)
        nw=self.f['bold'].measure(nt,13)
        self._txy(nt,'bold',13,(PW-nw)/2,mid+44)
        # Title
        self._fill(*WHITE)
        tw=self.f['bold'].measure(title,22)
        if tw<=CW+60:
            self._txy(title,'bold',22,(PW-tw)/2,mid+12)
        else:
            wds=title.split(); m=len(wds)//2
            l1=' '.join(wds[:m]); l2=' '.join(wds[m:])
            tw1=self.f['bold'].measure(l1,20); tw2=self.f['bold'].measure(l2,20)
            self._txy(l1,'bold',20,(PW-tw1)/2,mid+20)
            self._txy(l2,'bold',20,(PW-tw2)/2,mid+0)
        # Subtitle
        if subtitle:
            sw=self.f['reg'].measure(subtitle,11)
            self._fill(*ORANGE)
            self._txy(subtitle,'reg',11,(PW-sw)/2,mid-34)
        # Description box below
        if desc:
            self._y=mid-95
            self.box(desc,'info')
        else:
            self._y=mid-95
        # Bottom bar
        self._fill(*ORANGE)
        self._rect(0,MB+15,PW,3,'f')

    # ════════════════════════════════════════════════════════
    # FONT EMBEDDING
    # ════════════════════════════════════════════════════════
    def _tounicode(self,font,used):
        inv={}
        for cp,gid in font.cmap.items():
            if gid in used: inv.setdefault(gid,cp)
        items=sorted(inv.items())
        lines=['/CIDInit /ProcSet findresource begin','12 dict begin','begincmap',
               '/CIDSystemInfo << /Registry (Adobe) /Ordering (UCS) /Supplement 0 >> def',
               '/CMapName /Adobe-Identity-UCS def','/CMapType 2 def',
               '1 begincodespacerange','<0000> <FFFF>','endcodespacerange']
        i=0
        while i<len(items):
            ch=items[i:i+100]
            lines.append(f'{len(ch)} beginbfchar')
            for gid,cp in ch: lines.append(f'<{gid:04X}> <{cp:04X}>')
            lines.append('endbfchar'); i+=100
        lines+=['endcmap','CMapType findresource pop','end','end']
        return '\n'.join(lines).encode('latin-1','replace')

    def _Warray(self,font,used):
        gids=sorted(used)
        if not gids: return '[]'
        parts=[]; i=0
        while i<len(gids):
            g=gids[i]; run=[font.pdfw(g)]; i+=1
            while i<len(gids) and gids[i]==gids[i-1]+1:
                run.append(font.pdfw(gids[i])); i+=1
            parts.append(f'{g} [{" ".join(map(str,run))}]')
        return ' '.join(parts)

    def _embed(self,B,fk,fname,pname):
        font=self.f[fk]; used=self.used[fk] or {0}
        ff=B.obj(); ff.d={'/Length1':len(font.data)}; ff.s=font.data
        asc=round(font.t_asc*1000/font.upm)
        desc=round(font.t_desc*1000/font.upm)
        bb=' '.join(str(v) for v in font.bbox_pdf())
        fd=B.obj()
        fd.d={'/Type':'/FontDescriptor','/FontName':f'/{fname}',
              '/Flags':'32','/FontBBox':f'[{bb}]','/ItalicAngle':'0',
              '/Ascent':str(asc),'/Descent':str(desc),
              '/CapHeight':str(font.cap_pdf()),'/StemV':'80',
              '/FontFile2':f'{ff.oid} 0 R'}
        tu=B.obj(); tu.s=self._tounicode(font,used)
        Ws=self._Warray(font,used)
        cid=B.obj()
        cid.d={'/Type':'/Font','/Subtype':'/CIDFontType2',
               '/BaseFont':f'/{fname}',
               '/CIDSystemInfo':'<< /Registry (Adobe) /Ordering (Identity) /Supplement 0 >>',
               '/FontDescriptor':f'{fd.oid} 0 R','/DW':'556',
               '/W':f'[{Ws}]'}
        t0=B.obj()
        t0.d={'/Type':'/Font','/Subtype':'/Type0','/BaseFont':f'/{fname}',
              '/Encoding':'/Identity-H',
              '/DescendantFonts':f'[{cid.oid} 0 R]',
              '/ToUnicode':f'{tu.oid} 0 R'}
        return t0.oid

    # ════════════════════════════════════════════════════════
    # SAVE
    # ════════════════════════════════════════════════════════
    def save(self,path):
        if self._open: self._close_page()
        print(f'\n  {len(self._pages)} sayfa tamamlandi. PDF olusturuluyor...')
        B=PDFBuilder()
        cat=B.obj(); pages=B.obj()
        cs_ids=[]
        for stm in self._pages:
            o=B.obj(); o.s=stm; cs_ids.append(o.oid)
        fid={}
        for fk,fn,pn in zip(self.FK,self.FPDF,self.FN):
            fid[pn]=self._embed(B,fk,fn,pn)
        fres='<< '+' '.join(f'/{pn} {oid} 0 R' for pn,oid in fid.items())+' >>'
        pg_ids=[]
        for cid in cs_ids:
            pg=B.obj()
            pg.d={'/Type':'/Page','/Parent':f'{pages.oid} 0 R',
                  '/MediaBox':f'[0 0 {PW} {PH}]',
                  '/Contents':f'{cid} 0 R',
                  '/Resources':f'<< /Font {fres} >>'}
            pg_ids.append(pg.oid)
        kids=' '.join(f'{i} 0 R' for i in pg_ids)
        pages.d={'/Type':'/Pages','/Kids':f'[{kids}]','/Count':str(len(pg_ids))}
        cat.d={'/Type':'/Catalog','/Pages':f'{pages.oid} 0 R'}
        B.root_id=cat.oid
        with open(path,'wb') as f: B.write(f)
        sz=os.path.getsize(path)
        print(f'  Kaydedildi: {path}  ({sz//1024} KB,  {len(self._pages)} sayfa)')
        return len(self._pages)
