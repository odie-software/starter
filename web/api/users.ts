import { type User } from '~/types/user';

export const createUsersApi = (fetch: typeof $fetch) => ({
    me: () => {
        return fetch<User>('/api/users/me')
    }
})
