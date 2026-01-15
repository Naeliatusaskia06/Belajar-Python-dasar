#Latihan 2: Daftar Mahasiswa dan Nilai
#Menyimpan nama-nama mahasiswa dan nilai mereka dalam sebuah dictionary.
nilai_mahasiswa={
                "rudi": 85,
                "yuri": 79,
                "min-sol": 95
}

#Mencetak semua nama mahasiswa beserta nilainya.
for nama, nilai in nilai_mahasiswa.items():
    print(nama,":", nilai)

#Menambahkan satu mahasiswa baru.
nilai_mahasiswa.update({"yuna": 89,})
print("data directory setelah diperbarui:" ,nilai_mahasiswa)

#Mengupdate nilai salah satu mahasiswa.
nilai_mahasiswa["yuri"] = 80
print("data yuri seteh diupdate:", nilai_mahasiswa)

#Menghapus data salah satu mahasiswa.
del nilai_mahasiswa["yuna"]

# Menampilkan rata-rata nilai seluruh mahasiswa.
total_nilai = sum(nilai_mahasiswa.values())
jumlah_mahasiswa = len(nilai_mahasiswa)
rata_rata = total_nilai / jumlah_mahasiswa
print("Nilai rata-rata adalah:", rata_rata)
