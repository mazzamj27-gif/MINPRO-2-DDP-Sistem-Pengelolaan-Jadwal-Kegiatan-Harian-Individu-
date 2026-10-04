nama: muhammad azzam juhdi
NIM: 2609116089
kelas: C

>> Deskripsi singkat program
Sistem Pengelolaan Jadwal Kegiatan Harian Individu
ini tentang mengatur jadwal kita ngapain aja misalnya (jam 01:00 kita login valorant)
terus di jam (12:00 kita break/ishoma itu kita makan siang atau sholat)
dan juga kita bisa menghapus jadwalnya contohnya jam 01:00 kita ganti jamnya, serta di jam itu kita nagapain aja contohnya
(jam 01:00 ganti 10:00 kita mau berenang)

>> Gambar flowchart serta penjelasanya
>> penjelasan

1. Mulai
   Sistem dijalankan dan pengguna masuk ke halaman login.
2. Login
   Pengguna memasukkan username dan password.
3. Validasi Login
   Sistem memeriksa data login. Jika salah, pengguna login kembali. Jika benar, lanjut ke pengecekan role.
4. Cek Role
   Sistem menentukan pengguna sebagai **Admin** atau User
5. Menu Admin
   Admin dapat melihat, menambah, mengubah, dan menghapus jadwal.
6. Menu User
   User dapat melihat jadwal dan keluar dari sistem.
7. Pilih Menu
   Pengguna memilih menu yang tersedia.
8. Tampilkan Jadwal
   Sistem menampilkan data jadwal.
9. Tambah Jadwal
   Pengguna memasukkan waktu dan kegiatan, kemudian data disimpan.
10. ubah Jadwal
    Pengguna memilih jadwal dan mengubah datanya.
11. Hapus Jadwal
    Pengguna memilih jadwal untuk dihapus.
12. Pilih Kembali atau Selesai
    Pengguna dapat kembali ke menu atau mengakhiri sistem.
13. Selesai
    Sistem berakhir setelah pengguna keluar.

>> gambar flowcahrt
<img width="1920" height="1080" alt="Screenshot 2026-10-04 212155" src="https://github.com/user-attachments/assets/e2e6c00a-a427-41aa-aeba-f1d50ce0011e" />

>> Dokumentasi Program & Output, disertai dengan penjelasannya

>> gambar programnya
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214017" src="https://github.com/user-attachments/assets/25fe83c7-60bc-48e6-9f1f-e3e3912c2322" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214029" src="https://github.com/user-attachments/assets/611c8c9a-7668-43e6-9cbe-4bc52ee3114d" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214042" src="https://github.com/user-attachments/assets/e8f83faa-e00f-402d-ace5-d371d3b4111b" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214049" src="https://github.com/user-attachments/assets/0359fa56-b213-412a-b61b-c90cf68cb42c" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214057" src="https://github.com/user-attachments/assets/c4019b88-c50c-4f73-baf0-09fb3d2c8990" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214104" src="https://github.com/user-attachments/assets/34831ce2-a22d-47af-b514-d8168342126e" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214112" src="https://github.com/user-attachments/assets/46632f44-849e-4c91-a4b4-dff44481b864" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214122" src="https://github.com/user-attachments/assets/02dd0c2e-97c2-4735-a60b-36bc13a1ec2e" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214130" src="https://github.com/user-attachments/assets/86f3bce1-65f2-4163-ad05-223a14ff64b4" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214136" src="https://github.com/user-attachments/assets/8db6c4d2-fd66-411f-84f9-7b313b30d1c7" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214142" src="https://github.com/user-attachments/assets/c2bf973f-92a6-4038-a574-282d7a4cdda0" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 214149" src="https://github.com/user-attachments/assets/6075c114-3bc6-4548-86b2-a36dfd857ecb" />
>> penjelasannya programnya
1. Import Library
   Program menggunakan `datetime` untuk menampilkan tanggal dan `os` sebagai library pendukung.
2. Data Akun
   Program memiliki dua akun, yaitu admin dan user. Keduanya memiliki password dan hak akses yang berbeda.
3. Data Jadwal
   Data jadwal berisi **waktu, kegiatan, dan kategori. Data awal yang tersedia adalah kegiatan kuliah dan bersepeda.
4. Fungsi Login
   Fungsi `login()` digunakan untuk memeriksa username dan password. Jika benar, pengguna dapat masuk sesuai role. Jika salah, pengguna diminta mencoba kembali.
5. Menampilkan Jadwal
   Fungsi `tampil_jadwal()` digunakan untuk menampilkan seluruh jadwal yang tersimpan.
6. Menambah Jadwal
   Fungsi `tambah_jadwal()` memungkinkan Admin menambahkan jadwal baru berupa waktu, kegiatan, dan kategori.
7. Mengubah Jadwal
   Fungsi `ubah_jadwal()` digunakan Admin untuk memilih dan memperbarui data jadwal yang sudah ada.
8. Menghapus Jadwal
   Fungsi `hapus_jadwal()` digunakan Admin untuk menghapus jadwal setelah melakukan konfirmasi.
9. Menu Utama
   Fungsi `menu()` menampilkan pilihan berdasarkan role. Admin dapat melihat, menambah, mengubah, dan menghapus jadwal, sedangkan User hanya dapat melihat jadwal.
10. Program Utama
    Fungsi `main()` menjalankan proses login kemudian membuka menu sesuai role pengguna. Program dapat diakhiri melalui pilihan Keluar.




>> gambar outputnya
<img width="1920" height="1080" alt="Screenshot 2026-10-04 210817" src="https://github.com/user-attachments/assets/b1a76414-1a6c-48ac-b4db-ca58fcf0f29d" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 210832" src="https://github.com/user-attachments/assets/d97c8829-3b59-43c9-854f-398f7d1445dc" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 210849" src="https://github.com/user-attachments/assets/375e5da1-fd7a-403c-b77f-ddc4ce6bcd18" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 210900" src="https://github.com/user-attachments/assets/9d734fe6-c9a8-43a2-8fa4-3ece904a80eb" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 210911" src="https://github.com/user-attachments/assets/d5ec209f-fdbb-45bf-9ac0-434658227fe5" />
<img width="1920" height="1080" alt="Screenshot 2026-10-04 210921" src="https://github.com/user-attachments/assets/5235bf1b-7781-4fcb-9332-3b28c7638511" />

>> penjelasan outputnya

1.dan ini Tampilan Login
Gambar pertama menunjukkan halaman login yang digunakan untuk memasukkan username dan password agar dapat mengakses sistem.
2.ini Tampilan Menu Utama
Gambar kedua menunjukkan menu utama setelah pengguna berhasil login. Menu yang ditampilkan disesuaikan dengan hak akses Admin atau User.
3. ini Tampilan Lihat Jadwal
Gambar ketiga menunjukkan daftar jadwal kegiatan yang tersimpan, meliputi nomor, waktu, kegiatan, dan kategori.
4.dan ini Tampilan Tambah Jadwal
Gambar keempat menunjukkan proses penambahan jadwal dengan mengisi waktu, nama kegiatan, dan kategori. Data yang dimasukkan akan disimpan ke dalam sistem.
5.ini Tampilan Ubah Jadwal
Gambar kelima menunjukkan proses mengubah jadwal yang sudah ada dengan memasukkan nomor jadwal dan data baru.
6.jadi ini Tampilan Hapus Jadwal
Gambar keenam menunjukkan proses penghapusan jadwal dengan memilih nomor jadwal dan melakukan konfirmasi sebelum data dihapus.
