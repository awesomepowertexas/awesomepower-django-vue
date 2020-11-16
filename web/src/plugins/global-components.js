import AppButton from '/src/components/_global/AppButton.vue'
import FontAwesomeIcon from '/src/components/_global/FontAwesomeIcon.vue'
import LoadingSpinner from '/src/components/_global/LoadingSpinner.vue'
import TransitionExpand from '/src/components/_global/TransitionExpand.vue'

function registerGlobalComponents(app) {
  app.component('AppButton', AppButton)
  app.component('FontAwesomeIcon', FontAwesomeIcon)
  app.component('LoadingSpinner', LoadingSpinner)
  app.component('TransitionExpand', TransitionExpand)
}

export default registerGlobalComponents
