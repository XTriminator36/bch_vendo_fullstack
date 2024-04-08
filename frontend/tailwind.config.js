/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontSize: {
        '8xl': ['5.5rem', {
          lineHeight: '1',
        }],
        'xxs': '.55rem'
      },
      colors: {
        'lime': {
          '400': '#C7FF51',
          '300': '#C7FF51'
        }
      },
      height: {
        '100': '65rem',
      },
      width: {
        '46': '11.5rem',
      },
      boxShadow: {
        '3xl': '10px -18px 0px 0px rgba(0,0,0,1)',
        'rxl': '7px 4px 0px 1px rgb(249,67,67)',
      },
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
        oswald: ["Oswald", "sans-serif"],
        katibeh: ["Katibeh"],
        dela: ["Dela Gothic One"],
        josefin: ["Josefin Sans"],
        space: ["Space Grotesk"],
      },
    },
    
    borderRadius: {
      'none': '0',
      'sm': '0.125rem',
      DEFAULT: '4px',
      'md': '0.375rem',
      'lg': '0.5rem',
      'full': '9999px',
      'large': '12px',
      '2xl': '21px',
      '3xl': '51px',
    }
  },
  plugins: [],
}
