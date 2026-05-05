import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

import cloudflare from '@astrojs/cloudflare';

export default defineConfig({
  site: 'https://usolutions-wiki.gr',
  output: 'static',

  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [sitemap()],

  i18n: {
    defaultLocale: 'el',
    locales: ['el', 'en'],
    routing: {
      prefixDefaultLocale: false,
    }
  },

  adapter: cloudflare()
});