# Panduan Maintenance Aplikasi LENTERAMU

## ToDo List Maintenance (Detail & Urut)

1. **Manajemen Dependency**

- [ ] Cek perubahan library pada kode dan update `requirements.txt` jika perlu
- [ ] Lakukan instalasi/upgrade dependency:
  - [ ] Jalankan `pip install --upgrade -r requirements.txt`
  - [ ] Pastikan tidak ada error saat instalasi
- [ ] Hapus dependency yang tidak lagi digunakan dari `requirements.txt`

2. **Backup & Restore**

- [ ] Backup database secara berkala (export SQL)
- [ ] Backup seluruh file project (termasuk `requirements.txt`, `config.py`, dan file statis)
- [ ] Simpan backup di lokasi aman (cloud/local)
- [ ] Uji proses restore secara berkala

3. **Penyesuaian & Review Kode**

- [ ] Pastikan seluruh data processing dan Q-Learning menggunakan native Python
- [ ] Hapus import dan kode yang tidak digunakan
- [ ] Review konfigurasi database di `config.py` jika ada perubahan environment
- [ ] Pastikan tidak ada library eksternal berat (pandas, numpy, scikit-learn, dsb)

4. **Testing Fitur Utama**

- [ ] Uji login dan akses fitur untuk semua role (admin, guru, siswa)
- [ ] Lakukan testing manual pada endpoint API utama
- [ ] Pastikan seluruh fitur berjalan normal setelah update/deployment

5. **Manajemen File Statis**

- [ ] Pastikan file CSS dan JS terbaru sudah terupload
- [ ] Cek apakah file statis tidak corrupt dan dapat diakses dari browser

6. **Monitoring & Troubleshooting**

- [ ] Cek error log cPanel secara rutin (Error Log, Python App Log)
- [ ] Tindaklanjuti bug/error yang ditemukan
- [ ] Pastikan environment variable sudah benar

7. **Dokumentasi & Catatan**

- [ ] Dokumentasikan setiap perubahan kode/fungsi/fitur di file ini
- [ ] Update instruksi deployment jika ada perubahan proses
- [ ] Catat kendala dan solusi yang ditemukan selama maintenance

## 1. Update & Instalasi Dependency

- Selalu gunakan file `requirements.txt` terbaru yang sudah dioptimalkan untuk cPanel (tanpa pandas, numpy, scikit-learn, dll).
- Untuk update dependency:
  ```bash
  pip install --upgrade -r requirements.txt
  ```
- Pastikan environment Python di cPanel minimal versi 3.9.

## 2. Deployment di cPanel

1. Upload seluruh project ke File Manager cPanel.
2. Masuk ke menu **Python App** di cPanel.
3. Buat aplikasi Python baru (versi 3.9+).
4. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```
5. Set file startup ke `app.py` atau `passenger_wsgi.py`.
6. Konfigurasi database di `config.py` sesuai environment hosting.

## 3. Penyesuaian Kode

- Pastikan seluruh data processing dan Q-Learning menggunakan native Python (tanpa pandas/numpy).
- Jika ada library eksternal yang tidak bisa diinstal di cPanel, ganti dengan solusi native Python.
- Hapus import dan pemanggilan library yang sudah tidak digunakan dari kode.

## 4. Backup & Restore

- Backup file project dan database secara berkala.
- Simpan file `requirements.txt` dan `config.py` di tempat aman.
- Untuk restore, upload ulang file dan lakukan instalasi dependency seperti langkah deployment.

## 5. Troubleshooting

- Jika aplikasi gagal dijalankan:
  - Cek error log di cPanel (menu Error Log atau Python App Log).
  - Pastikan semua dependency sudah terinstall dan versi Python sesuai.
  - Cek konfigurasi database dan environment variable.
- Jika ada error import library, pastikan library tersebut memang ada di `requirements.txt` dan sudah diinstall.

## 6. Update Aplikasi

- Jika ada update kode atau fitur:
  1. Upload file yang diupdate ke server.
  2. Jika ada perubahan dependency, update `requirements.txt` dan jalankan kembali `pip install -r requirements.txt`.
  3. Restart aplikasi dari menu Python App.

## 7. Catatan

- Jangan menambah dependency berat (pandas, numpy, scikit-learn, dsb) agar tetap ringan dan kompatibel dengan cPanel.
- Selalu cek kompatibilitas versi library dengan Python 3.9+.
- Dokumentasikan setiap perubahan pada file `maintenance.md` ini.

---

**Terakhir diperbarui:** 23 September 2025
