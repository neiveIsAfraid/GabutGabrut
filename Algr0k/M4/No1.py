print("\n\n\nSelamat Datang di Program \033[31mPencetak Deret Harmonik\033[0m sampai N")
template = "1"
hasil = 0
pilihan = "y"

while pilihan == "y":
    masukan_pengguna = int(input("\nMasukkan angka: "))
    for i in range(1, masukan_pengguna + 1):
        rumus = (1/i)
        hasil += rumus
        if i != 1:
            template += f" + (1/{i})"
    print(template ," = ", hasil)
    pilihan = input("Lanjut [y/n]: ")
    template = "1"
    hasil = 0


"""
1. Tampilkan ucapan selamat datang ke pengguna dengan teks "Selamat Datang di Program Pencetak Deret Harmonik sampai N" dengan teks "Program Pencetak Deret Harmonik" berwarna merah
2. Membuat variabel template dengan nilai string "1" sebagai template hasil
3. Buat variabel "hasil" dengan nilai 0
4. Buat variabel "pilihan" dengan nilai default "y" yang akan digunakan pada perulangan while

6. Buat perulangan while dengan kondisi bila variabel pilihan sama dengan "y", eksekusi kode berikut
7. Buat variabel "masukan_pengguna" dengan masukan pengguna berupa pilihan sampai angka berapa yang akan dicetak 
8. Buat perulangan for dengan iterator "i" dan range dimulai dari 1 sampai nilai variabel "masukan_pengguna" + 1
9. Buat variabel rumus dengan nilai 1 dibagi nilai dari variabel i
10. Buat variabel "hasil" dengan nilai "hasil" ditambah hasil kalkulasi variabel rumus
11. Buat kondisi eksekusional agar template hasil tidak menampilkan 1/1
12. Simpan f-string " + (1/{i})" kedalam variabel "template" sebagai kerangka tampilan    
13. tampilkan data variabel "template" dengan "=" dan nilai variabel "hasil"
14. Buat variabel pilihan yang menerima masukan dari pengguna sebagai konfirmasi apabila pengguna ingin melanjutkan program.
15. Masukkan "1" kedalam variabel template untuk reset variabel
16. Masukkan 0 kedalam variabel hasil untuk reset variabel 
"""


