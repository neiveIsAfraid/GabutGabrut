nama_berkas = input("Nama berkas yang ingin dibuka: ")
with open(nama_berkas, "r") as file:
  berkas_baru = file.read()
  kata_kata = berkas_baru.split(" ")

filebaru = input("Nama berkas yang ingin dibuat: ")
with open(filebaru, "w") as file:
  counter = 1
  for i in kata_kata:
    file.write(f"Posisi {counter}: {i}\n")
    counter += 1
print("Berkas berhasil dibuat")

"""
1. Deklarasi variabel "nama_berkas" yang meminta masukan dari pengguna berupa nama berkas yang akan dibuka
2. Membuka file yang terdapat dalam variabel "nama_berkas" dengan mode "r" atau read, dan masukkan kedalam variabel "file"
3. Deklarasi variabel "berkas_baru" yang berisi isi dari variabel "file"
4. Deklarasi variabel "kata_kata" yang memisahkan isi dari variabel "berkas_baru" berdasarkan spasi (" ")
6. Deklarasi variabel "filebaru" yang meminta masukan dari pengguna berupa nama berkas yang ingin dibuat
7. Membuka file yang terdapat dalam variabel "filebaru" dengan mode "w" atau write, dan buka sebagai variabel "file"
8. Deklarasi variabel "counter" yang memiliki nilai default 1, variabel ini berguna dalam menghitung posisi masing masing kata
9 - 10. perulangan for yang mengiterasi variabel "kata_kata" dengan iterator i, masukkan posisi sesuai dengan variabel counter dan kata yang terdapat pada iterator "i" untuk setiap kali iterasi.
11. tambahkan nilai variabel "counter" dengan 1 untuk setiap kali iterasi 
12. Tampilkan teks bahwa berkas berhasil dibuat kepada pengguna 
"""
