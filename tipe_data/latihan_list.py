#lathan
#Level 1: Dasar
#Buat list berisi 5 nama teman
nama_teman = ["irma", "rika", "wulan","ica","yuna"]

#Tambahkan 1 nama menggunakan .append()
nama_teman.append("yuri")

#Cetak semua nama
print("list nama teman:", nama_teman)



# Latihan 2 - Dictionary
print("="*100)

# Buat dictionary berisi informasi buku
data_buku = {
    "judul": "Senyuman Sang Senja",
    "penulis": "Kang Min-sol",
    "tahun": 2025,
    "rating": 4.9
}

# Cetak semua nilainya satu per satu
print("Judul:", data_buku["judul"])
print("Penulis:", data_buku["penulis"])
print("Tahun:", data_buku["tahun"])
print("Rating:", data_buku["rating"])

# Tambahkan key "kategori"
data_buku["kategori"] = "Fiksi"

# Cetak dictionary yang sudah diperbarui
print("Data buku yang sudah diperbarui:", data_buku)

