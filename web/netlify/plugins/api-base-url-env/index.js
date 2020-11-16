module.exports = {
  onPreBuild: async ({ _inputs }) => {
    if (process.env.CONTEXT === 'deploy-preview') {
      process.env.VITE_API_BASE_URL = `https://awesomepower-pr-${process.env.REVIEW_ID}.herokuapp.com`
    }
  },
}
