# Latihan Bertingkat – while Loop
# Level 1: Dasar
#Cetak angka 1 sampai 10 menggunakan while loop
i = 1
while i <= 10:
    print("i sekarang:", i)
    i += 1  


# Level 2 – while dengan kondisi
#Buat program yang:
#Meminta pengguna memasukkan angka
while True:
    input_penguna= float(input("Silahkan Masukan Anggka:"))
    #Selama angka ≤ 100, program terus minta input lagi
    if input_penguna <= 100:
     print(input_penguna)
    else :
       input_penguna > 100
       print("Kamu menasukan anggka > 100 perogram selesai")
       break #menghentikan loop
#Jika angka > 100, cetak pesan:

#while Loop – Level 3: Validasi Input
while True:
    #Meminta pengguna memasukkan angka positif
    input_noF= int(input("Masukan Anggka Positif:"))
    #Jika pengguna memasukkan angka negatif atau nol, tampilkan:
    if input_noF <= 0:
       print("Anggka yang anda masukan Negatif masukan anggka postif!!!")
    #Jika valid, tampilkan:
    else:
       input_noF  > 0
       print("Terimakasih angka yang anda masukan valid:", input_noF)
       break