export interface User {
    email: string;
    first_name: string;
    last_name: string;
    id: number;
}

export type UserCreatePayload = Omit<User, 'id'> & { password: string }
