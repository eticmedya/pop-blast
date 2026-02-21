const { getDefaultConfig } = require('expo/metro-config');

const config = getDefaultConfig(__dirname);

// Web'de ESM yerine CJS çözümleme - import.meta hatasını önler
config.resolver.unstable_conditionNames = ['require'];
config.resolver.unstable_conditionsByPlatform = {
  ios: ['react-native'],
  android: ['react-native'],
  web: ['browser', 'require'],
};

module.exports = config;
