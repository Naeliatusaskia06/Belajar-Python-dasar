#Latihan 2: Operasi pada List Angka

#Buatlah list berisi 5 angka.
anggka = [1,2,3,4,4]

#Cetak angka terbesar dan terkecil dari list.
print("anggka terkecil adalah:", min(anggka))
print("anggka terbersar adalah:", max(anggka))

#Hitung rata-rata dari semua angka dalam list.
average = sum(anggka) / len(anggka)
print("nilai averagenya adalah:",average)

#Tambahkan satu angka lagi ke dalam list.
anggka.append(6)

#Cetak semua angka yang lebih besar dari 5
print("Angka > 5:")
for a in anggka:
    if a > 5:
        print(a)
