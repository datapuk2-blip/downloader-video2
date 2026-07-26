# DATA SP

DATA SP adalah Progressive Web App untuk mengelola data anggota serikat pekerja secara digital. Aplikasi dibuat mobile-first dengan React, Vite, TypeScript, TailwindCSS, React Router, Zustand, TanStack Query, React Hook Form, Zod, Chart.js, dan vite-plugin-pwa.

## Fitur

- Dashboard ringkasan total anggota, SP aktif, hampir habis, dan expired.
- Grafik anggota per seksi dan status masa berlaku SP.
- Data table anggota dengan detail, edit, hapus, export Excel/PDF, dan print.
- Form tambah/edit anggota dengan validasi wajib dan No Code unik.
- Pencarian realtime, filter status, dan sorting.
- Import Excel (.xlsx), laporan, dan pengaturan organisasi.
- Penyimpanan LocalStorage melalui helper `saveData`, `loadData`, `deleteData`, dan `updateData`.
- PWA installable dengan service worker auto-update, dukungan offline, manifest, splash/icon, dan caching.
- Dark mode tersimpan di LocalStorage.

## Menjalankan

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```
