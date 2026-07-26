import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  plugins: [react(), tailwindcss(), VitePWA({registerType:'autoUpdate',includeAssets:['pwa-192.svg','pwa-512.svg','apple-touch-icon.svg'],manifest:{name:'DATA SP - Data Anggota Serikat Pekerja',short_name:'DATA SP',description:'Aplikasi pengelolaan data anggota serikat pekerja',theme_color:'#0D47A1',background_color:'#F5F7FA',display:'standalone',orientation:'portrait',scope:'/',start_url:'/',icons:[{src:'/pwa-192.svg',sizes:'192x192',type:'image/svg+xml',purpose:'any maskable'},{src:'/pwa-512.svg',sizes:'512x512',type:'image/svg+xml',purpose:'any maskable'}]},workbox:{globPatterns:['**/*.{js,css,html,ico,png,svg,woff2}'],runtimeCaching:[{urlPattern:/^https:\/\/fonts\./,handler:'CacheFirst',options:{cacheName:'font-cache'}}],cleanupOutdatedCaches:true,clientsClaim:true,skipWaiting:true}})],
});
