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
