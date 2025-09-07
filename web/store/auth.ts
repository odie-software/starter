import { defineStore } from 'pinia';
import { type LoginCredentials } from '~/types/auth';

interface AuthState {
  status: 'idle' | 'pending' | 'success' | 'error';
  user: User | null;
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    status: 'idle',
    user: null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
  },

  actions: {
    async login(credentials: LoginCredentials) {
      this.status = 'pending';
      try {
        await useApi().auth.login(credentials);
        await this.fetchUser();
        this.status = 'success';
        navigateTo('/');
      } catch (error) {
        this.status = 'error';
        console.error("Login failed:", error);
      }
    },

    async logout() {
      this.status = 'pending';
      try {
        await useApi().auth.logout();
        this.user = null;
        this.status = 'success';
        navigateTo('/login');
      } catch (error) {
        this.status = 'error';
        console.error("Logout failed:", error);
      }
    },

    async fetchUser() {
      try {
        this.user = await useApi().auth.getUser();
      } catch (error) {
        this.user = null;
      }
    }
  },
});
