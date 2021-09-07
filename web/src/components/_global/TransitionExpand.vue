<script setup lang="ts">
// Full explanation: https://markus.oberlehner.net/blog/transition-to-height-auto-with-vue/
function enter(element) {
  const { width } = getComputedStyle(element)

  element.style.width = width
  element.style.position = 'absolute'
  element.style.visibility = 'hidden'
  element.style.height = 'auto'

  const { height } = getComputedStyle(element)

  element.style.width = null
  element.style.position = null
  element.style.visibility = null
  element.style.height = 0

  // Force repaint to make sure the animation is triggered correctly.
  getComputedStyle(element).height // eslint-disable-line no-unused-expressions

  // Trigger the animation.
  // We use `setTimeout` because we need to make sure the browser has finished
  // painting after setting the `height` to `0` in the line above.
  setTimeout(() => {
    element.style.height = height
  })
}

function afterEnter(element) {
  element.style.height = 'auto'
}

function leave(element) {
  const { height } = getComputedStyle(element)

  element.style.height = height

  // Force repaint to make sure the animation is triggered correctly.
  getComputedStyle(element).height // eslint-disable-line no-unused-expressions

  setTimeout(() => {
    element.style.height = 0
  })
}
</script>

<template>
  <transition
    name="expand"
    @enter="enter"
    @after-enter="afterEnter"
    @leave="leave"
  >
    <slot />
  </transition>
</template>

<style>
.expand-enter-active,
.expand-leave-active {
  overflow: hidden;
  transition: height 0.3s ease-in-out;
}

.expand-enter,
.expand-leave-to {
  height: 0;
}
</style>
