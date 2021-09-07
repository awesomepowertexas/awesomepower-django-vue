<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import api from '~/plugins/api'
import global from '~/global'
import { useRouter } from 'vue-router'

const router = useRouter()

const zipCode = ref('')
const loading = ref(false)
const apiError = ref(false)
const input = ref(null)

watch(zipCode, async () => {
  global.plans = []
  apiError.value = false

  if (zipCode.value.length === 5) {
    loading.value = true

    let response
    try {
      response = await api.get(`/plans?zip_code=${zipCode.value}`)
    } catch (error) {
      apiError.value = true
      loading.value = false
      return
    }

    global.plans = response.data
    loading.value = false
  }
})

onMounted(() => {
  input.value.focus()
})

function onlyNumber($event) {
  if ($event.key < '0' || $event.key > '9') {
    $event.preventDefault()
  }
}

function viewPlans() {
  if (global.plans.length > 0) {
    router.push(`/plans/${zipCode.value}`)
  }
}
</script>

<template>
  <div class="w-full max-w-md bg-blue-900 text-center rounded-lg shadow p-5">
    <p
      class="h-10 flex items-center justify-center font-solway font-bold text-white md:text-xl uppercase"
    >
      View plans in your zip code
    </p>

    <input
      ref="input"
      v-model="zipCode"
      :disabled="loading"
      type="text"
      class="my-4 w-56 h-16 rounded text-3xl text-center text-gray-800 font-solway font-light"
      placeholder="12345"
      maxlength="5"
      @keypress="onlyNumber"
      @keypress.enter="viewPlans"
    />

    <div class="h-10 relative">
      <template v-if="zipCode.length === 5">
        <Transition name="fade">
          <div
            v-if="loading"
            key="loading"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <LoadingSpinner class="text-white" />
          </div>

          <div
            v-else-if="apiError"
            key="error"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <p
              class="font-bold tracking-widest text-red-300 text-xs uppercase pb-1"
            >
              Sorry, something went wrong
            </p>
          </div>

          <div
            v-else-if="global.plans.length === 0"
            key="no-plans"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <p
              class="font-bold tracking-widest text-red-300 text-xs uppercase pb-1"
            >
              No plans found for this zip code
            </p>
          </div>

          <div
            v-else
            key="plans"
            class="absolute w-full h-full flex items-center justify-center"
          >
            <router-link :to="`/plans/${zipCode}`">
              <AppButton class="btn-green">
                View {{ global.plans.length }} plans
              </AppButton>
            </router-link>
          </div>
        </Transition>
      </template>
    </div>
  </div>
</template>
