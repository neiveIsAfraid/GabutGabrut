print("\n\nProgram Pembalik Kata dalam Kalimat")

kalimat_masukan = input("Masukkan kalimat\n:")
temporary = kalimat_masukan.split(" ") 
kalimat_terbalik = ""

for i in range(len(temporary) -1, -1, -1):
    kalimat_terbalik += temporary[i] + ' '
print(f"Kalimat Terbalik: {kalimat_terbalik}")


huruf_vokal = ['a', 'i', 'u', 'e', 'o']
counter_huruf_vokal = 0
for i in kalimat_terbalik:
    if i in huruf_vokal:
        counter_huruf_vokal += 1
print(f"Huruf vokal yang terdapat dalam kalimat: {counter_huruf_vokal}")

"""
1. Menampilkan teks kegunaan program kepada pengguna
3. Deklarasi variabel "kalimat_masukan" yang menerima input string dari pengguna dan ditampilkan "Masukkan kalimat" ":" pada konsol
4. Deklarasi variabel "temporary" yang memisah string didalam variabel "kalimat_masukan" tiap kali ditemukan spasi dengan menggunakan fungsi .split()
5. Deklarasi variabel "kalimat_terbalik dengan nilai string kosong

7. Perulangan for yang mengiterasi jumlah variabel "temporary" - 1, sampai nilai - 1, dan langkah iterasi -1
8. Tambah variabel "kalimat_terbalik" dengan nilai temporary pada index sesuai dengan nilai iterator "i" dan ditambah dengan ' ' (spasi)
9. Tampilkan  format string "Kalimat Terbalik: " diikuti dengan nilai variabel "kalimat_terbalik" kepada pengguna

12. Deklarasi list "huruf_vokal" dengan nilai string huruf - huruf vokal
13. Deklarasi variabel "counter_huruf_vokal" dengan nilai default 0
14. Perulangan for yang mengiterasi nilai variabel "kalimat_terbalik"
15 - 16. Eksekusi kondisional dengan kondisi apabila nilai iterator "i" terdapat didalam list "huruf_vokal" tambahkan nilai "counter_huruf_vokal" dengan 1 
17. Tampilkan nilai variabel "counter_huruf_vokal" yang menghitung jumlah huruf vokal dari kalimat masukan pengguna

"""
