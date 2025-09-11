242
▪ Menggunakan algoritma seperti Collaborative
Filtering untuk rekomendasi konten, Reinforcement
Learning untuk umpan balik adaptif, dan Supervised
Learning untuk klasifikasi performa siswa.
▪ Melakukan eksperimen dengan berbagai
hyperparameter untuk mengoptimalkan performa
model.
▪ Menggunakan teknik Cross-Validation untuk
memastikan model tidak overfitting pada data
pelatihan. 4) Validasi dan Evaluasi Model (Model Validation and
Evaluation)
Setelah model dilatih, model tersebut divalidasi dan
dievaluasi menggunakan data uji yang terpisah untuk
mengukur kinerja dan generalisasi model. Tahap ini
memastikan bahwa model berfungsi dengan baik pada data
baru yang tidak terlihat selama pelatihan. Aktivitas-aktivitas
dari Validasi dan Evaluasi adalah sebagai berikut:
▪ Menggunakan metrik evaluasi seperti Accuracy,
Precision, Recall, F1-Score, RMSE (Root Mean
Squared Error), dan AUC-ROC untuk menilai
performa model.
▪ Melakukan analisis error untuk mengidentifikasi area
di mana model mungkin tidak berfungsi dengan baik.
▪ Menggunakan teknik Model Tuning untuk
memperbaiki kelemahan yang teridentifikasi selama
evaluasi. 5) Implementasi dan Integrasi Model (Model Deployment and
Integration)
Model AI yang telah divalidasi kemudian diimplementasikan
dalam lingkungan produksi dan diintegrasikan dengan sistem
aplikasi cerdas. Model ini digunakan secara langsung untuk
memberikan rekomendasi, umpan balik, dan analisis

243
performa siswa. Aktivitas-aktivitas dari Implementasi dan
Integrasi Model adalah sebagai berikut:
▪ Menggunakan containerization (misalnya, Docker)
untuk menyebarkan model di lingkungan produksi.
▪ Mengatur pipeline integrasi (CI/CD) untuk
pembaruan model yang cepat dan otomatis.
▪ Mengintegrasikan model dengan antarmuka
pengguna melalui API untuk interaksi waktu nyata. 6) Monitoring dan Pembaruan Model (Model Monitoring and
Retraining)
Setelah model diimplementasikan, kinerjanya dipantau
secara berkelanjutan untuk memastikan model tetap relevan
dan akurat. Model diperbarui atau dilatih ulang secara
berkala untuk menangani perubahan data dan dinamika
pengguna. Aktivitas-aktivitas dari Monitoring dan
Pembaruan Model adalah sebagai berikut:
▪ Menggunakan alat monitoring seperti Prometheus
dan Grafana untuk memantau performa model
secara real-time.
▪ Mengidentifikasi Concept Drift jika terjadi
perubahan pola data dan melakukan retraining
model secara otomatis. 2. Manfaat Alur Proses Pembelajaran AI
Pada bagian ini membahas berbagai manfaat dari alur proses
pembelajaran AI, termasuk peningkatan kemampuan adaptasi
sistem, pengoptimalan keputusan berbasis data, serta inovasi dalam
produk dan layanan. Dengan memahami manfaat ini, diharapkan
dapat melihat potensi besar yang dimiliki AI dalam transformasi
proses pembelajaran dan penerapannya di dunia nyata.

1. Pengembangan Model yang Lebih Efisien
   Dengan mengikuti alur proses yang terstruktur, pengembang
   dapat dengan mudah mengikuti langkah-langkah yang

244
diperlukan untuk membangun model AI yang efektif dan
relevan. 2) Pengambilan Keputusan Berbasis Data yang Lebih Baik
Model AI yang dioptimalkan dapat memberikan wawasan
yang lebih akurat tentang perilaku dan kebutuhan siswa,
memungkinkan personalisasi yang lebih baik. 3) Penggunaan Sumber Daya yang Optimal
Alur ini memastikan penggunaan sumber daya komputasi
yang optimal untuk pelatihan dan validasi model,
menghindari pemborosan dan biaya yang tidak perlu. 4) Peningkatan Pengalaman Pengguna
Dengan mengimplementasikan model AI yang kuat,
pengalaman pengguna (siswa dan guru) di dalam sistem
menjadi lebih dinamis, responsif, dan relevan.

Gambar 6.3 1 Alur Proses Pembelajaran AI

245

Gambar di atas merupakan Flow Chart yang lebih jelas mengenai Alur
Proses Pembelajaran AI dalam LENTERAMU. Flow chart ini
menggambarkan tahapan-tahapan mulai dari pengumpulan data,
praproses data, pelatihan model, validasi dan evaluasi model,
implementasi model, hingga pemantauan dan pembaruan model. Ini
memperlihatkan aliran dari satu tahap ke tahap berikutnya dengan
jelas, yang menunjukkan bagaimana setiap proses saling terhubung
dalam sistem pembelajaran AI yang adaptif.

6.4 Diagram Alur Umpan Balik dan Penilaian
Diagram Alur Umpan Balik dan Penilaian dalam LENTERAMU
menggambarkan proses bagaimana sistem memberikan umpan balik
adaptif kepada siswa berdasarkan hasil evaluasi dan interaksi mereka
dengan konten pembelajaran. Diagram ini menunjukkan aliran data
dan proses mulai dari pengumpulan hasil evaluasi, analisis performa
siswa, hingga pemberian umpan balik yang disesuaikan. Diagram ini
penting untuk memvisualisasikan bagaimana sistem menggunakan
data dan algoritma untuk meningkatkan pengalaman belajar siswa
secara individual.

1. Tahapan Utama dalam Alur Umpan Balik dan Penilaian
   Alur proses umpan balik dan penilaian terdiri dari beberapa tahapan
   penting yang memastikan bahwa umpan balik yang diberikan
   relevan, adaptif, dan bermanfaat bagi perkembangan siswa. Berikut
   adalah tahapan-tahapan utama dalam diagram:

1) Pengumpulan Data Hasil Evaluasi (Assessment Data
   Collection)
   Pada tahap ini melibatkan pengumpulan hasil evaluasi siswa,
   seperti nilai kuis, tes, waktu penyelesaian, dan pola jawaban.
   Data ini dikumpulkan secara otomatis dari modul evaluasi
   dan disimpan dalam database sistem. Aktivitas-aktivitas
   Pengumulan Data Hasil Evaluasi adalah sebagai berikut:

246
▪ Merekam hasil setiap evaluasi atau kuis yang
dilakukan oleh siswa.
▪ Menyimpan informasi tambahan seperti waktu
pengerjaan, jumlah percobaan, dan tingkat kesulitan
soal. 2) Analisis Performa Siswa (Student Performance Analysis)
Setelah data evaluasi dikumpulkan, sistem melakukan
analisis performa siswa untuk mengidentifikasi kekuatan dan
kelemahan mereka. Analisis ini menggunakan algoritma
pembelajaran mesin dan analisis statistik untuk
menghasilkan wawasan yang lebih mendalam. Aktivitas-
aktivitas Analisis Performa Siswa adalah sebagai berikut:
▪ Menggunakan algoritma klasifikasi (seperti Decision
Tree, kNN) untuk mengelompokkan siswa
berdasarkan kinerja.
▪ Menggunakan analisis deskriptif dan statistik untuk
memahami pola kesalahan siswa dan waktu
pengerjaan. 3) Pemberian Umpan Balik Adaptif (Adaptive Feedback
Generation)
Berdasarkan hasil analisis performa, sistem menghasilkan
umpan balik yang disesuaikan secara otomatis. Umpan balik
ini dirancang untuk membantu siswa memahami kesalahan
mereka dan memberikan rekomendasi spesifik untuk
perbaikan. Aktivitas-aktivitas Pemberian Umpan Balik
Adaptif adalah sebagai berikut:
▪ Menggunakan teknik Reinforcement Learning untuk
memberikan umpan balik yang dinamis berdasarkan
pola belajar dan kebutuhan siswa.
▪ Menyajikan umpan balik yang jelas dan konstruktif
melalui antarmuka pengguna, yang mencakup saran
untuk peningkatan dan sumber daya tambahan. 4) Integrasi dengan Antarmuka Pengguna (Integration with
User Interface)

247
Umpan balik yang dihasilkan diintegrasikan ke dalam
antarmuka pengguna (dashboard siswa), sehingga siswa
dapat melihat umpan balik mereka secara real-time dan
memahami langkah-langkah yang perlu diambil untuk
meningkatkan pembelajaran mereka. Aktivitas-aktivitas
Integrasi dengan Antarmuka Pengguna adalah sebagai
berikut:
▪ Menampilkan umpan balik dan rekomendasi yang
relevan pada dashboard siswa.
▪ Memungkinkan siswa untuk mengakses sumber daya
pembelajaran tambahan berdasarkan rekomendasi
sistem. 5) Rekomendasi Konten Pembelajaran Tambahan (Additional
Learning Content Recommendation)
Berdasarkan umpan balik yang diberikan, sistem juga
merekomendasikan konten pembelajaran tambahan yang
sesuai dengan kebutuhan siswa. Konten ini dirancang untuk
memperkuat area di mana siswa membutuhkan perbaikan.
Aktivitas-aktivitas Rekomendasi Konten Pembelajaran
Tambahan adalah sebagai berikut:
▪ Menggunakan algoritma rekomendasi (Collaborative
Filtering, Content-Based Filtering) untuk
menyarankan materi pembelajaran tambahan.
▪ Menyediakan tautan langsung ke materi yang
direkomendasikan, seperti video, artikel, atau
latihan soal. 6) Pemantauan Hasil dan Penyesuaian Pembelajaran
(Monitoring Results and Learning Adjustments)
Setelah siswa menerima umpan balik dan mengikuti
rekomendasi, sistem memantau kemajuan siswa secara
berkelanjutan. Penyesuaian dilakukan jika diperlukan untuk
memastikan pembelajaran yang efektif. Aktivitas-aktivitas
Pemantauan Hasil dan Penyesuaian Pembelajaran adalah
sebagai berikut:

248
▪ Memantau interaksi siswa dengan konten
rekomendasi dan mengevaluasi dampak umpan balik
terhadap peningkatan performa.
▪ Menggunakan data baru untuk memperbarui model
AI dan menyesuaikan strategi umpan balik dan
rekomendasi di masa mendatang.

2. Manfaat Diagram Alur Umpan Balik dan Penilaian
   Pada bagian ini membahas berbagai manfaat dari penggunaan
   diagram alur umpan balik dan penilaian, mulai dari peningkatan
   efektivitas pengukuran kinerja hingga pengembangan strategi
   perbaikan yang lebih terarah. Dengan memahami manfaat ini,
   diharapkan dapat mengapresiasi peran diagram alur dalam
   menciptakan lingkungan belajar yang responsif dan dinamis, serta
   dalam mendukung pengambilan keputusan yang lebih informasional
   dan berbasis data.

1) Personalisasi Pembelajaran yang Lebih Efektif
   Dengan mengikuti alur yang terstruktur, sistem dapat
   memberikan umpan balik yang relevan dan tepat waktu,
   yang disesuaikan dengan kebutuhan individu siswa.
2) Peningkatan Kinerja Siswa
   Umpan balik adaptif dan rekomendasi konten membantu
   siswa untuk fokus pada area yang memerlukan perbaikan,
   meningkatkan kinerja mereka secara keseluruhan.
3) Penggunaan AI untuk Umpan Balik Dinamis
   Integrasi pembelajaran mesin dalam analisis performa dan
   pemberian umpan balik memastikan bahwa sistem selalu
   adaptif dan responsif terhadap perubahan pola belajar siswa.
4) Dokumentasi untuk Pengembangan dan Pengujian Sistem:
   Diagram ini berfungsi sebagai alat dokumentasi untuk
   pengembangan lebih lanjut dan pengujian sistem,

249
memastikan bahwa alur kerja umpan balik dan penilaian
bekerja sesuai dengan desain.

Block diagram berikut ini menggambarkan alur proses umpan balik
dan penilaian, menunjukkan bagaimana data hasil evaluasi
dikumpulkan, dianalisis, dan digunakan untuk memberikan umpan
balik yang adaptif. Diagram ini juga menunjukkan integrasi umpan
balik dengan antarmuka pengguna dan bagaimana rekomendasi
konten pembelajaran tambahan dihasilkan.

Gambar 6.4 1 Diagram Alur Umpan Balik dan Penilaian
Block Diagram Alur Umpan Balik dan Penilaian yang menggambarkan
tahapan-tahapan utama dalam proses pemberian umpan balik
adaptif dan penilaian di dalam LENTERAMU. Diagram ini
menunjukkan bagaimana data hasil evaluasi dikumpulkan, dianalisis,

250
dan digunakan untuk memberikan umpan balik yang relevan dan
rekomendasi konten pembelajaran tambahan. Anda dapat melihat
alur proses yang jelas mulai dari pengumpulan data hingga
penyesuaian strategi pembelajaran berdasarkan hasil pemantauan.

. Penjelasan Diagram Alur Kerja Sistem
Diagram Alur Kerja Sistem memberikan gambaran umum tentang
interaksi antara komponen utama dalam LENTERAMU. Berikut
adalah penjelasan komponen utama dalam diagram ini:

1. Antarmuka Pengguna (User Interface)
   Bertindak sebagai titik interaksi utama bagi siswa, guru, dan
   administrator. Melalui antarmuka ini, pengguna dapat
   mengakses berbagai fitur seperti konten pembelajaran,
   evaluasi, dan laporan kinerja. Antrmuka Pengguna terhubung
   langsung dengan modul-modul backend seperti Modul
   Analisis Data Siswa dan Modul Personalisasi Konten untuk
   mendapatkan data dan menampilkan hasilnya kepada
   pengguna.
2. Modul Analisis Data Siswa
   Berfungsi untuk mengumpulkan dan menganalisis data siswa
   untuk mengidentifikasi pola belajar dan memberikan
   wawasan yang lebih dalam mengenai kemajuan siswa. Modul
   ini mengambil data dari Data Warehouse dan memberikan

251
hasil analisis ke Modul Personalisasi Konten dan Modul
Umpan Balik Adaptif. 3) Modul Personalisasi Konten
Modul ini menggunakan hasil analisis untuk
merekomendasikan konten pembelajaran yang sesuai
dengan kebutuhan dan preferensi individu siswa. Modul ini
mengirimkan rekomendasi konten ke Antarmuka Pengguna
untuk diakses oleh siswa. 4) Modul Umpan Balik Adaptif
Berfungsi memberikan umpan balik dinamis kepada siswa
berdasarkan hasil evaluasi dan analisis performa. Modul ini
terintegrasi dengan Antarmuka Pengguna untuk
menampilkan umpan balik, serta berkomunikasi dengan
Modul Analisis Data Siswa untuk mendapatkan informasi
yang diperlukan. 5) Modul Pemantauan dan Penilaian
Berfungsi Memantau kinerja siswa secara keseluruhan dan
menyediakan laporan yang mudah diakses untuk
pengambilan keputusan oleh guru dan administrator. Modul
ini mengambil data dari Data Warehouse dan memberikan
laporan kepada antarmuka pengguna dan sistem
pengambilan keputusan. 6) Data Warehouse dan Sistem Manajemen Database (DBMS)
Berfungsi menyimpan semua data yang dihasilkan dan
dikumpulkan oleh sistem, termasuk data interaksi pengguna,
hasil evaluasi, dan log aktivitas. Modul ini menjadi pusat data
yang menyediakan informasi bagi semua modul yang
memerlukannya. 7) Sistem Keamanan dan Integrasi
Berfungsi mengatur keamanan data, autentikasi pengguna,
dan integrasi antar modul dan komponen sistem. Modul ini
menyediakan lapisan keamanan yang memastikan integritas
dan kerahasiaan data selama komunikasi antar modul.

252 2. Penjelasan Diagram Alur Kerja Pengguna
Diagram Alur Kerja Pengguna memetakan langkah-langkah yang
diambil oleh tiga jenis pengguna utama (Siswa, Guru, dan
Administrator) ketika berinteraksi dengan sistem. Berikut adalah
penjelasan dari alur kerja ini:

1. Siswa (Student)
   Alur Kerja Siswa Dimulai dari login atau registrasi, diikuti
   dengan akses ke dashboard mereka untuk melihat materi
   pembelajaran yang direkomendasikan. Setelah
   menyelesaikan evaluasi, siswa menerima umpan balik
   adaptif dan rekomendasi konten tambahan. Pentingnya alur
   ini adalah memastikan siswa mendapatkan pengalaman
   belajar yang disesuaikan dengan kebutuhan mereka, yang
   dapat meningkatkan keterlibatan dan hasil belajar.
2. Guru (Teacher)
   Alur Kerja Guru Melibatkan proses login, manajemen kelas,
   pembuatan konten pembelajaran, penilaian siswa, serta
   pemantauan dan pemberian umpan balik tambahan.
   Pentingnya alur ini adalah memastikan guru dapat mengelola
   kelas mereka secara efektif, memberikan konten berkualitas,
   dan memantau kemajuan siswa dengan tepat.
3. Administrator (Admin)
   Alur Kerja AdministratorTermasuk login, manajemen data
   pengguna, pemantauan sistem, pengaturan kebijakan
   keamanan, dan penanganan masalah sistem. Pentingnya alur
   ini Memastikan sistem berjalan dengan lancar dan aman,
   serta memberikan dukungan teknis dan operasional yang
   diperlukan.

3) Penjelasan Alur Proses Pembelajaran AI
   Diagram ini menggambarkan alur proses pembelajaran AI mulai dari
   pengumpulan data hingga pemantauan dan pembaruan model:

1. Pengumpulan Data merupakan kegiatan pengumpulan data
   dari berbagai sumber seperti hasil evaluasi siswa, interaksi
   pengguna, dan profil pengguna.

253 2) Praproses Data merupakan kegiatan pengumpulan data yang
diproses untuk memastikan kebersihan dan konsistensinya
sebelum digunakan dalam pelatihan model. 3) Pelatihan Model merupakan algoritma AI yang dilatih
menggunakan data yang telah diproses untuk memprediksi
hasil belajar dan memberikan rekomendasi. 4) Validasi dan Evaluasi Model merupakan model yang dilatih
dan divalidasi menggunakan data terpisah untuk
memastikan generalisasi dan akurasi. 5) Implementasi Model merupakan model yang divalidasi dan
diimplementasikan dalam sistem dan terintegrasi dengan
antarmuka pengguna. 6) Monitoring dan Pembaruan Model merupakan model yang
dipantau secara berkelanjutan dan diperbarui untuk
meningkatkan performa berdasarkan data baru. 4. Penjelasan Diagram Alur Umpan Balik dan Penilaian
Diagram ini memfokuskan pada alur bagaimana hasil evaluasi
digunakan untuk menghasilkan umpan balik adaptif:

1. Pengumpulan Data Hasil Evaluasi merupakan proses
   mengumpulkan data hasil kuis, tes, dan evaluasi lainnya.
2. Analisis Performa Siswa merupakan proses menganalisis data
   untuk mengidentifikasi kekuatan dan kelemahan siswa.
3. Pemberian Umpan Balik Adaptif merupakan proses
   memberikan umpan balik yang disesuaikan berdasarkan
   analisis perfoma.
4. Integrasi dengan Antarmuka Pengguna merupakan umpan
   balik yang dihasilkan disajikan pada dashboard siswa.
5. Rekomendasi Konten Pembelajaran Tambahan: merupakan
   proses menyarankan materi pembelajaran tambahan untuk
   perbaikan.
6. Pemantauan Hasil dan Penyesuaian Pembelajaran
   merupakan proses memantau efektivitas umpan balik dan
   menyesuaikan strategi pembelajaran sesuai kebutuhan.

254 5. Kesimpulan Penjelasan Diagram Alur Kerja
Penjelasan dari diagram-diagram alur kerja ini menunjukkan bahwa
setiap komponen dan proses dalam LENTERAMU bekerja sama untuk
menciptakan lingkungan pembelajaran yang adaptif, responsif, dan
berbasis data. Dengan memahami diagram ini, pengembang dan
pemangku kepentingan dapat mengoptimalkan sistem untuk
mendukung pengalaman belajar yang lebih baik bagi siswa,
meningkatkan efektivitas guru, dan memastikan keamanan serta
efisiensi operasional bagi administrator.
