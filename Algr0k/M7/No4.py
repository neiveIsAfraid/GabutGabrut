pemetaan = ["dibagi", "dikali", "dikurang","dikurangi", "ditambah", "adalah", "berapa"]
masukan_pengguna = ""
print("\n\nProgram evaluasi aritmatika sederhana\n\nMasukanlah ekspresi yang ingin dievaluasi")
while masukan_pengguna != "selesai":
    masukan_pengguna = input(": ")
    temporary = []
    for i in masukan_pengguna.split(" "):
        if i in pemetaan:
            continue
        else:
            temporary.append(int(i))

    for i in masukan_pengguna.split(" "):
        if i == "ditambah":
            print(f"{temporary[0] + temporary[1] }")
        elif i == "dikurang":
            print(f"{temporary[0] - temporary[1] }")
        elif i == "dikali":
            print(f"{temporary[0] * temporary[1] }")
        elif i == "dibagi":
            print(f"{temporary[0] / temporary[1] }") 


"""
1. Deklarasi list "pemetaan" yang berisi kata kunci untuk operasi aritmatika sederhana
2. Deklarasi variabel "masukan_pengguna" yang bernilai string kosong 
3. Tampilkan fungsionalitas program kepada pengguna
4. Perulangan while dengan kondisi selama variabel "masukan_pengguna" tidak bernilai "selesai", eksekusi blok kode berikut
5. Minta input bertipe data string kepada pengguna dan masukkan kedalam variabel "masukan_pengguna" 
6. Deklarasi list kosong dengan nama variabel "temporary"
7. Perulangan for yang mengiterasi nilai variabel "masukan_pengguna" yang dipisah tiap ditemukan adanya spasi dengan method .split()
8 - 9. Eksekusi kondisional dengan kondisi bila iterator "i" terdapat didalam list "pemetaan" lanjutkan program
10 - 11. Eksekusi kondisional else, jika kondisi if tidak terpenuhi tambahkan nilai iterator "i" kedalam list "temporary" dengan method .append()

13. Perulangan for yang mengiterasi nilai "masukan_pengguna" yang dipisah tiap ditemukan adanya spasi dengan method .split()
14. Eksekusi kondisional jika nilai iterator "i" sama dengan "ditambah", tampilkan hasil berupa nilai list temporary pada index 0 ditambahkan dengan nilai list temporary pada index 1
15. Eksekusi kondisional jika nilai iterator "i" sama dengan "dikurang", tampilkan hasil berupa nilai list temporary pada index 0 dikurangi dengan nilai list temporary pada index 1
16. Eksekusi kondisional jika nilai iterator "i" sama dengan "dikali", tampilkan hasil berupa nilai list temporary pada index 0 dikalikan dengan nilai list temporary pada index 1
17. Eksekusi kondisional jika nilai iterator "i" sama dengan "dibagi", tampilkan hasil berupa nilai list temporary pada index 0 dibagi dengan nilai list temporary pada index 1
"""

"""
