<script setup>
const _props = defineProps({
  isOpen: Boolean,
})

const _emits = defineEmits(['toggle'])
</script>

<template>
  <div>
    <div
      class="faq-question flex items-start cursor-pointer mt-6"
      @click="$emit('toggle')"
    >
      <div class="w-8 flex-shrink-0 md:pt-1">
        <font-awesome-icon
          :class="{ 'transform -rotate-180': isOpen }"
          class="text-blue-500 transition"
          icon="chevron-circle-down"
        />
      </div>

      <div class="flex-grow">
        <p class="font-bold md:text-xl md:pt-px">
          <slot name="question" />
        </p>
      </div>
    </div>

    <transition-expand>
      <div
        v-if="isOpen"
        class="text-gray-700 text-sm leading-loose md:text-base md:leading-loose pl-8"
      >
        <div class="h-4" />
        <slot name="answer" />
      </div>
    </transition-expand>
  </div>
</template>
