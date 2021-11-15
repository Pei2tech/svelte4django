import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import path from "path";
import glob from "glob";
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: path.join(__dirname,"mysite/statics"),
    rollupOptions: {
      input: glob.sync(path.resolve(__dirname,"index.html")),
      // external: [
      //   "",
      // ],
    },
  },
})
