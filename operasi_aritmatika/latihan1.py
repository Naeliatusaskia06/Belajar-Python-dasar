# Latihan aritmatika menghitung total gaji
gaji_pokok = 3500000
bonus = 1250000
potongan = 500000
tunjangan_transport = 200000

total_gaji = gaji_pokok + bonus + tunjangan_transport - potongan

print("Total gaji bersih adalah:", total_gaji)

# Apakah gaji bersih lebih dari 5 juta?
gaji_lebih_dari_5jt = total_gaji > 5000000
print("Apakah lebih dari 5jt:", gaji_lebih_dari_5jt)

# Apakah bonus lebih kecil dari potongan?
apakah_bonus_lebih_kecil_dari_potongan = bonus < potongan
print("Apakah bonus lebih kecil dari potongan:", apakah_bonus_lebih_kecil_dari_potongan)
