# Dokumentasi Siswa: Rekomendasi AI LENTERAMU

## 1. Alur Mendapatkan Rekomendasi AI

### a. Login Siswa

1. Buka aplikasi/web LENTERAMU.
2. Login menggunakan akun siswa (contoh: username `demo_student`, password `demo123`).
3. Setelah login, siswa akan diarahkan ke dashboard utama.

### b. Aktivitas Belajar

1. Siswa dapat mengakses menu "Fitur" untuk melihat daftar materi, tugas, dan kuis.
2. Siswa mengerjakan materi, tugas, atau kuis. Setiap aktivitas akan tercatat di sistem (progress, nilai, waktu belajar).
3. Progress dan aktivitas siswa akan otomatis tersimpan di database.

### c. Mendapatkan Rekomendasi AI

1. Klik menu "Fitur" → "Rekomendasi AI" (ikon lampu).
2. Halaman rekomendasi AI akan menampilkan saran belajar personal berdasarkan data aktivitas siswa.
3. Jika belum ada cukup aktivitas, sistem akan menampilkan rekomendasi default.
4. Setelah siswa aktif belajar (mengisi progress/nilai), rekomendasi AI akan semakin personal dan relevan.

## 2. Cara Kerja AI Rekomendasi

### e. Detail Content-Based Filtering (CBF)

- **CBF** adalah metode yang merekomendasikan materi/tugas/kuis berdasarkan kecocokan konten dengan minat atau preferensi siswa.
- Pada sistem ini, CBF bekerja dengan cara:
  - Mengecek apakah profil siswa memiliki field minat/topik tertentu (misal: `interest` atau `preferred_subjects`).
  - Jika ada, AI akan memprioritaskan course (materi/tugas/kuis) yang judul atau deskripsinya mengandung kata kunci minat siswa.
  - Jika tidak ada minat spesifik, semua course hasil Q-learning tetap ditampilkan.
- CBF berjalan setelah proses Q-learning, sehingga hasil akhirnya adalah kombinasi antara prioritas AI (Q-table) dan kecocokan minat/topik siswa.

Contoh:

- Jika siswa memiliki minat "matematika", maka course dengan judul/deskripsi mengandung "matematika" akan lebih diprioritaskan dalam rekomendasi.

### a. Data yang Diperlukan

- **Profil siswa**: gaya belajar, motivasi, engagement, dsb.
- **Daftar materi/tugas/kuis**: diambil dari tabel Course.
- **Aktivitas belajar**: log aktivitas (LearningActivity) dan progress (StudentProgress).
- **Nilai dan progress**: hasil pengerjaan tugas/kuis/materi.

### b. Detail Q-learning: State, Action, Reward

- **State**: Kombinasi karakteristik siswa, terdiri dari:

  - Gaya belajar (VARK): `visual`, `auditory`, `kinesthetic`, `reading`
  - Motivasi belajar (MSLQ): `high`, `medium`, `low`
  - Tipe motivasi (AMS): `intrinsic`, `extrinsic`, `achievement`, `amotivation`
  - Engagement: `high`, `medium`, `low`
  - Contoh state: `('visual', 'medium', 'intrinsic', 'medium')`

- **Action**: Pilihan materi/tugas/kuis yang tersedia untuk siswa.

  - Setiap action adalah ID dari Course (materi, tugas, kuis) yang aktif di sistem.
  - Contoh action: `3` (ID course untuk "Persamaan Linear"), `5` (ID tugas matematika), dst.

- **Reward**: Diberikan +1 jika siswa menyelesaikan (progress 100%) pada course/action tersebut.

- **Q-table**: Menyimpan skor preferensi untuk setiap kombinasi (state, action). Q-table diupdate setiap kali siswa menyelesaikan materi/tugas/kuis.

### c. Proses AI (Q-learning + CBF)

1. **Pengumpulan Data**: Sistem mengumpulkan data aktivitas dan progress siswa.
2. **Q-learning RL**: AI membangun Q-table berdasarkan interaksi siswa dengan materi/tugas/kuis. Reward diberikan jika progress 100%.
3. **Content-Based Filtering (CBF)**: AI juga mempertimbangkan minat/topik dari profil siswa.
4. **Rekomendasi**: AI memilih materi/tugas/kuis prioritas berdasarkan Q-table dan preferensi siswa.
5. **Fallback**: Jika data masih minim, sistem tetap menampilkan rekomendasi default agar siswa selalu mendapat saran.

### d. Update Otomatis

- Setiap kali siswa menyelesaikan materi/tugas/kuis, Q-table dan rekomendasi AI akan otomatis diperbarui.
- Tidak perlu intervensi admin/guru untuk menjalankan training AI.

## 3. Tips Agar Rekomendasi AI Muncul

- Pastikan login sebagai siswa (demo_student atau akun siswa lain).
- Lakukan aktivitas belajar: buka materi, kerjakan tugas/kuis, hingga progress bertambah.
- Semakin banyak aktivitas, rekomendasi AI akan semakin personal.
- Jika baru pertama login dan belum ada aktivitas, sistem akan menampilkan rekomendasi default.

## 4. Troubleshooting

- Jika rekomendasi AI tidak muncul:
  - Pastikan sudah login sebagai siswa.
  - Pastikan sudah ada data materi/tugas/kuis di sistem.
  - Lakukan minimal 1 aktivitas belajar.
  - Jika masih kosong, hubungi admin untuk pengecekan data demo.

---

**Catatan:**

- Semua proses AI berjalan otomatis di backend.
- Tidak perlu menjalankan training AI manual.
- Rekomendasi AI akan selalu muncul, baik personal maupun default.
