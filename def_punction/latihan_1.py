#Latihan Fungsi – Level 1
#Buat fungsi bernama ucapan_selamat yang:
def ucapan_salam(nama):
    print("Helllowww good morning!!!", nama)

ucapan_salam("yuna")
ucapan_salam("min-sol")
ucapan_salam("enbi")


#Latihan Fungsi – Level 2
#Buat fungsi bernama luas_persegi
#Menerima 1 parameter: sisi
def luas_persegi(sisi):
    #Mengembalikan nilai luas dari persegi (sisi * sisi)
    return(sisi * sisi)
#input user
s = int(input("Masukan panjang sisi:"))
#Simpan hasil ke variabel dan cetak hasilnya
luas_p = luas_persegi(s)
print("Luas persegi adalah:" ,luas_p)

 #Latihan Fungsi – Level 3: Volume Balok
#Instruksi:
#Buatlah fungsi bernama volume_balok
#Fungsi menerima 3 parameter: panjang, lebar, dan tinggi
def volume_belok(panjang, lebar, tinggi):
    return(panjang * lebar * tinggi)

#input dari penguna
p = int(input("masukan nilai panjang:"))
l = int(input("masukan nilai lebar:"))
t = int(input("masukan nilai tinggi:"))
volume = volume_belok(p,l,t)

#output
print("volumenya adalah:",volume)


#Latihan Fungsi – Level 3: Konversi Suhu
#Instruksi:
#Buatlah fungsi bernama konversi_suhu.
def konversi_suhu(celcius):
    return((celcius * 9/5) +32)

i= int(input("masukan nilai celcies:"))
fahrenheit = konversi_suhu(i)
print("dalam fahrenheit:",fahrenheit)
    


