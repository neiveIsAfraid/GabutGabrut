kodon_dan_protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", 
    "UUC": "Phenylalanine",
    "UUA": "Leucine", 
    "UUG": "Leucine",
    "UCU": "Serine", 
    "UCC": "Serine", 
    "UCA": "Serine", 
    "UCG": "Serine",
    "UAU": "Tyrosine", 
    "UAC": "Tyrosine",
    "UGU": "Cysteine", 
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", 
    "UAG": "STOP", 
    "UGA": "STOP"
}

masukan_pengguna = input("Masukkan kodon: ")
masukan = [] 
terjemahan = []

for i in range(0, len(masukan_pengguna), 3):
    masukan.append(masukan_pengguna[i:i+3])

for i in masukan:
    temporary = kodon_dan_protein.get(i, '')
    if temporary == "STOP":
        break
    terjemahan.append(temporary)

masukan_tampilan = ""
counter = 0
for i in masukan:
    if len(masukan) - counter == 1:
        masukan_tampilan += f"{i}"
    else:
        masukan_tampilan += f"{i}, "
        counter += 1

terjemahan_tampilan = ""
counter = 0
for i in terjemahan:
    if len(terjemahan) - counter == 1:
        terjemahan_tampilan += f"{i}"
    else:
        terjemahan_tampilan += f"{i}, "
        counter += 1

print(f"Kodon yang dimasukkan: |{masukan_tampilan}| yang menjadi polipeptida dengan urutan sebagai berikut\nProtein: {terjemahan_tampilan}")

"""
1 - 19. Deklarasi dictionary yang menyimpan data kodon dan protein
21. Deklarasi variabel "masukan_pengguna" yang menerima input berupa string RNA yang ingin diterjemahkan dari pengguna
22. Deklarasi variabel "masukan" yang memiliki nilai default string kosong
23. Deklarasi variabel "terjemahan" yang memiliki nilai default string kosong

25. Perulangan for yang mengiterasi jumlah karakter dalam variabel "masukan_pengguna" dengan iterasi tiap 3 langkah 
26. tambahkan string yang terdapat pada variabel "masukan_pengguna" di index nilai iterator "i" sampai "i+3" kedalam list masukan
28. Perulangan for yang mengiterasi list masukan
29. Deklarasi variabel temporary yang bernilai value dari dictionary "kodon_dan_protein" pada key sesuai dengan iterator "i"
30 - 31. Eksekusi kondisional dengan kondisi bila nilai variabel "temporary" sama dengan == "STOP", hentikan perulangan
32. Tambahkan nilai dari variabel "temporary" kedalam list "terjemahan"

34. Deklarasi variabel "masukan_tampilan" dengan nilai string kosong
35. Deklarasi variabel "counter" dengan nilai default 0
36. Perulangan for yang mengiterasi variabel "masukan"
37. Eksekusi kondisional dengan kondisi bila nilai jumlah variabel "masukan" dikurangi variabel  "counter" sama dengan 1, eksekusi blok kode berikut
38. Tambahkan nilai variabel "masukan_tampilan" dengan nilai iterator "i"
39. Eksekusi kondisional else, Tambahkan nilai variabel "masukan_tampilan" dengan nilai iterator "i" dan ',' (koma), Kemudian tambahkan nilai variabel "counter" dengan 1

43. Deklarasi variabel "terjemahan_tampilan" dengan nilai string kosong
44. Deklarasi ulang variabel "counter" dengan nilai default 0
45. Perulangan for yang mengiterasi nilai variabel "terjemahan"
46. Eksekusi kondisional dengan kondisi bila nilai jumlah variabel "terjemahan" dikurangi variabel  "counter" sama dengan 1, eksekusi blok kode berikut
47. Tambahkan nilai variabel "terjemahan_tampilan" dengan nilai iterator "i"
48 - 50. Eksekusi kondisional else, Tambahkan nilai variabel "terjemahan_tampilan" dengan nilai iterator "i" dan',' (koma), Kemudian tambahkan nilai variabel "counter" dengan 1
52. Tampilkan hasil pemisahan kodon yang terdapat pada variabel "masukan_tampilan" dan hasil translasi yang terdapat pada variabel "terjemahan_tampilan" kepada pengguna 
"""
