print("\n\n\nKonversi berkas tanpa baris")
with open(input("Nama berkas yang ingin di buka: "), "r") as f:
  file = f.read().split("\n")
  new_file = open(input("Berkas yang ingin ditulis: "), "a")
  for i in file:
    new_file.write(i)
print("Berkas Berhasil dibuat")
"""
1. Tampilkan judul program kepada pengguna
2. Meminta masukan nama berkas yang ingin dibuka kepada pengguna dengan mode buka berkas "r" atau read, buka berkas sebagai variabel "f"
3. Deklarasi variabel "file" yang memiliki value membuka variabel "f" dan memisahkan konten dalam berkas dengan parameter baris baru atau "\n"
4. Deklarasi variabel "new_file" yang meminta masukan nama berkas yang ingin ditulis, menggunakan mode "a" atau "append"
5. Perulangan for yang mengiterasi isi variabel "file" dengan iterator "i" 
6. Tulis isi iterator "i" kedalam file "new_file"
7. Tampilkan pesan bahwa berkas berhasil dibuat kepada pengguna
"""
