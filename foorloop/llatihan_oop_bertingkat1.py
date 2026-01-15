#Buatlah sebuah list berisi 3 siswa, masing-masing memiliki nama dan daftar 2 nilai ujian. 
#Cetak nama siswa dan seluruh nilainya satu per satu.
siswa = [
    ["Risa", [85, 84]],
    ["Elsa", [81, 89]],
    ["Wullan", [91, 87]]
]

for data in siswa:
    nama = data[0]
    nilai = data[1]

    print("Nama:", nama)
    for n in nilai:
        print("  Nilai:", n)

    rata_rata = sum(nilai) / len(nilai)
    print("  Rata-rata:", rata_rata)
    print()
