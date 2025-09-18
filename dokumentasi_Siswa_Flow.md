# Dokumentasi Siswa: Rekomendasi AI LENTERAMU (Lengkap dengan Alur Flow)

## 1. Alur Flow Mendapatkan Rekomendasi AI

### Diagram Alur (Flow)

1. **Login Siswa**
   - Siswa login ke aplikasi/web LENTERAMU.
   - Sistem memuat profil siswa dan data aktivitas sebelumnya.
2. **Akses Fitur Belajar**
   - Siswa membuka menu "Fitur" untuk melihat materi, tugas, kuis.
   - Siswa memilih dan mengerjakan materi/tugas/kuis.
   - Setiap aktivitas tercatat otomatis (progress, nilai, waktu).
3. **Penyimpanan Aktivitas**
   - Sistem menyimpan log aktivitas (LearningActivity) dan progress (StudentProgress) ke database.
4. **AI Memproses Data**
   - Setelah ada aktivitas, AI (Q-learning + CBF) memproses data siswa.
   - Q-table diupdate setiap kali progress 100%.
5. **Akses Menu Rekomendasi AI**
   - Siswa klik menu "Fitur" → "Rekomendasi AI".
   - Sistem menampilkan rekomendasi personal (atau default jika data masih minim).

### Flowchart Sederhana

```
[Login Siswa] → [Akses Fitur Belajar] → [Aktivitas Tercatat] → [AI Proses Data] → [Siswa Akses Rekomendasi AI] → [Tampil Rekomendasi]
```

## 2. Cara Kerja AI Rekomendasi

### a. Data yang Diperlukan

- Profil siswa: gaya belajar, motivasi, engagement, dsb.
- Daftar materi/tugas/kuis: dari tabel Course.
- Aktivitas belajar: log aktivitas (LearningActivity) dan progress (StudentProgress).
- Nilai dan progress: hasil pengerjaan tugas/kuis/materi.

### b. Detail Q-learning: State, Action, Reward

- **State**: Kombinasi karakteristik siswa:
  - Gaya belajar (VARK): visual, auditory, kinesthetic, reading
  - Motivasi belajar (MSLQ): high, medium, low
  - Tipe motivasi (AMS): intrinsic, extrinsic, achievement, amotivation
  - Engagement: high, medium, low
  - Contoh state: ('visual', 'medium', 'intrinsic', 'medium')
- **Action**: ID Course (materi/tugas/kuis) yang aktif di sistem.
- **Reward**: +1 jika progress 100% pada course/action tersebut.
- **Q-table**: Skor preferensi untuk setiap (state, action), diupdate setiap kali siswa menyelesaikan materi/tugas/kuis.

### c. Detail Content-Based Filtering (CBF)

- CBF merekomendasikan materi/tugas/kuis berdasarkan kecocokan konten dengan minat siswa.
- Sistem mengecek field minat/topik siswa (interest/preferred_subjects).
- Jika ada, AI memprioritaskan course yang judul/deskripsinya mengandung kata kunci minat siswa.
- Jika tidak ada minat spesifik, semua course hasil Q-learning tetap ditampilkan.
- CBF berjalan setelah proses Q-learning, sehingga hasil akhirnya adalah kombinasi antara prioritas AI (Q-table) dan kecocokan minat/topik siswa.

### d. Proses AI (Q-learning + CBF)

1. Pengumpulan Data: Sistem mengumpulkan data aktivitas dan progress siswa.
2. Q-learning RL: AI membangun Q-table berdasarkan interaksi siswa dengan materi/tugas/kuis. Reward diberikan jika progress 100%.
3. Content-Based Filtering (CBF): AI juga mempertimbangkan minat/topik dari profil siswa.
4. Rekomendasi: AI memilih materi/tugas/kuis prioritas berdasarkan Q-table dan preferensi siswa.
5. Fallback: Jika data masih minim, sistem tetap menampilkan rekomendasi default.

### e. Update Otomatis

- Setiap kali siswa menyelesaikan materi/tugas/kuis, Q-table dan rekomendasi AI otomatis diperbarui.
- Tidak perlu intervensi admin/guru untuk menjalankan training AI.

## 3. Tips Agar Rekomendasi AI Muncul

- Login sebagai siswa (demo_student atau akun siswa lain).
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
