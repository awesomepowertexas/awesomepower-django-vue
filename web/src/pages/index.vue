<template>
  <div class="relative">
    <img
      src="/src/assets/svg/intro-bg-mobile.svg"
      class="md:hidden -z-10 absolute w-screen h-screen top-0 left-0"
    />

    <img
      src="/src/assets/svg/intro-bg.svg"
      class="hidden md:block -z-10 absolute w-screen h-screen top-0 left-0"
    />

    <img
      id="svg-pawprints-mobile"
      src="/src/assets/svg/pawprints-mobile.svg"
      class="-z-10 absolute md:hidden w-screen left-0"
    />

    <div
      id="svg-pawprints"
      class="-z-10 absolute hidden md:block w-screen left-0 max-h-full overflow-hidden"
    >
      <img src="/src/assets/svg/pawprints.svg" />
    </div>

    <div id="intro-section" class="h-screen p-4">
      <h1
        class="font-solway font-bold text-3xl md:text-5xl md:leading-tight text-center"
      >
        <div>
          Find a cheap
          <br class="md:hidden" />
          electricity plan,
        </div>

        <div>
          <span class="border-b-4 border-blue-300 px-3 pb-1">
            headache-free</span
          >
        </div>
      </h1>

      <view-plans class="mx-auto mt-16 md:mt-20" />
    </div>

    <div id="faqs" class="px-6 pt-8 -mt-8 pb-12 md:pt-48 md:pb-64">
      <div class="w-full max-w-2xl mx-auto">
        <h2
          class="font-solway font-bold text-2xl md:text-3xl text-center mb-12"
        >
          <span class="border-b-4 border-blue-300 px-3 pb-1">FAQs</span>
        </h2>

        <faqs-item
          :is-open="openFaq === 'cost'"
          @toggle="openFaq !== 'cost' ? (openFaq = 'cost') : (openFaq = '')"
        >
          <template #question>
            How much does this website cost to use?
          </template>

          <template #answer>
            <p>
              Awesome Power is free to use and always will be. In the future, we
              may accept donations to cover server costs.
            </p>
          </template>
        </faqs-item>

        <faqs-item
          :is-open="openFaq === 'ptc'"
          @toggle="openFaq !== 'ptc' ? (openFaq = 'ptc') : (openFaq = '')"
        >
          <template #question>
            How is this different than Power To Choose?
          </template>

          <template #answer>
            <p>
              Power To Choose tells an incomplete story of plan pricing. Plans
              are ranked in order of their cost at exactly 1000 kWh; however,
              these results says nothing about the rest of the range of the
              plan. If you use just 1 kWh over (or under) 1000 kWh, you may pay
              twice as much as expected!
            </p>

            <p class="mt-4">
              Awesome Power solves this by using a weighted average to calculate
              plan costs. We take the average of a plan's cost across a range of
              kWh, so that misleading price jumps will be accounted for in the
              final pricing estimate.
            </p>
          </template>
        </faqs-item>

        <faqs-item
          :is-open="openFaq === 'calc'"
          @toggle="openFaq !== 'calc' ? (openFaq = 'calc') : (openFaq = '')"
        >
          <template #question>
            Can we see the calculations used in the results?
          </template>

          <template #answer>
            <p>
              Yep! Awesome Power is open source; check out the codebase
              <a
                href="https://github.com/awesomepowertexas/awesomepower"
                class="font-bold"
                target="_blank"
                >here</a
              >.
            </p>

            <p class="mt-4">
              Below are the distributions for each of the low, medium, and high
              usage profiles.
            </p>

            <div
              class="relative mt-6"
              style="padding-bottom: calc((398 / 760) * (11 / 12) * 100%)"
            >
              <img
                src="/src/assets/img/usage-weight.png"
                class="absolute w-11/12 md:rounded-lg md:shadow"
              />
            </div>

            <p class="mt-8">
              Basically, for each plan, we calculate the plan’s cost at every
              kWh from 1 to 5000, then multiply that cost by the weight (the
              number on the y-axis). We then sum up all of those weighted costs
              to get an expected cost for that usage profile.
            </p>
          </template>
        </faqs-item>

        <faqs-item
          :is-open="openFaq === 'missing'"
          @toggle="
            openFaq !== 'missing' ? (openFaq = 'missing') : (openFaq = '')
          "
        >
          <template #question>
            Why don’t the results include plan XYZ?
          </template>

          <template #answer>
            <p>
              The most challenging and time-consuming part of maintaining
              Awesome Power is collecting the complete pricing profile for every
              plan. Every night, we retrieve a list of all of the plans on Power
              To Choose. However, this list only tells us each plan’s cost at
              500, 1000, and 2000 kWh. In order for Awesome Power to work, we
              need to know the cost at every kWh, which you can only determine
              from the Electricity Facts Label (EFL) for that plan. The EFL does
              not have a standard format, so we try to figure out the different
              rates and charges by collecting all of the numbers visible on the
              EFL, and applying the numbers to one of the known cost functions
              for that provider. This process is entirely automated.
            </p>

            <p class="mt-4">
              We get the pricing profile for most of the plans this way, but
              many EFLs are tough to interpret, and we have no choice but to
              leave that plan off of the results.
            </p>
          </template>
        </faqs-item>

        <faqs-item
          :is-open="openFaq === 'old'"
          @toggle="openFaq !== 'old' ? (openFaq = 'old') : (openFaq = '')"
        >
          <template #question>
            What happened to the old Awesome Power website?
          </template>

          <template #answer>
            <p>
              In 2017, the creators of Awesome Power worked hard to improve
              consumer access to energy usage data by attending several meetings
              with the Public Utility Commission of Texas, and helping to
              determine the requirements for the state’s data access site, Smart
              Meter Texas.
            </p>

            <p class="mt-4">
              Finally, on December 7, 2019, SMT 2.0 was unveiled.
            </p>

            <p class="mt-4">
              Unfortunately, this meant that Awesome Power’s integration with
              Smart Meter Texas was broken. So, we simplified Awesome Power to
              only require a zip code to find the cheapest plans.
            </p>

            <p class="mt-4">
              If there's anything else that hasn't been answered in these FAQs,
              shoot me an email at michael@awesomepowertexas.com, and I'll try
              to get back to you.
            </p>
          </template>
        </faqs-item>
      </div>
    </div>
  </div>
</template>

<script>
import ViewPlans from '/src/components/Landing/ViewPlans.vue'
import FaqsItem from '/src/components/Landing/FaqsItem.vue'

export default {
  components: {
    ViewPlans,
    FaqsItem,
  },

  data: function () {
    return {
      openFaq: '',
    }
  },

  head: {
    title: 'Find a cheap electricity plan, headache free',
  },

  mounted() {
    this.checkHash()
  },

  methods: {
    async checkHash() {
      if (this.$route.hash === '#faqs') {
        await this.$nextTick()
        await this.$nextTick()
        document.getElementById('faqs').scrollIntoView({ behavior: 'smooth' })
      }
    },
  },
}
</script>

<style scoped lang="postcss">
#intro-section {
  padding-top: 16vh;
}

@screen md {
  #intro-section {
    padding-top: 20vh;
  }
}

#svg-pawprints-mobile {
  top: 65vh;
}

#svg-pawprints {
  padding-top: calc(80vh - 40vw);
}
</style>
