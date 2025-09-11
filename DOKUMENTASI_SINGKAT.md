# 📖 Dokumentasi Lengkap Aplikasi LENTERAMU

---

## 1. Tentang LENTERAMU

**LENTERAMU** adalah aplikasi pembelajaran digital berbasis web yang mengintegrasikan teknologi AI untuk mendukung proses belajar-mengajar di sekolah. Platform ini menyediakan dashboard dinamis untuk siswa, guru, dan admin, serta fitur manajemen kelas, tugas, analitik, dan rekomendasi pembelajaran yang adaptif.

---

## 2. Struktur Menu & Navigasi

### 2.1. Menu Utama

| Menu        | Siswa | Guru | Admin | Penjelasan                                                            |
| ----------- | ----- | ---- | ----- | --------------------------------------------------------------------- |
| Dashboard   | ✔     | ✔    | ✔     | Tampilan utama berisi ringkasan aktivitas, statistik, dan notifikasi. |
| Kelas       | ✔     | ✔    | ✔     | Daftar kelas yang diikuti/dikelola, detail anggota dan materi.        |
| Tugas       | ✔     | ✔    | ✔     | Daftar tugas yang harus dikerjakan/dibuat/dinilai.                    |
| Analitik    | ✔     | ✔    | ✔     | Grafik performa, progress belajar, dan insight AI.                    |
| AI Insights | ✔     | ✔    | ✔     | Rekomendasi materi/tugas dari sistem AI berdasarkan data pengguna.    |
| Notifikasi  | ✔     | ✔    | ✔     | Informasi terbaru terkait kelas, tugas, dan sistem.                   |
| Pengaturan  | -     | ✔    | ✔     | Pengaturan akun, preferensi, dan sistem.                              |
| Bantuan     | ✔     | ✔    | ✔     | FAQ, kontak admin, dan panduan penggunaan aplikasi.                   |

---

## 3. Penjelasan Menu & Fitur

### 3.1. Dashboard

- **Fungsi:**  
  Menampilkan ringkasan aktivitas, statistik utama (jumlah kelas, tugas, progress), dan notifikasi terbaru.
- **Fitur:**
  - Statistik dinamis (jumlah tugas, kelas, nilai rata-rata)
  - Quick actions (Aksi cepat: mulai tugas, lihat kelas, buat tugas)
  - Notifikasi real-time

### 3.2. Kelas

- **Fungsi:**  
  Mengelola dan melihat daftar kelas yang diikuti/dikelola.
- **Fitur:**
  - Daftar kelas aktif
  - Detail anggota kelas (siswa/guru)
  - Materi dan jadwal kelas
  - Aksi: gabung kelas, kelola kelas, lihat materi

### 3.3. Tugas

- **Fungsi:**  
  Manajemen tugas untuk siswa (mengerjakan), guru (membuat/menilai), dan admin (monitoring).
- **Fitur:**
  - Daftar tugas terbaru dan status pengerjaan
  - Progress tugas (sudah/dalam proses/belum)
  - Upload jawaban dan penilaian otomatis/manual
  - Reminder deadline

### 3.4. Analitik

- **Fungsi:**  
  Menyajikan data performa belajar, progress, dan insight AI.
- **Fitur:**
  - Grafik nilai dan progress belajar
  - Statistik kehadiran dan penyelesaian tugas
  - Insight AI: rekomendasi materi/tugas berikutnya

### 3.5. AI Insights

- **Fungsi:**  
  Memberikan rekomendasi pembelajaran berbasis AI sesuai kebutuhan pengguna.
- **Fitur:**
  - Saran materi/tugas yang relevan
  - Deteksi siswa yang butuh bantuan
  - Analisis pola belajar

### 3.6. Notifikasi

- **Fungsi:**  
  Menyampaikan informasi terbaru terkait aktivitas pengguna.
- **Fitur:**
  - Notifikasi tugas baru, nilai, pengumuman kelas
  - Sistem toast notification interaktif
  - Penanda notifikasi belum dibaca

### 3.7. Pengaturan

- **Fungsi:**  
  Mengelola preferensi akun dan sistem (khusus guru/admin).
- **Fitur:**
  - Edit profil dan password
  - Pengaturan notifikasi
  - Manajemen user (admin)

### 3.8. Bantuan

- **Fungsi:**  
  Memberikan panduan dan solusi masalah penggunaan aplikasi.
- **Fitur:**
  - FAQ
  - Kontak admin/support
  - Tutorial penggunaan

---

## 4. Fitur Khusus & Teknologi

- **Landing Page Modern:**  
  Tampilan awal profesional, responsif, dan informatif.
- **Autentikasi Multi-Role:**  
  Login dengan role Siswa, Guru, Admin.
- **Dashboard Dinamis:**  
  Statistik, notifikasi, progress, dan aksi cepat sesuai role.
- **Manajemen Kelas & Tugas:**  
  Guru dapat mengelola kelas, membuat tugas, dan menilai.
- **Analitik Performa:**  
  Grafik performa siswa, AI insights, dan laporan otomatis.
- **Notifikasi Real-Time:**  
  Sistem notifikasi interaktif untuk semua user.
- **Footer & Header Modern:**  
  Navigasi dan informasi aplikasi di bagian atas dan bawah.
- **Responsive Design:**  
  Tampilan optimal di desktop dan mobile.

---

## 5. Alur Pengguna

### Siswa

1. Login
2. Melihat dashboard (statistik, tugas, kelas)
3. Mengerjakan tugas
4. Melihat analitik dan rekomendasi AI
5. Menerima notifikasi

### Guru

1. Login
2. Melihat dashboard (kelas, tugas, analitik)
3. Membuat dan menilai tugas
4. Melihat insight AI untuk siswa
5. Mengelola kelas dan materi

### Admin

1. Login
2. Monitoring aktivitas seluruh user
3. Manajemen user dan sistem
4. Melihat laporan dan statistik global

---

## 6. Teknologi & Integrasi

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript, Jinja2
- **Database:** MySQL (opsional)
- **Library:** FontAwesome, Chart.js
- **AI Engine:** Rekomendasi berbasis data progress siswa

---

## 7. Instalasi & Setup

1. **Clone Repository**
   ```
   git clone https://github.com/username/lenteramu.git
   cd lenteramu
   ```
2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Jalankan Aplikasi**
   ```
   python app.py
   ```
   Akses di `http://127.0.0.1:5000/`

---

## 8. Struktur Folder

```
Lenteramu/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── landing.html
│   ├── login.html
│   ├── workflows/
│   │   ├── student_workflow.html
│   │   ├── teacher_workflow.html
│   │   └── admin_workflow.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js
│   │   └── dynamic-dashboard.js
│   └── images/
├── README.md
└── DOKUMENTASI_APLIKASI.md
```

---

## 9. API Endpoint (Contoh)

| Endpoint                    | Method | Deskripsi               |
| --------------------------- | ------ | ----------------------- |
| `/api/dashboard/<role>`     | GET    | Data dashboard per role |
| `/api/notifications/<role>` | GET    | Notifikasi terbaru      |
| `/api/classes`              | GET    | Data kelas              |
| `/api/assignments`          | GET    | Data tugas              |

---

## 10. Troubleshooting

- **Tampilan tertutup:**  
  Pastikan CSS `.container` tidak menimpa header/footer.
- **Login tidak bisa:**  
  Cek route dan session Flask.
- **Data tidak muncul:**  
  Pastikan variabel dikirim dari backend ke template.

---

## 11. Kontak & Bantuan

- Email: support@lenteramu.com
- Telegram: @lenteramu_support

---

## 12. Credits

Tim Pengembang LENTERAMU  
Kontributor open source

---

\*\*Dokumentasi ini menggambarkan seluruh menu, fungsi, dan fitur aplikasi LENTERAMU secara lengkap
