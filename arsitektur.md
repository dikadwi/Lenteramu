57

1. Lapisan Pengumpulan Data (Data Collection Layer)
   a) Komponen

1) Data Warehouse
2) Sistem Eksternal (LMS, SIS, platform e-learning)
3) Antarmuka Pengguna
   b) Aliran Data
   Data dari sistem eksternal dan antarmuka pengguna
   dikumpulkan dan disimpan di Data Warehouse. Antarmuka
   Pengguna juga memungkinkan input data langsung dari
   siswa, guru, dan administrator.

Garis panah menggambarkan aliran data dari antarmuka pengguna
dan sistem eksternal ke Data Warehouse.

Gambar 2.5. 1 Arsitektur Lapisan Pengumpulan Data

2. Lapisan Pemrosesan dan Analisis (Processing and Analytics
   Layer)
   a) Komponen:

1) Modul Analisis Data Siswa
2) Sistem Pemantauan Kinerja
   b) Aliran Data
   Data dari Data Warehouse diambil oleh “Modul Analisis Data
   Siswa” untuk dianalisis lebih lanjut. Hasil analisis ini dikirim

58
ke Sistem Pemantauan dan Penilaian Kinerja untuk
pemantauan dan penilaian.

“Modul Analisis Data Siswa” dan Sistem Pemantauan dan Penilaian  
Kinerja dihubungkan dengan Data Warehouse melalui panah dua
arah yang menunjukkan aliran data masuk dan keluar.

Gambar 2.5. 2 Arsitektur Lapisan Pemrosesan dan Analisis

3. Lapisan Layanan AI dan Personalisasi (AI Services and
   Personalization Layer)
   a) Komponen:

1) Modul Personalisasi Konten
2) Modul Umpan Balik Adaptif
   b) Aliran Data
   Hasil analisis dari “Modul Analisis Data Siswa” diteruskan ke
   “Modul Personalisasi Konten” dan “Modul Umpan Balik
   Adaptif”. “Modul Personalisasi Konten” menghasilkan
   rekomendasi yang dikirim kembali ke antarmuka pengguna,
   sementara “Modul Umpan Balik Adaptif” menghasilkan
   umpan balik dinamis berdasarkan kinerja siswa.

59
Modul-modul ini terhubung dengan Sistem Pemantauan dan
Penilaian Kinerja dan “Modul Analisis Data Siswa”, menunjukkan
aliran data dan rekomendasi yang berkelanjutan.

Gambar 2.5. 3 Arsitektur Lapisan Layanan AI dan Personalisasi

4. Lapisan Antarmuka Pengguna (User Interface Layer)
   a) Komponen:

1) Dashboard Siswa
2) Dashboard Guru dan Administrator
   b) Aliran Data
   Data dan rekomendasi yang dihasilkan oleh berbagai modul
   AI dan analitik dikirimkan ke antarmuka pengguna melalui
   API. Siswa, guru, dan administrator dapat mengakses data
   dan laporan melalui dashboard masing-masing.

Dashboard Siswa dan Dashboard Guru dihubungkan dengan Layanan
AI (modul AI dan analitik) dan “Modul Pembuatan Laporan”,
menunjukkan penyampaian informasi yang berkelanjutan dan
interaktif.

60
Gambar 2.5. 4 Arsitektur Lapisan Antarmuka Pengguna

5. Lapisan Integrasi dan Keamanan (Integration and Security
   Layer)
   a) Komponen:

1) API dan Web Services
2) Komponen Keamanan dan Privasi
   b) Aliran Data
   API dan Web Services memungkinkan komunikasi antara
   sistem cerdas dengan sistem eksternal. Komponen
   Keamanan dan Privasi memastikan bahwa semua aliran data
   antar komponen aman dan sesuai dengan standar
   perlindungan data.

61
c) API dan Web Services terhubung dengan semua komponen
lain dalam sistem, menunjukkan integrasi yang mendalam.
Komponen Keamanan dan Privasi berada di sekitar diagram
untuk menunjukkan perlindungan di setiap lapisan.
Gambar 2.5. 5 Arsitektur Lapisan Integrasi dan Keamanan 6. Lapisan Laporan dan Visualisasi (Reporting and Visualization
Layer)
a) Komponen:
• “Modul Pembuatan Laporan dan Analisis Visual”
b) Aliran Data
Modul ini menerima data dari Sistem Pemantauan dan
Penilaian Kinerja dan mengubahnya menjadi laporan visual
yang dapat dipahami oleh guru dan administrator.
c) Modul ini terhubung dengan Sistem Pemantauan dan
Penilaian Kinerja melalui panah dua arah yang menunjukkan
pengambilan dan pengolahan data untuk pembuatan
laporan.

62

Gambar 2.5. 6 Arsitektur Lapisan Laporan dan Visualisasi

Gambar 2.5.7 menyajikan arsitektur utuh sistem yang merupakan
representasi dari gabungan setiap lapisan.

Gambar 2.5. 7 Arsitektur Utuh LENTERAMU

63

Diagram ini mengilustrasikan secara utuh bagaimana komponen-
komponen dan modul-modul utama dalam sistem bekerja secara
sinergis untuk mencapai tujuan utama sistem—menciptakan
pengalaman belajar yang lebih personal dan efektif. Dengan
menggunakan diagram arsitektur ini, pengembang, guru, dan
pemangku kepentingan lainnya dapat dengan mudah memahami
struktur sistem, aliran data, dan cara komponen-komponen utama
berkolaborasi untuk menyediakan layanan personalisasi
pembelajaran yang berbasis data dan berfokus pada siswa
