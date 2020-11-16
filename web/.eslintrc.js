module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
    'prettier',
    'prettier/vue',
  ],
  rules: {
    camelcase: 'off',
    'no-unused-vars': [
      'error',
      { argsIgnorePattern: '^_', varsIgnorePattern: '^_' },
    ],
    'vue/html-self-closing': ['error', { html: { void: 'any' } }],
    'vue/require-default-prop': 'off',
  },
}
