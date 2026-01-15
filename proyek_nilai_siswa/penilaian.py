# ========================
# Sistem Penilaian Siswa
# ========================

#  Buat daftar siswa dalam bentuk list of dictionary
#    Setiap dictionary berisi nama dan daftar nilai (2 nilai ujian misalnya)

nilai_ujian= [
    {"nama":"Yuna", "nilai":[85,84]},
    {"nama":"Min_sol", "nilai":[92,95]},
    {"nama":"Nari", "nilai":[75,83]},
    {"nama":"Nara", "nilai":[95,95]},
    {"nama":"En-bi", "nilai":[83,83]},
]

#  Buat fungsi untuk menghitung rata-rata dari list nilai
def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)

#  Buat fungsi untuk menentukan status kelulusan berdasarkan rata-rata
def cek_kelulusan(rata_rata):
    return "Lulus" if rata_rata >75 else "Tidak Lulus"

# Tambahkan menu sederhana: lihat data, tambah data, keluar
# ========================
# Menu Interaktif
# ========================

while True:
    print("\n=== MENU ===")
    print("1. Lihat semua data siswa")
    print("2. Tambah siswa baru")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        # Lihat semua data siswa
        for data in nilai_ujian:
            print("\nNama:", data["nama"])
            print("Nilai:", data["nilai"])
            rata = hitung_rata_rata(data["nilai"])
            print("Rata-rata:", rata)
            status = cek_kelulusan(rata)
            print("Status:", status)

    elif pilihan == "2":
        # Tambah siswa baru
        nama_baru = input("Masukkan nama siswa baru: ")
        try:
            n1 = int(input("Masukkan nilai 1: "))
            n2 = int(input("Masukkan nilai 2: "))
        except ValueError:
            print("Nilai harus berupa angka!")
            continue

        # Simpan ke dalam list nilai_ujian
        nilai_ujian.append({
            "nama": nama_baru,
            "nilai": [n1, n2]
        })
        print("Data siswa berhasil ditambahkan.")

    elif pilihan == "3":
        # Keluar dari program
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")



#  Buat perulangan untuk menampilkan data semua siswa:
# Tampilkan nama siswa
for data in nilai_ujian:
    print("Nama:",data["nama"])
    # - Tampilkan semua nilai siswa
    print("Nilai",data["nilai"])
    # - Hitung dan tampilkan rata-rata nilai
    for n in data["nilai"]:
        print("  Nilai:", n)
    
    # Ini di luar loop 'for n' tapi masih di dalam 'for d'
    rata_rata = hitung_rata_rata(data["nilai"])
    print(f"{data['nama']} Nilai rata-rata: {rata_rata}")
 
# Tampilkan status kelulusan ("Lulus" jika rata-rata >= 75)
    cek= cek_kelulusan(rata_rata)
    print(f"{data["nama"]} Di Nyatakan:{cek}")

# Tambahkan siswa baru ke dalam daftar dengan input()
# Menambahkan siswa baru dengan input dari pengguna
print("\n=== Tambah Siswa Baru ===")
nama_baru = input("Masukkan nama siswa baru: ")
nilai1 = int(input("Masukkan nilai ujian 1: "))
nilai2 = int(input("Masukkan nilai ujian 2: "))

# Buat dictionary baru dan tambahkan ke list nilai_ujian
siswa_baru = {
    "nama": nama_baru,
    "nilai": [nilai1, nilai2]
}
nilai_ujian.append(siswa_baru)

print("\nData berhasil ditambahkan!")

# Simpan hasil akhir ke file .txt menggunakan write()
with open("data_siswa.txt", "w") as file:
    for siswa in nilai_ujian:
        nama = siswa["nama"]
        nilai = ", ".join(str(n) for n in siswa["nilai"])
        file.write(f"{nama}: {nilai}\n")
