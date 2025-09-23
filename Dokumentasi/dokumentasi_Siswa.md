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

## 6. Struktur Database (ERD Sederhana)

```
[users] 1---1 [student_profiles] 1---* [student_progress] *---1 [courses] *---1 [subjects]
   |                                 |
   |                                 *---* [learning_activities]
   |                                 |
   *---* [ai_recommendations] -------*
```

- **users**: Data akun siswa/guru/admin.
- **student_profiles**: Profil detail siswa, relasi 1:1 ke users.
- **subjects**: Mata pelajaran.
- **courses**: Materi/tugas/kuis, relasi ke subjects.
- **student_progress**: Progress & nilai siswa per course.
- **learning_activities**: Log aktivitas belajar siswa per course.
- **ai_recommendations**: Q-table dan hasil rekomendasi AI per siswa per course.

> Semua tabel saling terhubung dan wajib ada agar AI berjalan otomatis dan rekomendasi personal bisa diberikan.

## 6. Tabel Database yang Diperlukan untuk AI Siswa

### 1. users

- id (PK)
- username
- email
- password_hash
- full_name
- role (siswa, guru, admin)
- is_active

### 2. student_profiles

- id (PK)
- user_id (FK ke users)
- student_id
- grade_level
- school_name
- learning_style (visual, auditory, kinesthetic, reading)
- learning_pace (slow, normal, fast)
- preferred_subjects (JSON/text, minat/topik)
- mslq_level (high, medium, low)
- ams_type (intrinsic, extrinsic, achievement, amotivation)
- engagement_level (high, medium, low)

### 3. subjects

- id (PK)
- name
- code
- description
- grade_level

### 4. courses

- id (PK)
- title
- description
- subject_id (FK ke subjects)
- difficulty_level (beginner, intermediate, advanced)
- content_type (video, article, quiz, practice)
- content_url
- duration_minutes
- is_active

### 5. learning_activities

- id (PK)
- user_id (FK ke users)
- course_id (FK ke courses)
- activity_type (view, complete, quiz_attempt, practice)
- start_time
- end_time
- score
- completed

### 6. student_progress

- id (PK)
- student_id (FK ke student_profiles)
- course_id (FK ke courses)
- progress_percentage
- last_accessed
- completion_date
- grade

### 7. ai_recommendations

- id (PK)
- user_id (FK ke users)
- course_id (FK ke courses)
- recommendation_type (content, difficulty, timing, sequence)
- match_score
- reasoning (state-action serialized)
- is_active

### Tabel & Field yang Diperlukan untuk Q-Learning

- **users**: id, role
- **student_profiles**: id, user_id, learning_style, mslq_level, ams_type, engagement_level
- **courses**: id, title, content_type, is_active
- **student_progress**: id, student_id, course_id, progress_percentage, grade
- **ai_recommendations**: id, user_id, course_id, recommendation_type, match_score, reasoning, is_active

### Tabel & Field yang Diperlukan untuk CBF (Content-Based Filtering)

- **student_profiles**: id, user_id, preferred_subjects (atau interest/minat)
- **courses**: id, title, description, content_type, is_active

> Q-Learning membutuhkan data karakteristik siswa, daftar course, progress, dan tabel rekomendasi AI (Q-table).
> CBF membutuhkan data minat/topik siswa dan metadata course (judul, deskripsi, tipe).

> Semua tabel di atas wajib ada dan terisi agar AI siswa (Q-learning + CBF) dapat berjalan otomatis dan optimal.

---

**Catatan:**

- Semua proses AI berjalan otomatis di backend.
- Tidak perlu menjalankan training AI manual.
- Rekomendasi AI akan selalu muncul, baik personal maupun default.
