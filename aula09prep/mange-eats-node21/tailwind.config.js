/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        mange: {
          red: '#b91c1c',
          dark: '#171717',
          orange: '#f97316',
          cream: '#fff7ed'
        }
      },
      boxShadow: {
        soft: '0 12px 30px rgba(0,0,0,.08)'
      }
    },
  },
  plugins: [],
}
