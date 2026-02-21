import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Switch,
  ScrollView,
  Modal,
} from 'react-native';
import { useTranslation } from 'react-i18next';
import { useSettingsStore } from '../stores/settingsStore';
import { SUPPORTED_LANGUAGES } from '../i18n';
import { BG_COLOR, TEXT_COLOR, ACCENT_COLOR } from '../constants/colors';
import { soundManager } from '../services/SoundManager';

interface Props {
  onBack: () => void;
}

export default function SettingsScreen({ onBack }: Props) {
  const { t } = useTranslation();
  const soundEnabled = useSettingsStore((s) => s.soundEnabled);
  const hapticsEnabled = useSettingsStore((s) => s.hapticsEnabled);
  const language = useSettingsStore((s) => s.language);
  const setSoundEnabled = useSettingsStore((s) => s.setSoundEnabled);
  const setHapticsEnabled = useSettingsStore((s) => s.setHapticsEnabled);
  const setLanguage = useSettingsStore((s) => s.setLanguage);

  const [showLangModal, setShowLangModal] = useState(false);

  const currentLangName =
    SUPPORTED_LANGUAGES.find((l) => l.code === language)?.name ?? 'English';

  const handleSoundToggle = (val: boolean) => {
    setSoundEnabled(val);
    soundManager.setMuted(!val);
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={onBack} style={styles.backBtn}>
          <Text style={styles.backText}>{'<'} {t('settings.back')}</Text>
        </TouchableOpacity>
        <Text style={styles.title}>{t('settings.title')}</Text>
        <View style={styles.backBtn} />
      </View>

      <View style={styles.section}>
        {/* Sound */}
        <View style={styles.row}>
          <Text style={styles.rowLabel}>🔊 {t('settings.sound')}</Text>
          <Switch
            value={soundEnabled}
            onValueChange={handleSoundToggle}
            trackColor={{ false: 'rgba(255,255,255,0.1)', true: ACCENT_COLOR }}
            thumbColor="#fff"
          />
        </View>

        {/* Haptics */}
        <View style={styles.row}>
          <Text style={styles.rowLabel}>📳 {t('settings.haptics')}</Text>
          <Switch
            value={hapticsEnabled}
            onValueChange={setHapticsEnabled}
            trackColor={{ false: 'rgba(255,255,255,0.1)', true: ACCENT_COLOR }}
            thumbColor="#fff"
          />
        </View>

        {/* Language */}
        <TouchableOpacity
          style={styles.row}
          onPress={() => setShowLangModal(true)}
        >
          <Text style={styles.rowLabel}>🌐 {t('settings.language')}</Text>
          <Text style={styles.rowValue}>{currentLangName} ›</Text>
        </TouchableOpacity>
      </View>

      <Text style={styles.version}>Pop Blast v1.0.0</Text>

      {/* Language Selection Modal */}
      <Modal transparent visible={showLangModal} animationType="fade">
        <View style={styles.modalOverlay}>
          <View style={styles.langModal}>
            <Text style={styles.langTitle}>{t('settings.selectLanguage')}</Text>
            <ScrollView style={styles.langList}>
              {SUPPORTED_LANGUAGES.map((lang) => (
                <TouchableOpacity
                  key={lang.code}
                  style={[
                    styles.langRow,
                    lang.code === language && styles.langRowActive,
                  ]}
                  onPress={() => {
                    setLanguage(lang.code);
                    setShowLangModal(false);
                  }}
                >
                  <Text
                    style={[
                      styles.langName,
                      lang.code === language && styles.langNameActive,
                    ]}
                  >
                    {lang.name}
                  </Text>
                  {lang.code === language && (
                    <Text style={styles.langCheck}>✓</Text>
                  )}
                </TouchableOpacity>
              ))}
            </ScrollView>
            <TouchableOpacity
              style={styles.langCloseBtn}
              onPress={() => setShowLangModal(false)}
            >
              <Text style={styles.langCloseText}>{t('common.close')}</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: BG_COLOR,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingTop: 60,
    paddingBottom: 16,
  },
  backBtn: {
    width: 80,
  },
  backText: {
    color: ACCENT_COLOR,
    fontSize: 16,
    fontWeight: '600',
  },
  title: {
    color: TEXT_COLOR,
    fontSize: 22,
    fontWeight: '900',
    letterSpacing: 1,
  },
  section: {
    margin: 20,
    backgroundColor: 'rgba(255,255,255,0.04)',
    borderRadius: 16,
    overflow: 'hidden',
  },
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingVertical: 16,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.05)',
  },
  rowLabel: {
    color: TEXT_COLOR,
    fontSize: 16,
    fontWeight: '500',
  },
  rowValue: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 14,
  },
  version: {
    color: 'rgba(255,255,255,0.2)',
    fontSize: 12,
    textAlign: 'center',
    marginTop: 40,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  langModal: {
    backgroundColor: '#1A1A2E',
    borderRadius: 20,
    padding: 20,
    width: '85%',
    maxHeight: '70%',
  },
  langTitle: {
    color: TEXT_COLOR,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 16,
  },
  langList: {
    maxHeight: 400,
  },
  langRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 10,
    marginBottom: 4,
  },
  langRowActive: {
    backgroundColor: 'rgba(255,107,53,0.15)',
  },
  langName: {
    color: 'rgba(255,255,255,0.7)',
    fontSize: 15,
  },
  langNameActive: {
    color: ACCENT_COLOR,
    fontWeight: 'bold',
  },
  langCheck: {
    color: ACCENT_COLOR,
    fontSize: 16,
    fontWeight: 'bold',
  },
  langCloseBtn: {
    alignItems: 'center',
    paddingVertical: 12,
    marginTop: 8,
  },
  langCloseText: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: 14,
  },
});
