import React, { useMemo } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Modal } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useDailyRewardStore } from '../stores/dailyRewardStore';
import { usePowerUpStore } from '../stores/powerupStore';
import { useLivesStore } from '../stores/livesStore';
import { useGameStore } from '../stores/gameStore';
import {
  ACCENT_COLOR,
  TEXT_COLOR,
  SCORE_COLOR,
  SUCCESS_COLOR,
} from '../constants/colors';

interface Props {
  visible: boolean;
  onClose: () => void;
}

export default function DailyRewardModal({ visible, onClose }: Props) {
  const { t } = useTranslation();
  const streakDay = useDailyRewardStore((s) => s.streakDay);
  const lastClaimDate = useDailyRewardStore((s) => s.lastClaimDate);
  const claim = useDailyRewardStore((s) => s.claim);
  const getRewards = useDailyRewardStore((s) => s.getRewards);
  const addPowerUp = usePowerUpStore((s) => s.addPowerUp);
  const addLife = useLivesStore((s) => s.addLife);
  const addBonusMoves = useGameStore((s) => s.addBonusMoves);

  const rewards = useMemo(() => getRewards(), [streakDay, getRewards]);
  const canClaim = useMemo(() => {
    if (!lastClaimDate) return true;
    return lastClaimDate !== new Date().toISOString().split('T')[0];
  }, [lastClaimDate]);

  const handleClaim = () => {
    const reward = claim();
    if (!reward) return;

    switch (reward.type) {
      case 'moves':
        addBonusMoves(reward.amount);
        break;
      case 'powerup':
        if (reward.powerupType) {
          addPowerUp(reward.powerupType, reward.amount);
        }
        break;
      case 'lives':
        addLife(reward.amount);
        break;
    }
    onClose();
  };

  const getRewardIcon = (type: string, powerupType?: string) => {
    if (type === 'moves') return '🎯';
    if (type === 'lives') return '❤️';
    if (powerupType === 'rowBomb') return '💥';
    if (powerupType === 'colorBomb') return '🌈';
    if (powerupType === 'shuffle') return '🔀';
    return '🎁';
  };

  const getRewardText = (reward: typeof rewards[0]) => {
    if (reward.type === 'moves') return t('dailyReward.bonusMoves', { count: reward.amount });
    if (reward.type === 'lives') return t('dailyReward.bonusLives', { count: reward.amount });
    return t('dailyReward.powerup');
  };

  return (
    <Modal transparent visible={visible} animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.title}>{t('dailyReward.title')}</Text>

          <View style={styles.rewardsRow}>
            {rewards.map((reward) => (
              <View
                key={reward.day}
                style={[
                  styles.dayCard,
                  reward.claimed && styles.claimedCard,
                  reward.current && canClaim && styles.currentCard,
                ]}
              >
                <Text style={styles.dayText}>
                  {t('dailyReward.day', { number: reward.day })}
                </Text>
                <Text style={styles.rewardIcon}>
                  {getRewardIcon(reward.type, reward.powerupType)}
                </Text>
                {reward.claimed && <Text style={styles.checkmark}>✓</Text>}
              </View>
            ))}
          </View>

          {canClaim && (
            <TouchableOpacity style={styles.claimBtn} onPress={handleClaim}>
              <Text style={styles.claimText}>{t('dailyReward.claim')}</Text>
            </TouchableOpacity>
          )}

          <TouchableOpacity style={styles.closeBtn} onPress={onClose}>
            <Text style={styles.closeText}>{t('common.close')}</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.75)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modal: {
    backgroundColor: '#1A1A2E',
    borderRadius: 24,
    padding: 24,
    alignItems: 'center',
    width: '90%',
    borderWidth: 2,
    borderColor: SCORE_COLOR,
  },
  title: {
    color: SCORE_COLOR,
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  rewardsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: 8,
    marginBottom: 20,
  },
  dayCard: {
    width: 70,
    height: 80,
    borderRadius: 12,
    backgroundColor: 'rgba(255,255,255,0.06)',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255,255,255,0.1)',
    gap: 4,
  },
  claimedCard: {
    backgroundColor: 'rgba(46,213,115,0.15)',
    borderColor: SUCCESS_COLOR,
  },
  currentCard: {
    borderColor: SCORE_COLOR,
    borderWidth: 2,
    shadowColor: SCORE_COLOR,
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.5,
    shadowRadius: 8,
    elevation: 6,
  },
  dayText: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 10,
    fontWeight: '600',
  },
  rewardIcon: {
    fontSize: 24,
  },
  checkmark: {
    color: SUCCESS_COLOR,
    fontSize: 12,
    fontWeight: 'bold',
  },
  claimBtn: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 48,
    paddingVertical: 14,
    borderRadius: 16,
    marginBottom: 12,
    shadowColor: ACCENT_COLOR,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.4,
    shadowRadius: 8,
    elevation: 6,
  },
  claimText: {
    color: TEXT_COLOR,
    fontSize: 18,
    fontWeight: 'bold',
  },
  closeBtn: {
    paddingVertical: 8,
  },
  closeText: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: 14,
  },
});
