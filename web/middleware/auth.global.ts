import { useAuthStore } from '~/store/auth';

export default defineNuxtRouteMiddleware(async (to, from) => {
    // Make sure middleware runs client-only
    if (import.meta.server) return

    const authStore = useAuthStore();

    // On initial app load, fetch the user to check for an existing session.
    if (!authStore.user) {
        await authStore.fetchUser();
    }

    // If the user is not authenticated and is trying to access a protected page,
    // redirect them to the login page.
    if (!authStore.isAuthenticated && to.path !== '/login') {
        return navigateTo('/login');
    }

    // If the user is authenticated and tries to access the login page,
    // redirect them to the home page.
    if (authStore.isAuthenticated && to.path === '/login') {
        return navigateTo('/');
    }
});
