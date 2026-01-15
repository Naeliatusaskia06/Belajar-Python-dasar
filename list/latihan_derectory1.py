#Latihan 1: Dictionary Dasar
#Buat dictionary berisi data diri kamu (nama, umur, hobi).
data_mahasiswa = {
                    "nama": "naelia",
                    "hobi":"baca buku",
                    "umur": "18",
}

#Cetak salah satu nilai dari dictionary.
print("nama:",data_mahasiswa["nama"])

#Tambahkan kunci baru misalnya: "kota": "Bandung"
print("directory sebelum di tambah",data_mahasiswa)
data_mahasiswa.update( { "kota": "bandung",})
print("directory setelah di tambah:",data_mahasiswa)

#Ubah nilai dari "umur".
data_mahasiswa["umur"] = "sembilan belas"
print("data dengan umur yang sudah di update:" , data_mahasiswa)

#Hapus kunci "hobi".
del data_mahasiswa["hobi"]
print("data setelh hobi di hapus:", data_mahasiswa)

#Cetak dictionary akhirnya.
print("directory akhirnya", data_mahasiswa)

