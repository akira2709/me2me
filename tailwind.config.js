/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue, js,ts,jsx,tsx}",],
  theme: {
    extend: {},
    screens: {
      'desktop': '1100px',
      'small': {'max': '1100px'},
    },
  },
  plugins: [],
}

