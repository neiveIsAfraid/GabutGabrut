with open(input("Nama berkas yang ingin di buka: "), "r") as f:
  file = f.read().split("\n")
  new_file = open(input("Berkas yang ingin ditulis: "), "w")
  new_file.write(file)
print("Berkas Berhasil dibuat")
"""
1. Meminta masukan nama berkas yang ingin dibuka kepada pengguna dengan mode buka berkas "r" atau read, buka berkas sebagai variabel "f"
2. Deklarasi variabel "file" yang memiliki value membuka variabel "f" dan memisahkan konten dalam berkas dengan parameter baris baru atau "\n"
3. Deklarasi variabel "new_file" yang meminta masukan nama berkas yang ingin ditulis, menggunakan mode "w" atau "write"
4. Tulis isi variabel "file" kedalam file "new_file"
5. Tampilkan pesan bahwa berkas berhasil dibuat kepada pengguna
"""
