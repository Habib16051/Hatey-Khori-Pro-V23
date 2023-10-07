/** @type {import('tailwindcss').Config} */

// module.exports = {
//   content: ["./**/*.{html,js}"],
//   theme: {
//     extend: {
//       spacing: {
//         'some key': {
//           1.5: '<something>',
//         },
//       },
//     },
//   },
//   plugins: [],
// }


module.exports = {
  content: ["./**/*.{html, js}"],

  theme: {
    screen: {
      sm: "576px",
      md: "768px",
      lg: "992px",
      xl: "1200px",
    },
    container: {
      center: true,
      padding: "1rem",
    },
    extend: {
      spacing: {
        'some key': {
          1.5: '<something>',
        },
      },

      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
        roboto: ["Roboto", "sans-serif"],
      },
      colors: {
        primary: "#fd3d57",
      },
    },
  },
  plugins: [],
};