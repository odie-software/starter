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
})
