module.exports = {
  theme: {
    colors: {
      transparent: 'transparent',

      black: 'hsl(0, 0%, 0%)',
      white: 'hsl(0, 0%, 100%)',

      gray: {
        100: 'hsl(214, 45%, 98%)',
        200: 'hsl(214, 38%, 95%)',
        300: 'hsl(214, 32%, 91%)',
        400: 'hsl(214, 25%, 84%)',
        500: 'hsl(214, 20%, 69%)',
        600: 'hsl(214, 15%, 52%)',
        700: 'hsl(214, 17%, 35%)',
        800: 'hsl(214, 23%, 23%)',
        900: 'hsl(214, 26%, 14%)',
      },
      red: {
        100: 'hsl(0, 100%, 98%)',
        300: 'hsl(0, 97%, 85%)',
        500: 'hsl(0, 88%, 68%)',
        600: 'hsl(0, 76%, 57%)',
      },
      orange: {
        500: 'hsl(27, 84%, 57%)',
      },
      green: {
        100: 'hsl(145, 100%, 97%)',
        500: 'hsl(145, 46%, 51%)',
        600: 'hsl(145, 48%, 43%)',
      },
      blue: {
        100: 'hsl(207, 90%, 96%)',
        300: 'hsl(207, 82%, 76%)',
        500: 'hsl(207, 73%, 57%)',
        600: 'hsl(207, 62%, 50%)',
        700: 'hsl(207, 61%, 43%)',
        800: 'hsl(213, 49%, 34%)',
        900: 'hsl(207, 41%, 28%)',
      },
    },
    boxShadow: {
      DEFAULT: '0 2px 6px 0 rgba(0, 0, 0, 0.25), 0 0 2px 0 rgba(0, 0, 0, 0.1)',
    },
    fontFamily: {
      'open-sans': ["'Open Sans'", 'sans-serif'],
      solway: ['"Solway"', 'serif'],
    },
    extend: {
      borderRadius: {
        xl: '0.75rem',
      },
      spacing: {
        '2px': '2px',
        '3px': '3px',
        14: '3.5rem',
        80: '20rem',
        96: '24rem',
        112: '28rem',
        128: '32rem',
      },
    },
  },
  variants: {},
  plugins: [],
  purge: {
    content: ['./index.html', './src/**/*.vue', './src/**/*.js'],
  },
}
