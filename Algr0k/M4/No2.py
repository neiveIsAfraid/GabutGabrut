print("\n\nSelamat datang pada program 'Fibonnaci Printer'")
n1 = 0
n2 = 1
hasil = f"{n2}"
pilihan_pengguna = int(input("Masukkan Angka: "))

for i in range(1, pilihan_pengguna):
    n3 = n1 + n2
    hasil += f", {n3}"
    n1 = n2
    n2 = n3

print(hasil)

"""
1. Buat variabel n1 dengan nilai 0
2. Buat variabel n2 dengan nilai 1
3. Buat variabel hasil dengan f-string nilai dari "n2"
4. Buat variabel "pilihan_pengguna" dengan nilai dari masukan pengguna berupa angka yang bertipe data integer

6. Perulangan for dengan jarak dari nilai "pilihan_pengguna" - 1
7. Buat variabel n3 dengan data "n1" ditambah "n2"
8. Tambah variabel hasil dengan f-string template berupa nilai dari variabel n3
9. Masukkan nilai variabel n1 kedalam variabel n2
10. Masukkan nilai variabel n2 kedalam n3
"""