import defaultTheme from 'tailwindcss/defaultTheme';
import forms from '@tailwindcss/forms';

/** @type {import('tailwindcss').Config} */
export default {
    future: {
        hoverOnlyWhenSupported: true,
    },
    content: [
        './vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php',
        './storage/framework/views/*.php',
        './resources/views/**/*.blade.php',
        './resources/js/**/*.vue',
    ],

    theme: {
        extend: {
            fontFamily: {
                sans: ['Figtree', ...defaultTheme.fontFamily.sans],
            },
            colors: {
                noun: {
                    green: '#006600',
                    yellow: '#f2a900',
                    dark: '#004d00',
                    light: '#e6f2e6',
                    navy: '#0a1628',
                    'navy-light': '#112240',
                    gold: '#c9982a',
                    'gold-light': '#f0c860',
                    'yellow-light': '#f5c543',
                }
            },
            boxShadow: {
                'noun': '0 4px 14px 0 rgba(0, 102, 0, 0.15)',
            },
        },
    },

    plugins: [forms],
};
