import datetime
import os


# ==========================================
# DATA AKUN
# ==========================================

akun = {
    "admin": {
        "password": "123",
        "role": "admin"
    },
    "user": {
        "password": "123",
        "role": "user"
    }
}


# ==========================================
# DATA JADWAL
# ==========================================

jadwal = {
    1: {
        "waktu": "07:00",
        "kegiatan": "Kuliah",
        "kategori": "Pendidikan"
    },
    2: {
        "waktu": "16:00",
        "kegiatan": "Bersepeda",
        "kategori": "Hobi"
    }
}


# ==========================================
# FUNGSI LOGIN
# ==========================================

def login():

    while True:

        print("\n================================")
        print("           LOGIN SISTEM")
        print("================================")

        username = input("Username : ")
        password = input("Password : ")

        if username in akun and akun[username]["password"] == password:

            print("\nLogin berhasil!")
            print("Login sebagai:", akun[username]["role"])

            return username, akun[username]["role"]

        else:

            print("\nUsername atau password salah!")
            input("Tekan Enter untuk mencoba lagi...")


# ==========================================
# FUNGSI MENAMPILKAN JADWAL
# ==========================================

def tampil_jadwal():

    print("\n================================")
    print("          DAFTAR JADWAL")
    print("================================")

    if len(jadwal) == 0:

        print("Belum ada jadwal.")
        return

    print("No | Waktu | Kegiatan | Kategori")
    print("--------------------------------")

    for nomor, data in jadwal.items():

        print(
            nomor,
            "|",
            data["waktu"],
            "|",
            data["kegiatan"],
            "|",
            data["kategori"]
        )


# ==========================================
# FUNGSI TAMBAH JADWAL
# ==========================================

def tambah_jadwal():

    print("\n================================")
    print("          TAMBAH JADWAL")
    print("================================")

    waktu = input("Waktu (HH:MM) : ")
    kegiatan = input("Kegiatan       : ")
    kategori = input("Kategori       : ")

    if waktu == "" or kegiatan == "" or kategori == "":

        print("\nData tidak boleh kosong!")
        return

    nomor = max(jadwal.keys(), default=0) + 1

    jadwal[nomor] = {
        "waktu": waktu,
        "kegiatan": kegiatan,
        "kategori": kategori
    }

    print("\nJadwal berhasil ditambahkan!")

    print("\nData jadwal setelah ditambahkan:")
    tampil_jadwal()


# ==========================================
# FUNGSI UBAH JADWAL
# ==========================================

def ubah_jadwal():

    print("\n================================")
    print("           UBAH JADWAL")
    print("================================")

    tampil_jadwal()

    if len(jadwal) == 0:
        return

    try:

        nomor = int(
            input("\nMasukkan nomor jadwal yang diubah: ")
        )

        if nomor not in jadwal:

            print("\nNomor jadwal tidak ditemukan!")
            return

        print("\nMasukkan data baru:")

        waktu = input("Waktu baru    : ")
        kegiatan = input("Kegiatan baru : ")
        kategori = input("Kategori baru : ")

        if waktu == "" or kegiatan == "" or kategori == "":

            print("\nData tidak boleh kosong!")
            return

        jadwal[nomor] = {
            "waktu": waktu,
            "kegiatan": kegiatan,
            "kategori": kategori
        }

        print("\nJadwal berhasil diubah!")

        print("\nData jadwal setelah diubah:")
        tampil_jadwal()

    except ValueError:

        print("\nNomor jadwal harus berupa angka!")


# ==========================================
# FUNGSI HAPUS JADWAL
# ==========================================

def hapus_jadwal():

    print("\n================================")
    print("          HAPUS JADWAL")
    print("================================")

    tampil_jadwal()

    if len(jadwal) == 0:
        return

    try:

        nomor = int(
            input("\nMasukkan nomor jadwal yang ingin dihapus: ")
        )

        if nomor not in jadwal:

            print("\nNomor jadwal tidak ditemukan!")
            return

        print("\nData yang akan dihapus:")

        print("Waktu    :", jadwal[nomor]["waktu"])
        print("Kegiatan :", jadwal[nomor]["kegiatan"])
        print("Kategori :", jadwal[nomor]["kategori"])

        konfirmasi = input(
            "\nYakin ingin menghapus? (y/n): "
        ).lower()

        if konfirmasi == "y":

            del jadwal[nomor]

            print("\nJadwal berhasil dihapus!")

            print("\nData jadwal setelah dihapus:")
            tampil_jadwal()

        else:

            print("\nPenghapusan dibatalkan.")

    except ValueError:

        print("\nNomor jadwal harus berupa angka!")


# ==========================================
# FUNGSI MENU UTAMA
# ==========================================

def menu(role):

    while True:

        print("\n\n================================")
        print(" SISTEM JADWAL KEGIATAN HARIAN")
        print("================================")

        print("Tanggal       :", datetime.date.today())
        print("Login sebagai :", role)

        print("\n----------- MENU -----------")

        print("1. Lihat Jadwal")

        if role == "admin":

            print("2. Tambah Jadwal")
            print("3. Ubah Jadwal")
            print("4. Hapus Jadwal")

        print("0. Keluar")

        pilihan = input("\nPilih menu: ")

        # ======================================
        # LIHAT JADWAL
        # ======================================

        if pilihan == "1":

            tampil_jadwal()

            input("\nTekan Enter untuk kembali ke menu...")


        # ======================================
        # TAMBAH JADWAL
        # ======================================

        elif pilihan == "2" and role == "admin":

            tambah_jadwal()

            input("\nTekan Enter untuk kembali ke menu...")


        # ======================================
        # UBAH JADWAL
        # ======================================

        elif pilihan == "3" and role == "admin":

            ubah_jadwal()

            input("\nTekan Enter untuk kembali ke menu...")


        # ======================================
        # HAPUS JADWAL
        # ======================================

        elif pilihan == "4" and role == "admin":

            hapus_jadwal()

            input("\nTekan Enter untuk kembali ke menu...")


        # ======================================
        # KELUAR
        # ======================================

        elif pilihan == "0":

            print("\n================================")
            print("Program selesai.")
            print("Terima kasih!")
            print("================================")

            break


        # ======================================
        # PILIHAN TIDAK VALID
        # ======================================

        else:

            print("\nPilihan menu tidak valid!")

            input("Tekan Enter untuk mencoba lagi...")


# ==========================================
# PROGRAM UTAMA
# ==========================================

def main():

    username, role = login()

    menu(role)


# ==========================================
# JALANKAN PROGRAM
# ==========================================

main()