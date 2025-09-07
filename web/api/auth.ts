import { type LoginCredentials } from '~/types/auth';
import { type User } from '~/types/user';

export const createAuthApi = (fetch: typeof $fetch) => ({
    login: (credentials: LoginCredentials) => {
        return fetch('/auth/login/', {
            method: 'POST',
            body: credentials,
        })
    },
    logout: () => {
        return fetch('/auth/logout/', {
            method: 'POST',
        })
    },
    getUser: () => {
        return fetch<User>('/auth/user/')
    },
})
