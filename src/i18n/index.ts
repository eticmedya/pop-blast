import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import { getLocales } from 'expo-localization';

import en from './locales/en.json';
import tr from './locales/tr.json';
import de from './locales/de.json';
import fr from './locales/fr.json';
import es from './locales/es.json';
import pt from './locales/pt.json';
import ru from './locales/ru.json';
import ja from './locales/ja.json';
import ko from './locales/ko.json';
import zhCN from './locales/zh-CN.json';
import zhTW from './locales/zh-TW.json';
import ar from './locales/ar.json';
import hi from './locales/hi.json';
import it from './locales/it.json';
import nl from './locales/nl.json';
import pl from './locales/pl.json';
import sv from './locales/sv.json';
import no from './locales/no.json';
import da from './locales/da.json';
import fi from './locales/fi.json';

const resources = {
  en: { translation: en },
  tr: { translation: tr },
  de: { translation: de },
  fr: { translation: fr },
  es: { translation: es },
  pt: { translation: pt },
  ru: { translation: ru },
  ja: { translation: ja },
  ko: { translation: ko },
  'zh-CN': { translation: zhCN },
  'zh-TW': { translation: zhTW },
  ar: { translation: ar },
  hi: { translation: hi },
  it: { translation: it },
  nl: { translation: nl },
  pl: { translation: pl },
  sv: { translation: sv },
  no: { translation: no },
  da: { translation: da },
  fi: { translation: fi },
};

export const SUPPORTED_LANGUAGES = [
  { code: 'en', name: 'English' },
  { code: 'tr', name: 'Turkce' },
  { code: 'de', name: 'Deutsch' },
  { code: 'fr', name: 'Francais' },
  { code: 'es', name: 'Espanol' },
  { code: 'pt', name: 'Portugues' },
  { code: 'ru', name: 'Russkiy' },
  { code: 'ja', name: 'Nihongo' },
  { code: 'ko', name: 'Hangugeo' },
  { code: 'zh-CN', name: 'Zhongwen (Jianti)' },
  { code: 'zh-TW', name: 'Zhongwen (Fanti)' },
  { code: 'ar', name: 'Arabiya' },
  { code: 'hi', name: 'Hindi' },
  { code: 'it', name: 'Italiano' },
  { code: 'nl', name: 'Nederlands' },
  { code: 'pl', name: 'Polski' },
  { code: 'sv', name: 'Svenska' },
  { code: 'no', name: 'Norsk' },
  { code: 'da', name: 'Dansk' },
  { code: 'fi', name: 'Suomi' },
];

function getDeviceLanguage(): string {
  try {
    const locales = getLocales();
    if (locales.length > 0) {
      const tag = locales[0].languageTag;
      // Check exact match first (zh-CN, zh-TW)
      if (resources[tag as keyof typeof resources]) return tag;
      // Check language code only (en, tr, de, etc.)
      const lang = tag.split('-')[0];
      if (resources[lang as keyof typeof resources]) return lang;
    }
  } catch {}
  return 'en';
}

i18n.use(initReactI18next).init({
  resources,
  lng: getDeviceLanguage(),
  fallbackLng: 'en',
  interpolation: { escapeValue: false },
  react: { useSuspense: false },
});

export default i18n;
