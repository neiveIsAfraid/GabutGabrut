print("\n\n\n===Selamat datang===")
masukan_pengguna = int(input("Masukkan angka yang ingin ditampilkan: "))
hasil = ""
for i in range(1, masukan_pengguna + 1):
    hasil += f"{i}"
    print(hasil)
    if i == masukan_pengguna:
        for j in range(masukan_pengguna, 0, -1):
            print(hasil[0:j-1])

"""
1. Menampilkan tampilan selamat datang
2. Meminta masukan pengguna untuk untuk angka yang ingin dicetak dan dimasukkan kedalam variabel "pilihan_pengguna"
3. Buat variabel hasil dengan nilai string kosong
4. Perulangan for, dengan kondisi iterator  adalah masukan pengguna ditambah 1, dimulai dari angka 1.
5. Masukkan template f-string untuk variabel i yang merupakan iterator dan masukkan kedalam variabel hasil
6. Tampilkan nilai variabel hasil
7 - 8. Perulangan for didalam kondisi eksekusional, jika iterator "i" bernilai sama dengan nilai variabel "masukan_pengguna" maka, pada perulangan for, untuk iterator "j" iterasikan nilai variabel "masukan_pengguna" sampai dengan 0
9. Tampikan isi variable "hasil" dari indeks 0 sampai iterator j dikurang 1
"""