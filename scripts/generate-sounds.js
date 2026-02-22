/**
 * Generate game sound effects as WAV files using Node.js
 * No external dependencies needed - pure Buffer manipulation
 */
const fs = require('fs');
const path = require('path');

const SAMPLE_RATE = 22050; // Lower sample rate for smaller files
const outputDir = path.join(__dirname, '..', 'assets', 'sounds');

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

function createWavBuffer(samples, sampleRate = SAMPLE_RATE) {
  const numSamples = samples.length;
  const byteRate = sampleRate * 2; // 16-bit mono
  const dataSize = numSamples * 2;
  const buffer = Buffer.alloc(44 + dataSize);

  // WAV header
  buffer.write('RIFF', 0);
  buffer.writeUInt32LE(36 + dataSize, 4);
  buffer.write('WAVE', 8);
  buffer.write('fmt ', 12);
  buffer.writeUInt32LE(16, 16); // chunk size
  buffer.writeUInt16LE(1, 20); // PCM
  buffer.writeUInt16LE(1, 22); // mono
  buffer.writeUInt32LE(sampleRate, 24);
  buffer.writeUInt32LE(byteRate, 28);
  buffer.writeUInt16LE(2, 32); // block align
  buffer.writeUInt16LE(16, 34); // bits per sample
  buffer.write('data', 36);
  buffer.writeUInt32LE(dataSize, 40);

  // Write samples
  for (let i = 0; i < numSamples; i++) {
    const val = Math.max(-1, Math.min(1, samples[i]));
    buffer.writeInt16LE(Math.round(val * 32767), 44 + i * 2);
  }
  return buffer;
}

function generateSamples(durationSec, fn) {
  const numSamples = Math.floor(SAMPLE_RATE * durationSec);
  const samples = new Float64Array(numSamples);
  for (let i = 0; i < numSamples; i++) {
    const t = i / SAMPLE_RATE;
    samples[i] = fn(t, i, numSamples);
  }
  return samples;
}

// Envelope helpers
function envelope(t, attack, decay, sustain, release, total) {
  if (t < attack) return t / attack;
  if (t < attack + decay) return 1 - (1 - sustain) * ((t - attack) / decay);
  if (t < total - release) return sustain;
  return sustain * ((total - t) / release);
}

function expDecay(t, duration) {
  return Math.exp(-4 * t / duration);
}

// ===== SOUND GENERATORS =====

// TAP: Short percussive click
function generateTap() {
  return generateSamples(0.08, (t, i, n) => {
    const env = expDecay(t, 0.08);
    const click = Math.sin(2 * Math.PI * 800 * t) * 0.6;
    const noise = (Math.random() * 2 - 1) * 0.4;
    return (click + noise) * env;
  });
}

// SWAP: Quick whoosh
function generateSwap() {
  return generateSamples(0.2, (t, i, n) => {
    const env = Math.sin(Math.PI * t / 0.2); // bell curve
    const freq = 200 + 600 * (t / 0.2); // rising frequency
    const wave = Math.sin(2 * Math.PI * freq * t) * 0.3;
    const noise = (Math.random() * 2 - 1) * 0.15;
    return (wave + noise) * env * 0.7;
  });
}

// MATCH: Satisfying pop/burst
function generateMatch() {
  return generateSamples(0.3, (t, i, n) => {
    const env = expDecay(t, 0.15);
    const pop = Math.sin(2 * Math.PI * 520 * t) * 0.5;
    const harmonic = Math.sin(2 * Math.PI * 1040 * t) * 0.25;
    const highPop = Math.sin(2 * Math.PI * 1560 * t) * 0.1;
    const burst = (Math.random() * 2 - 1) * 0.2 * expDecay(t, 0.05);
    return (pop + harmonic + highPop + burst) * env;
  });
}

// COMBO: Ascending chime (sparkly)
function generateCombo() {
  return generateSamples(0.6, (t, i, n) => {
    let val = 0;
    const notes = [523, 659, 784, 1047]; // C5, E5, G5, C6
    for (let j = 0; j < notes.length; j++) {
      const noteStart = j * 0.12;
      if (t >= noteStart) {
        const noteT = t - noteStart;
        const noteEnv = expDecay(noteT, 0.25);
        val += Math.sin(2 * Math.PI * notes[j] * noteT) * 0.25 * noteEnv;
        // Add shimmer
        val += Math.sin(2 * Math.PI * notes[j] * 2.01 * noteT) * 0.08 * noteEnv;
      }
    }
    return val;
  });
}

// CANNON: Deep boom with rumble
function generateCannon() {
  return generateSamples(0.5, (t, i, n) => {
    const env = expDecay(t, 0.25);
    // Deep thud
    const bass = Math.sin(2 * Math.PI * 60 * t) * 0.6 * expDecay(t, 0.2);
    // Mid punch
    const mid = Math.sin(2 * Math.PI * 150 * t) * 0.3 * expDecay(t, 0.15);
    // Impact noise
    const noise = (Math.random() * 2 - 1) * 0.4 * expDecay(t, 0.08);
    // Rumble
    const rumble = Math.sin(2 * Math.PI * 40 * t + Math.sin(2 * Math.PI * 5 * t) * 2) * 0.2 * expDecay(t, 0.4);
    return (bass + mid + noise + rumble) * env;
  });
}

// WIN: Victory fanfare (bright ascending)
function generateWin() {
  return generateSamples(1.5, (t, i, n) => {
    let val = 0;
    // Fanfare notes: C-E-G-C (ascending, staggered)
    const fanfare = [
      { freq: 523, start: 0, dur: 0.4 },     // C5
      { freq: 659, start: 0.2, dur: 0.4 },    // E5
      { freq: 784, start: 0.4, dur: 0.5 },    // G5
      { freq: 1047, start: 0.6, dur: 0.8 },   // C6
      { freq: 1319, start: 0.8, dur: 0.7 },   // E6
    ];
    for (const note of fanfare) {
      if (t >= note.start && t < note.start + note.dur) {
        const nt = t - note.start;
        const env = Math.sin(Math.PI * nt / note.dur);
        val += Math.sin(2 * Math.PI * note.freq * nt) * 0.2 * env;
        val += Math.sin(2 * Math.PI * note.freq * 1.5 * nt) * 0.08 * env; // 5th harmonic
      }
    }
    // Sparkle overlay
    if (t > 0.6) {
      const sparkleT = t - 0.6;
      val += Math.sin(2 * Math.PI * 2093 * sparkleT) * 0.05 * expDecay(sparkleT, 0.5);
    }
    return val * 1.2;
  });
}

// LOSE: Sad descending tones
function generateLose() {
  return generateSamples(1.2, (t, i, n) => {
    let val = 0;
    // Descending sad notes
    const notes = [
      { freq: 392, start: 0, dur: 0.35 },     // G4
      { freq: 349, start: 0.3, dur: 0.35 },    // F4
      { freq: 311, start: 0.6, dur: 0.5 },     // Eb4
      { freq: 261, start: 0.85, dur: 0.35 },   // C4
    ];
    for (const note of notes) {
      if (t >= note.start && t < note.start + note.dur) {
        const nt = t - note.start;
        const env = expDecay(nt, note.dur * 0.8);
        val += Math.sin(2 * Math.PI * note.freq * nt) * 0.3 * env;
        // Slight detuning for sadness
        val += Math.sin(2 * Math.PI * (note.freq * 1.003) * nt) * 0.1 * env;
      }
    }
    return val;
  });
}

// ===== GENERATE ALL SOUNDS =====
const sounds = {
  tap: generateTap(),
  swap: generateSwap(),
  match: generateMatch(),
  combo: generateCombo(),
  cannon: generateCannon(),
  win: generateWin(),
  lose: generateLose(),
};

for (const [name, samples] of Object.entries(sounds)) {
  const wavBuffer = createWavBuffer(samples);
  const filePath = path.join(outputDir, `${name}.wav`);
  fs.writeFileSync(filePath, wavBuffer);
  const sizeKB = (wavBuffer.length / 1024).toFixed(1);
  console.log(`Generated ${name}.wav (${sizeKB} KB, ${(samples.length / SAMPLE_RATE).toFixed(2)}s)`);
}

console.log('\nAll sound effects generated!');
