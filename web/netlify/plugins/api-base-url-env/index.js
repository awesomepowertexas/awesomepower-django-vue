module.exports = {
  onPreBuild: async ({ inputs }) => {
    if (process.env.CONTEXT === 'deploy-preview') {
      process.env.API_BASE_URL = `https://awesomepower-pr-${process.env.REVIEW_ID}.herokuapp.com`
    }
  },
}
