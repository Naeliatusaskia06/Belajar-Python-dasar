#Level 1: Dasar
#Cetak angka 1 sampai 10 menggunakan for loop dan range().

for i in range(1,10):
    print("perulangan:",i)

print("===========================================")
# Level 2: Menengah
#Diberi list:

#list
angka = [3, 6, 9, 12, 15]
#Cetak semua angka satu per satu
for item in angka:
    print("angka:", item)

#Hitung dan cetak total jumlahnya
jumlah_semua= sum(angka)
print("jumlah seua adalah:", jumlah_semua)

print("==================================")
# Level 3: 
#Diberi list:
# List nilai
nilai = [78, 85, 60, 92, 88, 70]

# Buat list baru untuk menyimpan nilai di atas 80
nilai_atas80 = []

# Loop untuk filter nilai
for data in nilai:
    if data > 80:
        print("Data di atas 80:", data)
        nilai_atas80.append(data)

# Hitung jumlah dan rata-rata
jumlah_data = len(nilai_atas80)
total = sum(nilai_atas80)
rata_rata = total / jumlah_data

# Cetak hasil
print("Jumlah nilai di atas 80:", jumlah_data)
print("Rata-rata nilai di atas 80:", round(rata_rata, 2))

