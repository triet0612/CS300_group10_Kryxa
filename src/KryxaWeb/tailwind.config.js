/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        BlackOpsOne: ['"Black Ops One"'],
        NotoSans:['"Noto Serif"']
      },
      backgroundImage: {
        'login-bg': "url('$lib/assets/admin/login-bg.png')",
      }
    },
  },
  plugins: [],
}

