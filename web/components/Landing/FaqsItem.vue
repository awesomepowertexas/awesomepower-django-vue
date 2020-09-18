<template>
  <div>
    <div class="flex items-start cursor-pointer mt-6" @click="$emit('toggle')">
      <div class="w-8 flex-shrink-0 md:pt-1">
        <font-awesome-icon
          :class="{ flipped: isOpen }"
          class="chevron-icon text-blue-500"
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
        class="text-gray-700 text-sm md:text-base leading-loose pl-8"
      >
        <div class="h-4" />
        <slot name="answer" />
      </div>
    </transition-expand>
  </div>
</template>

<script>
export default {
  props: {
    isOpen: Boolean,
  },
}
</script>

<style scoped lang="postcss">
.chevron-icon {
  transition: transform 0.3s ease;
}

.chevron-icon.flipped {
  transform: rotate(-180deg);
}
</style>
