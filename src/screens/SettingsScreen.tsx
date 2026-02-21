import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Switch,
  ScrollView,
  Modal,
  Pressable,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { useTranslation } from 'react-i18next';
import { useSettingsStore } from '../stores/settingsStore';
import { SUPPORTED_LANGUAGES } from '../i18n';
import { soundManager } from '../services/SoundManager';
import { SCREEN_WIDTH } from '../constants/dimensions';

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
    <LinearGradient
      colors={['#7B2FF7', '#4A90D9', '#67D5B5']}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 0.3, y: 1 }}
    >
      {/* Modal kartı */}
      <View style={styles.card}>
        <LinearGradient
          colors={['#FFFBF0', '#FFF5E1', '#FFEED4']}
          style={styles.cardGradient}
          start={{ x: 0, y: 0 }}
          end={{ x: 0, y: 1 }}
        >
          {/* Üst banner */}
          <LinearGradient
            colors={['#8B5CF6', '#6D28D9']}
            style={styles.banner}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 0 }}
          >
            <Text style={styles.title}>{t('settings.title').toUpperCase()}</Text>
            <Pressable style={styles.closeBtn} onPress={onBack}>
              <Ionicons name="close" size={22} color="#fff" />
            </Pressable>
          </LinearGradient>

          {/* Toggle satırları */}
          <View style={styles.toggleSection}>
            {/* Ses */}
            <View style={styles.toggleRow}>
              <View style={styles.toggleIconBox}>
                <Ionicons name="volume-high" size={28} color="#F59E0B" />
              </View>
              <Switch
                value={soundEnabled}
                onValueChange={handleSoundToggle}
                trackColor={{ false: '#E5E7EB', true: '#86EFAC' }}
                thumbColor={soundEnabled ? '#22C55E' : '#9CA3AF'}
                style={styles.switch}
              />
              <Text style={[styles.toggleLabel, { color: soundEnabled ? '#22C55E' : '#9CA3AF' }]}>
                {soundEnabled ? 'ON' : 'OFF'}
              </Text>
            </View>

            {/* Haptics / Titreşim */}
            <View style={styles.toggleRow}>
              <View style={styles.toggleIconBox}>
                <Ionicons name="phone-portrait" size={28} color="#8B5CF6" />
              </View>
              <Switch
                value={hapticsEnabled}
                onValueChange={setHapticsEnabled}
                trackColor={{ false: '#E5E7EB', true: '#86EFAC' }}
                thumbColor={hapticsEnabled ? '#22C55E' : '#9CA3AF'}
                style={styles.switch}
              />
              <Text style={[styles.toggleLabel, { color: hapticsEnabled ? '#22C55E' : '#9CA3AF' }]}>
                {hapticsEnabled ? 'ON' : 'OFF'}
              </Text>
            </View>
          </View>

          {/* Dil seçimi */}
          <TouchableOpacity
            style={styles.langBtn}
            onPress={() => setShowLangModal(true)}
          >
            <LinearGradient
              colors={['#C084FC', '#A855F7']}
              style={styles.langBtnGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Ionicons name="globe-outline" size={18} color="#fff" />
              <Text style={styles.langBtnText}>{currentLangName}</Text>
            </LinearGradient>
          </TouchableOpacity>

          {/* Versiyon */}
          <Text style={styles.version}>Pop Blast v1.0.0</Text>
        </LinearGradient>
      </View>

      {/* Dil Seçim Modalı */}
      <Modal transparent visible={showLangModal} animationType="fade">
        <View style={styles.modalOverlay}>
          <View style={styles.langModal}>
            <LinearGradient
              colors={['#FFFBF0', '#FFF5E1']}
              style={styles.langModalGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 0, y: 1 }}
            >
              <Text style={styles.langTitle}>{t('settings.selectLanguage')}</Text>
              <ScrollView style={styles.langList} showsVerticalScrollIndicator={false}>
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
                      <Ionicons name="checkmark-circle" size={20} color="#8B5CF6" />
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
            </LinearGradient>
          </View>
        </View>
      </Modal>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  card: {
    width: SCREEN_WIDTH * 0.85,
    borderRadius: 28,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 12 },
    shadowOpacity: 0.3,
    shadowRadius: 20,
    elevation: 16,
  },
  cardGradient: {
    alignItems: 'center',
    paddingBottom: 20,
  },
  banner: {
    width: '100%',
    paddingVertical: 20,
    alignItems: 'center',
    borderTopLeftRadius: 28,
    borderTopRightRadius: 28,
  },
  title: {
    color: '#fff',
    fontSize: 26,
    fontWeight: '900',
    letterSpacing: 2,
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
  closeBtn: {
    position: 'absolute',
    right: 16,
    top: 16,
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: 'rgba(0,0,0,0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  toggleSection: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 32,
    paddingVertical: 28,
    paddingHorizontal: 20,
  },
  toggleRow: {
    alignItems: 'center',
    gap: 8,
  },
  toggleIconBox: {
    width: 60,
    height: 60,
    borderRadius: 16,
    backgroundColor: '#FFF8E1',
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  switch: {
    marginTop: 4,
  },
  toggleLabel: {
    fontSize: 13,
    fontWeight: '800',
    letterSpacing: 1,
  },
  langBtn: {
    width: '70%',
    borderRadius: 20,
    overflow: 'hidden',
    marginBottom: 16,
  },
  langBtnGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 14,
  },
  langBtnText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '700',
  },
  version: {
    color: '#BDBDBD',
    fontSize: 11,
    marginTop: 4,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.7)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  langModal: {
    width: SCREEN_WIDTH * 0.85,
    maxHeight: '70%',
    borderRadius: 24,
    overflow: 'hidden',
  },
  langModalGradient: {
    padding: 20,
  },
  langTitle: {
    color: '#5D4037',
    fontSize: 20,
    fontWeight: '900',
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
    paddingVertical: 14,
    paddingHorizontal: 16,
    borderRadius: 12,
    marginBottom: 4,
  },
  langRowActive: {
    backgroundColor: 'rgba(139,92,246,0.1)',
  },
  langName: {
    color: '#5D4037',
    fontSize: 15,
    fontWeight: '500',
  },
  langNameActive: {
    color: '#8B5CF6',
    fontWeight: '800',
  },
  langCloseBtn: {
    alignItems: 'center',
    paddingVertical: 14,
    marginTop: 8,
    backgroundColor: 'rgba(0,0,0,0.05)',
    borderRadius: 14,
  },
  langCloseText: {
    color: '#9E9E9E',
    fontSize: 15,
    fontWeight: '600',
  },
});
