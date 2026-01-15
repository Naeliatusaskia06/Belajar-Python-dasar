#Buat list berisi 3 siswa (pakai dictionary).
#Untuk setiap siswa, tampilkan:
data_siswa = [
    {"Nama": "yuri", "nilai": [82, 87]},
    {"Nama": "min-sol", "nilai": [92, 97]},
    {"Nama": "nari", "nilai": [82, 89]},
]

# Tampilkan semua nilai dan rata-rata
for d in data_siswa:
    print("Nama:", d["Nama"])
    
    # Cetak semua nilai
    for n in d["nilai"]:
        print("  Nilai:", n)
    
    # Hitung rata-rata
    jumlah = sum(d["nilai"])
    total = len(d["nilai"])
    rata_rata = jumlah / total
    print("  Nilai rata-rata:", rata_rata)
    print()

# Tentukan predikat
    if rata_rata >= 90:
        predikat = "A"
    elif rata_rata >= 80:
        predikat = "B"
    elif rata_rata >= 70:
        predikat = "C"
    else:
        predikat = "D"
    
    print("  Predikat:", predikat)
    print()
