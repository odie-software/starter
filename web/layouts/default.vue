<template>
  <q-layout class="bg-white flex">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>Starter
        </q-toolbar-title>
        <q-spacer />

      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawer" :width="200" :breakpoint="500">
      <q-scroll-area class="fit">
        <q-list padding class="menu-list">

          <q-item @click="navigateTo(item)" :active="router.currentRoute.value.path == item.to" v-for="item in menuItems" clickable v-ripple>
            <q-item-section avatar>
              <q-icon :name="item.icon" />
            </q-item-section>

            <q-item-section>
              {{ item.label }}
            </q-item-section>
          </q-item>


        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container class="full-width full-height">
      <div class="q-ma-md">
      <slot />
    </div>
    </q-page-container>

    <q-footer class="q-pa-sm bg-grey-4 text-grey-6">
      <div class="text-right">{{ version }}</div>
    </q-footer>
  </q-layout>
</template>

<script lang="ts" setup>
const api = useApi()
const version = useVersion()
const drawer = ref(true)
const router = useRouter()


interface MenuItem {
  label: string;
  icon: string;
  to: string;
}

const menuItems = ref([
  {
    label: 'Time Tracking',
    icon: 'mdi-clock-outline',
    to: '/time-tracking'
  }
]) as Ref<MenuItem[]>

const navigateTo = (item: MenuItem) => {
  router.push(item.to)
}
</script>

<style>

</style>
