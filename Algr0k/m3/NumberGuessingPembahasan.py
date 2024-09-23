import sys, random

nama = input("Nama: ")
umur = int(input("Umur: "))

if umur < 17:
    sys.exit("\033[31mAnak kecil tidak boleh mainan game seperti ini.\033[0m")

print(f"\n\n\nSELAMAT DATANG {nama} DI PERMAINAN TERBAIK ABAD INI\nKamu akan menebak angka yang dipilih komputer\nApakah kamu ingin bermain ?")

konfirmasi = input("(y/n): ")
if konfirmasi == "y":
    print("Kita akan bermain!!!\nTebak satu angka dari 1 - 20")
else:
    i = 100
    while i>0:
        print("Kamu tidak seru sekali -_-")
        i -= 1
    sys.exit()

#mulai game
pilihan_komputer = random.randint(1, 20)
pilihan_pengguna= 0
tries = 0
while pilihan_pengguna!= pilihan_komputer:

    if tries > 5:
        confirm = input("Apakah anda ingin menyerah ? ")
        if confirm == "n":
            print("Anda adalah pejuang, saya suka")
            tries -= 5
        else:
            sys.exit("Anda cupu")

    pilihan_pengguna= int(input(": "))
    if pilihan_pengguna> pilihan_komputer:
        print("Turunkan sedikit...")
        tries += 1
    elif pilihan_pengguna< pilihan_komputer:
        print("naikkan sedikit...")
        tries += 1
    elif pilihan_pengguna== pilihan_komputer:
        print(f"Anda Benar !!!\n Selamat {nama} kamu berhasil memenangkan game ini!!!")

"""
1. Import modul sys dan random untuk keperluan program

3-4. Membuat variabel nama dan umur dengan nilai dari masukkan pengguna

6. Eksekusi kondisional, Jika umur yang dimasukkan pengguna dibawah 17 Tahun, program akan berhenti dan menampilkan "Anak kecil tidak boleh mainan game seperti ini." dengan teks berwarna merah

9. Tampilkan "SELAMAT DATANG" nama dengan data dari variabel nama "DI PERMAINAN TERBAIK ABAD INI Kamu akan menebak angka yang dipilih komputer Apakah kamu ingin bermain ?"

11. Membuat varibel konfirmasi yang menerima input ya dan tidak dari pengguna
12 - 19. Blok kode eksekusional, Jika variabel konfirmasi sama dengan "y", tampilkan "Kita akan bermain!!! Tebak satu angka dari 1 - 20". Jika pilihan selain "y" maka mulai while loop yang menampilkan "Kamu tidak seru sekali -_-" sampai variabel i mencapai angka 0 dan keluar dari program

22. Buat variabel pilihan_komputer dengan nilai random menggunakan fungsi randint untuk memilih angka 1 sampai 20 secara acak
23. Buat variabel pilihan_penggunadengan nilai default 0
24. Buat variabel tries dengan nilai default 0
25. buat while loop dengan kondisi jika nilai variabel pilihan_penggunatidak sama dengan pilihan_komputer, maka eksekusi berikut.

27. Eksekusi kondisional, mengecek bila nilai dari variabel tries lebih besar dari 5, buat variabel confirm dengan meminta masukkan dari pengguna dan menampilkan "Apakah anda ingin menyerah ?", jika pengguna memasukkan "n" tampilkan  "Anda adalah pejuang, saya suka" dan kurangi nilai dari variabel tries sebanyak 5. Jika pilihan pengguna selain daripada "y", keluar dari program dan tampilkan "Harus lebih semangat lagi"

35. Buat variabel pilihan_pengguna dengan data masukkan dari pengguna untuk menebak nilai pilihan_komputer
36-38. Eksekusi kondisional, jika pilihan_pengguna lebih besar dari pilihan_komputer, tampilkan "Turunkan sedikit..." dan tambahkan variabel tries dengan 1
39-41.  Eksekusi kondisional, jika pilihan_pengguna lebih kecil dari pilihan_komputer, tampilkan "Naikkan sedikit..." dan tambahkan variabel tries dengan 1
42-43. Eksekusi kondisional, jika pilihan_pengguna lebih besar dari pilihan_komputer, tampilkan "Anda Benar !!! Selamat {nama} kamu berhasil memenangkan game ini!!!" dan tambahkan variabel tries dengan 1 
"""
