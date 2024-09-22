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
pil = 0
tries = 0
while pil != pilihan_komputer:

    if tries > 5:
        confirm = input("Apakah anda ingin menyerah ? ")
        if confirm == "n":
            print("Anda adalah pejuang, saya suka")
            tries -= 5
        else:
            sys.exit("Anda cupu")

    pil = int(input(": "))
    if pil > pilihan_komputer:
        print("Turunkan sedikit...")
        tries += 1
    elif pil < pilihan_komputer:
        print("naikkan sedikit...")
        tries += 1
    elif pil == pilihan_komputer:
        print(f"Anda Benar !!!\n Selamat {nama} kamu berhasil memenangkan game ini!!!")

"""
1. Import modul sys dan random untuk keperluan progrma
3-4. Membuat variabel nama dan umur dengan nilai dari masukkan pengguna
6. Eksekusi kondisional, Jika umur yang dimasukkan pengguna dibawah 17 Tahun, program akan berhenti dan menampilkan "Anak kecil tidak boleh mainan game seperti ini." dengan teks berwarna merah
9. Tampilkan Selamat datang

"""