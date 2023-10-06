/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./**/*.{html,js}"],
  presets: [],
  theme: {
    extend: {
      spacing: {
        'some key': {
          1.5: '<something>',
        },
      },
    },
  },
  plugins: [],
}