from prettytable import PrettyTable
import pwinput


# DATA PRODUK SKINCARE
skincare = {
    1: {"nama": "Toner", "harga": 40000, "tanggal": "01-09-2025"},
    2: {"nama": "Serum", "harga": 140000, "tanggal": "05-09-2025"},
    3: {"nama": "Moisturizer", "harga": 60000, "tanggal": "12-09-2025"},
    4: {"nama": "Sunscreen", "harga": 50000, "tanggal": "20-09-2025"},
    5: {"nama": "Facial Wash", "harga": 80000, "tanggal": "25-09-2025"}
}

# AKUN LOGIN
users = {
    "GlowQueen": {"password": "300507", "role": "👑 Manager"},
    "BabyGlow": {"password": "130706", "role": "🐣 Karyawan"}
}

# READ
def read_produk():
    if not skincare:
        print("📭 Data skincare masih kosong!")
        return
    table = PrettyTable(["NO", "Nama Produk", "Harga", "Tanggal Beli"])
    for no_produk, data in skincare.items():
        table.add_row([no_produk, data["nama"], data["harga"], data["tanggal"]])
    print(table)

# CERATE
def create_produk():
    try:
        nama = input("Masukkan nama produk baru: ")
        harga = int(input("Masukkan harga produk: "))
        tanggal = input("Masukkan tanggal beli (dd-mm-yyyy): ")
        new_id = max(skincare.keys()) + 1
        skincare[new_id] = {"nama": nama, "harga": harga, "tanggal": tanggal}
        print(f"✅ Produk '{nama}' berhasil ditambahkan!")
    except ValueError:
        print("❌ Harga harus berupa angka!")
    read_produk()

# UPDATE
def update_produk():
    read_produk()
    try:
        no_produk = int(input("Masukkan NO produk yang mau diubah: "))
        if no_produk in skincare:
            nama = input("Masukkan nama baru: ")
            harga = int(input("Masukkan harga baru: "))
            tanggal = input("Masukkan tanggal beli baru: ")
            skincare[no_produk] = {"nama": nama, "harga": harga, "tanggal": tanggal}
            print("✅ Data berhasil diupdate!")
        else:
            print("❌ NO produk tidak ditemukan!")
    except ValueError:
        print("⚠️ Input harus berupa angka!")
    read_produk()

# DELETE 
def delete_produk():
    read_produk()
    try:
        no_produk = int(input("Masukkan NO produk yang mau dihapus: "))
        if no_produk in skincare:
            deleted = skincare.pop(no_produk)
            print(f"✅ Produk '{deleted['nama']}' berhasil dihapus!")
        else:
            print("❌ NO produk tidak ditemukan!")
    except ValueError:
        print("⚠️ Input harus berupa angka!")
    read_produk()

# TOTAL PENGELUARAN 
def total_pengeluaran():
    total = sum([data["harga"] for data in skincare.values()])
    read_produk()
    print(f"💅 Karena cantik itu investasi... total skincare kamu💸: Rp {total}" )


while True:
    print("============ SISTEM PENCATAT BIAYA SKINCARE ============")
    print("1. Masuk sebagai Manager")
    print("2. Masuk sebagai Karyawan")
    try:
        pilihan_role = int(input("👉 Pilih role (1 atau 2): "))
        if pilihan_role == 1:
            expected_role = "👑 Manager"
            break
        elif pilihan_role == 2:
            expected_role = "🐣 Karyawan"
            break
        else:
            print("❌ Pilihan tidak valid! Silahkan pilih 1 atau 2!\n")
    except ValueError:
        print("⚠️ Input harus berupa angka!\n")


while True:
    username = input("👤 Username: ")
    password = pwinput.pwinput("🔑 Password: ")

    if username in users and users[username]["password"] == password and users[username]["role"] == expected_role:
        role = users[username]["role"]
        print(f"\n✅ Login berhasil! Selamat datang, anda login sebagai {role}.")
        break
    else:
        print("❌ Login gagal! Username atau password salah.\nSilakan coba lagi...\n")


while True:
        if role == "👑 Manager":
            print("\n=== MENU MANAGER ===")
            print("1. Lihat Produk 👀")
            print("2. Tambah Produk 💅")
            print("3. Update Produk 📝")
            print("4. Hapus Produk ❌")
            print("5. Total Pengeluaran 💸")
            print("6. Keluar 🚪")
        else:  # Karyawan
            print("\n=== MENU KARYAWAN ===")
            print("1. Lihat Produk 👀")
            print("5. Total Pengeluaran 💸")
            print("6. Keluar 🚪")

        try:
            pilihan = int(input("👉 Pilih Menu: "))
            if pilihan == 1:
                read_produk()
            elif pilihan == 2 and role == "👑 Manager":
                create_produk()
            elif pilihan == 3 and role == "👑 Manager":
                update_produk()
            elif pilihan == 4 and role == "👑 Manager":
                delete_produk()
            elif pilihan == 5:
                total_pengeluaran()
            elif pilihan == 6:
                print("👋 Terima kasih sudah menggunakan sistem ini!")
                break
            else:
                print("❌ Pilihan tidak valid atau tidak punya akses!")
        except ValueError:
            print("⚠️ Input harus berupa angka!")
else:
    print("❌ Login gagal! Username atau password salah")