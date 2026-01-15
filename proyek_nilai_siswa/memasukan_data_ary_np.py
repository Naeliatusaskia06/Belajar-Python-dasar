# Import numpy
import numpy as np

# Gunakan array data_nilai_siswa seperti sebelumnya (bisa copy dari proyek kemarin)
data_ns = np.array([
    [78,78,94],
    [87,85,78],
    [78,90,34],
    [43,78,77],
    [87,90,95]
])
print("=====Output Data_ns=====")
print(data_ns)

# Tambahkan data nilai siswa baru: [88, 77, 66]
data_sb =np.array([[88,77,66]])

#  Gabungkan data siswa baru itu ke dalam array data_nilai_siswa
data_gb = np.vstack((data_ns, data_sb))

# Tampilkan array hasil gabungan
print("=====Output Data_gb=====")
print(data_gb)

#  Hitung kembali rata-rata per siswa dan status kelulusan untuk semua siswa (termasuk yang baru)
rata2_data_gb =np.mean(data_gb , axis=1)
print("Nilai Rata-Rata siswa (baris):" , rata2_data_gb)

# Tampilkan hasil akhir (nilai, rata-rata, dan status kelulusan tiap siswa)
print("Nilai semua semua siswa:")
for i, nilai in enumerate(data_gb):
    rata = rata2_data_gb[i]
    status= "LULUS" if rata >= 75 else "TIDAK LULUS"
    print("Siswa",i+1, "Nilai:", nilai, "Rata-rata:", rata , "Status:", status)
