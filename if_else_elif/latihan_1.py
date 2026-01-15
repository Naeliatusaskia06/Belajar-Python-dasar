
#lathian evaluasi gaji

#nilai gaji:
gaji_pokok = 3500000
bonus = 1250000
potongan = 500000
tunjangan_transport = 200000

total_gaji = gaji_pokok + bonus + tunjangan_transport - potongan

#operasi elif
if total_gaji >= 5000000:
    print("Gaji di atas rata-rata")
elif total_gaji >= 3000000 and total_gaji < 5000000:
    print("Gaji Standar")
else:
    print("Gaji dibawah rata-rata")

