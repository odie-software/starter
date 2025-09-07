<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex flex-center bg-grey-2">
        <q-card class="q-pa-md shadow-2 my-card" bordered>
          <q-card-section class="text-center">
            <div class="text-grey-9 text-h5 text-weight-bold">Sign in</div>
          </q-card-section>
          <q-card-section>
            <q-form @submit="onSubmit">
              <q-input dense outlined v-model="email" label="Email Address" class="q-mb-md" />
              <q-input dense outlined v-model="password" type="password" label="Password" />
              <q-btn type="submit" color="primary" size="md" label="Sign in" no-caps class="full-width q-mt-md"></q-btn>
            </q-form>
          </q-card-section>

        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts" setup>
import { useAuthStore } from '~/store/auth';

const email = ref('');
const password = ref('');
const authStore = useAuthStore();

const onSubmit = () => {
  authStore.login({ email: email.value, password: password.value });
};

definePageMeta({
  layout: false
})
</script>
