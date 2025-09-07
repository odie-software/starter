// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: ['nuxt-quasar-ui', '@pinia/nuxt'],
  runtimeConfig: {
    public: {
      apiUrl: 'http://api:8000',
      version: '1.0.0'
    }
  },
  quasar: {
    iconSet: 'mdi-v7',
    config: {
      brand: {
        primary: '#297373',
        secondary: '#26A69A',
        accent: '#3c153b',
        dark: '#1d1d1d',
        'dark-page': '#121212',
        positive: '#8ea604',
        negative: '#fe5f55',
        info: '#009ffd',
        warning: '#ffa400'
      }
    }
  }
})
