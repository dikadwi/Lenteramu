Perubahan tampilan `base_siswa` dan `dashboard_siswa` (ringkas)

Tujuan:

- Membuat tampilan lebih dinamis dan mencegah error ketika data tidak lengkap.
- Menyediakan fallback dan state kosong agar UI tetap rapi.

Perubahan utama:

- `templates/siswa/base_siswa.html`

  - Menambahkan default nilai untuk variabel umum (`user`, `learning_progress`, `material_progress`, `pending_tasks`, `new_achievements`) agar template tidak error bila data tidak tersedia.
  - Menambahkan fungsi JavaScript ringan (stubs) untuk dropdowns, AI assistant, dan toast agar elemen interaktif tidak menyebabkan error di konsol.

- `templates/siswa/dashboard_siswa.html`
  - Menambahkan default untuk `subjects`, `upcoming_exams`, `notifications`, `progress`, dan variabel lainnya.
  - Menambahkan pesan "empty state" ketika tidak ada data (mata pelajaran, ujian, notifikasi).
  - Mengubah fallback avatar untuk menggunakan `url_for('static', ... )`.

Verifikasi singkat:

- Menjalankan pemeriksaan sintaks Jinja2 (`tools/check_templates.py`) berhasil mem-parse kedua template tanpa error.

Saran tindak lanjut (opsional):

- Pindahkan CSS besar di `dashboard_siswa.html` ke file `static/css/siswa/dashboard.css` untuk pemisahan concerns dan caching.
- Hubungkan fungsi JS stubs (`followRecommendation`, `markAllRead`) ke endpoint API untuk behaviour penuh.
- Tambahkan unit test render template menggunakan Flask test_request_context untuk verifikasi variabel `url_for` dan `request`.

Jika Anda ingin, saya bisa: memindahkan CSS ke file statis, menambahkan contoh API endpoint untuk notifikasi, dan menulis 1-2 unit test untuk render dashboard.
