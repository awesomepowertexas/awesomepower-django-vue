<script setup lang="ts">
import { useHead } from '@vueuse/head'

useHead({ title: 'Terms and Conditions' })
</script>

<template>
  <div class="pt-20 md:pt-48 px-4 pb-8 md:pb-20">
    <div class="w-full max-w-2xl mx-auto">
      <h1>Terms and Conditions</h1>

      <div class="w-10 md:w-20 h-1 bg-blue-300" />

      <p><i>Last updated: December 04, 2019</i></p>

      <p>
        These Terms and Conditions ("Terms", "Terms and Conditions") govern your
        relationship with https://awesomepowertexas.com website (the "Service")
        operated by Awesome Power ("us", "we", or "our").
      </p>

      <p>
        Please read these Terms and Conditions carefully before using the
        Service.
      </p>

      <p>
        Your access to and use of the Service is conditioned on your acceptance
        of and compliance with these Terms. These Terms apply to all visitors,
        users and others who access or use the Service.
      </p>

      <p>
        By accessing or using the Service you agree to be bound by these Terms.
        If you disagree with any part of the terms then you may not access the
        Service.
      </p>

      <h2>Links To Other Web Sites</h2>

      <p>
        Our Service may contain links to third-party web sites or services that
        are not owned or controlled by Awesome Power.
      </p>

      <p>
        Awesome Power has no control over, and assumes no responsibility for,
        the content, privacy policies, or practices of any third party web sites
        or services. You further acknowledge and agree that Awesome Power shall
        not be responsible or liable, directly or indirectly, for any damage or
        loss caused or alleged to be caused by or in connection with use of or
        reliance on any such content, goods or services available on or through
        any such web sites or services.
      </p>

      <p>
        We strongly advise you to read the terms and conditions and privacy
        policies of any third-party web sites or services that you visit.
      </p>

      <h2>Limitation Of Liability</h2>

      <p>
        In no event shall Awesome Power, nor its directors, employees, partners,
        agents, suppliers, or affiliates, be liable for any indirect,
        incidental, special, consequential or punitive damages, including
        without limitation, loss of profits, data, use, goodwill, or other
        intangible losses, resulting from (i) your access to or use of or
        inability to access or use the Service; (ii) any conduct or content of
        any third party on the Service; (iii) any content obtained from the
        Service; and (iv) unauthorized access, use or alteration of your
        transmissions or content, whether based on warranty, contract, tort
        (including negligence) or any other legal theory, whether or not we have
        been informed of the possibility of such damage, and even if a remedy
        set forth herein is found to have failed of its essential purpose.
      </p>

      <h2>Disclaimer</h2>

      <p>
        Your use of the Service is at your sole risk. The Service is provided on
        an "AS IS" and "AS AVAILABLE" basis. The Service is provided without
        warranties of any kind, whether express or implied, including, but not
        limited to, implied warranties of merchantability, fitness for a
        particular purpose, non-infringement or course of performance.
      </p>

      <p>
        Awesome Power its subsidiaries, affiliates, and its licensors do not
        warrant that a) the Service will function uninterrupted, secure or
        available at any particular time or location; b) any errors or defects
        will be corrected; c) the Service is free of viruses or other harmful
        components; or d) the results of using the Service will meet your
        requirements.
      </p>

      <p>
        The price you pay for an electricity plan might be different from the
        expected price shown. We do not guarantee the accuracy of information on
        this website. By using this website, you agree to indemnify and hold
        harmless Awesome Power, its owners, and its employees from any damages
        caused as a result of the information and services you obtain from this
        website.
      </p>

      <h2>Governing Law</h2>

      <p>
        These Terms shall be governed and construed in accordance with the laws
        of United States, without regard to its conflict of law provisions.
      </p>

      <p>
        Our failure to enforce any right or provision of these Terms will not be
        considered a waiver of those rights. If any provision of these Terms is
        held to be invalid or unenforceable by a court, the remaining provisions
        of these Terms will remain in effect. These Terms constitute the entire
        agreement between us regarding our Service, and supersede and replace
        any prior agreements we might have between us regarding the Service.
      </p>

      <h2>Changes</h2>

      <p>
        We reserve the right, at our sole discretion, to modify or replace these
        Terms at any time. If a revision is material we will try to provide at
        least 30 days notice prior to any new terms taking effect. What
        constitutes a material change will be determined at our sole discretion.
      </p>

      <p>
        By continuing to access or use our Service after those revisions become
        effective, you agree to be bound by the revised terms. If you do not
        agree to the new terms, please stop using the Service.
      </p>

      <h2>Contact Us</h2>
      <p>
        If you have any questions about this Privacy Policy, please contact us:
      </p>
      <ul>
        <li>By email: michael@awesomepowertexas.com</li>
      </ul>
    </div>
  </div>
</template>

<style scoped lang="postcss">
p,
li {
  @apply text-sm leading-loose md:text-base md:leading-loose text-gray-700;
}

p {
  @apply mt-4;
}

li {
  @apply mt-2 ml-10;
}

li > p {
  @apply mt-0;
}

li:before {
  @apply block relative;
  content: url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOCIgaGVpZ2h0PSI4IiB2aWV3Qm94PSIwIDAgOCA4IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8Y2lyY2xlIGN4PSI0IiBjeT0iNCIgcj0iNCIgZmlsbD0iIzQyOTlFMSIvPgo8L3N2Zz4K');
  max-height: 0;
  max-width: 0;
  left: -20px;
  top: -2px;
}

h1 {
  @apply font-solway font-bold text-2xl md:text-4xl;
}

h2 {
  @apply font-solway font-bold text-xl md:text-3xl mt-8 md:mt-12;
}

h3 {
  @apply font-solway font-bold text-lg md:text-xl mt-6;
}

h4 {
  @apply font-bold text-sm text-gray-700 uppercase tracking-widest mt-6;
}
</style>
