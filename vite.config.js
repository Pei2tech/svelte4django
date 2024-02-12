import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import path from "path";
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const _filename = fileURLToPath(import.meta.url);
const _dirname = dirname(_filename);

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  build: {
    // below for main.js
    outDir: path.join(_dirname, "mysite/statics/assets"),
    rollupOptions: {
      output: {
        entryFileNames: `[name].js`,
        chunkFileNames: `[name].js`,
        assetFileNames: `[name].[ext]`,
      },
      input: path.resolve(_dirname, "src", "main.js"),
      // external: [
      // ],
    },
  },
})


