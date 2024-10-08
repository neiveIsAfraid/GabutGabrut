pilihan = 0
pilihan2 = 0
hasil_kali = []
while pilihan != 4:
    pilihan = int(input("\n1. Buat matriks\n2. Tampilkan matriks\n3. Kalikan matriks\n4. Keluar\n: "))
    if pilihan == 1:
        pilihan2 = int(input("\nBuat Matriks (1/2)\n: "))
        if pilihan2 == 1:
            print("\nMatriks", 1)
            row_1 = int(input("Baris matriks: "))
            column_1 = int(input("Kolom matriks: ")) 
            matrix1 = []
            for i in range(row_1):
                matrix1.append([])
                for j in range(column_1):
                    matrix1[i].append(0)
            for i in range(len(matrix1)):
                for j in range(len(matrix1[i])):
                    matrix1[i][j] = int(input(f"matriks[{i}][{j}]: {matrix1[i][j]}: "))
        
        elif pilihan2 == 2:
            print("\nMatriks",2)
            row_2 = int(input("Baris matriks: "))
            column_2 = int(input("Kolom matriks: ")) 
            matrix2 = []
            for i in range(row_2):
                matrix2.append([])
                for j in range(column_2):
                    matrix2[i].append(0)
            for i in range(len(matrix2)):
                for j in range(len(matrix2[i])):
                    matrix2[i][j] = int(input(f"matriks[{i}][{j}]: {matrix2[i][j]}: "))  
    
    elif pilihan == 2:
        pilihan2 = int(input("\nTampilkan matriks (1/2): "))
        if pilihan2 == 1:
            for i in range(len(matrix1)):
                print(matrix1[i])
        elif pilihan2 == 2 :
            for i in range(len(matrix2)):
                print(matrix2[i])

    elif pilihan == 3:
        for i in range(column_2):
            hasil_kali.append([])
            for j in range(row_1):
               hasil_kali[i].append(0)
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    hasil_kali[i][j] += matrix1[i][k] * matrix2[k][j]
        for i in range(len(hasil_kali)):
            print(hasil_kali[i])
        hasil_kali = []


"""
1. Deklarasi variabel "pilihan" dengan nilai default 0
2. Deklarasi variabel "pilihan2" dengan nilai default 0
3. Deklarasi variabel "hasil_kali" dengan nilai list kosong
4. perulangan while dengan kondisi bila nilai variabel pilihan tidak sama dengan 4 eksekusi blok kode berikut

5. Tampilkan pilihan menu program untuk membuat matriks, menampilkan matriks, mengalikan matriks atau keluar dari program dan masukan pilihan pengguna kedalam variabel "pilihan" bertipe data integer
6. eksekusi kondisional bila variabel "pilihan" bernilai sama dengan 1, eksekusi blok kode berikut
7. Tampilkan pilihan menu untuk membuat matriks 1 atau 2 dan masukan pilihan pengguna kedalam variabel "pilihan2" dengan tipe data integer
8. eksekusi kondisional bila variabel "pilihan" bernilai sama dengan 1, eksekusi blok kode berikut
9. Tampilan menu "Matriks 1"
10. Deklarasi variabel "row_1" dengan nilai masukan pengguna bertipe data integer 
11. Deklarasi variabel "column_1" dengan nilai masukan pengguna bertipe data integer
12. Deklarasi variabel "matrix1" dengan nilai list kosong 
13. Perulangan for dengan iterable nilai dari variabel "row_1" menggunakan iterator i
14. Tambahkan "[]" pada setiap iterasi kedalam list "matrix1"
15. perulangan for didalam perulangan for dengan nilai iterable dari variabel "column_1" menggunakan iterator j
16. Tambahkan 0 ke list "matrix1" pada index iterator i
17. Perulangan for dengan nilai iterable jumlah item pada list "matrix1" dengan iterator i
18. Perulangan for dalam perulangan for dengan iterator "j", nilai iterable perulagan ini menggunakan jumlah item pada list "matrix1" pada index sesuai dengan iterator "i"
19. Masukkan masukan pengguna yang bertipe data integer kedalam list "matrix1" pada index "i" dan "j" dan tampilkan string "matriks" pada index "i""j": nilai dari "matrix1" pada index "i""j" sebagai pedoman pengguna dalam memasukan nilai
21. eksekusi kondisional bila variabel "pilihan" bernilai sama dengan 2, eksekusi blok kode berikut
22. Tampilan menu "Matriks 1"
23. Deklarasi variabel "row_2" dengan nilai masukan pengguna bertipe data integer
24. Deklarasi variabel "column_2" dengan nilai masukan pengguna bertipe data integer
25. Deklarasi variabel "matrix2" dengan nilai list kosong 
26. Perulangan for dengan iterable nilai dari variabel "row_2" menggunakan iterator i
27. Tambahkan "[]" kedalam list "matrix2" pada setiap iterasi 
28. perulangan for didalam perulangan for dengan nilai iterable dari variabel "column_2" menggunakan iterator "j"
29. Tambahkan 0 ke list "matrix2" pada index iterator "i"
30. Perulangan for dengan nilai iterable jumlah item pada list "matrix2" dengan iterator i
31. Perulangan for dalam perulangan for dengan iterator "j", nilai iterable perulagan ini menggunakan jumlah item pada list "matrix2" pada index sesuai dengan iterator "i"
32. Masukkan masukan pengguna yang bertipe data integer kedalam list "matrix1" pada index "i" dan "j" dan tampilkan string "matriks" pada index "i""j": nilai dari "matrix1" pada index "i""j" sebagai pedoman pengguna dalam memasukan nilai

34. eksekusi kondisional dengan kondisi bila nilai variabel "pilihan" sama dengan 2 eksekusi blok kode berikut
35. Tampilkan pilihan menu untuk menampilkan matriks 1 atau 2 dan masukan pilihan pengguna kedalam variabel "pilihan2" dengan tipe data integer
36. Eksekusi kondisional dengan kondisi jika nilai variabel "pilihan2" sama dengan 1, eksekusi blok kode berikut
37. perulangan for yang mengiterasi nilai jumlah item pada list "matrix1" dengan iterator i
38. Tampilkan nilai "matrix1" pada index sesuai dengan nilai iterator "i"
39. Eksekusi kondisional dengan kondisi jika nilai variabel "pilihan2" sama dengan 2, eksekusi blok kode berikut
40. perulangan for yang mengiterasi nilai jumlah item pada list "matrix2" dengan iterator i
41. Tampilkan nilai "matrix2" pada index sesuai dengan nilai iterator "i"

43. eksekusi kondisional dengan kondisi bila variabel "pilihan" bernilai sama dengan 3 eksekusi blok kode berikut
44. Perulangan for dengan mengiterasi nilai variabel "column_2" menggunakan iterator "i"
45. Tambahkan list kosong "[]" tiap kali iterasi
46. Perulangan for didalam perulangan for dengan mengiterasi nilai variabel "row_1" menggunakan iterator "j"
47. Masukkan 0 kedalam list "hasil_kali" pada index nilai dari iterator "i"
48. perulagan for dengan mengiterasi nilai jumlah dari item list "matrix1" menggunakan iterator "i"
49. perulangan for didalam perulangan for dengan mengiterasi nilai jumlah dari item list "matrix2" yang terdapat pada index 0 menggunakan nilai dari iterator "j"
50. perulangan for bertingkat 3 kali yang mengiterasi nilai jumlah dari item list "matrix2" menggunakan iterator "k"
51. Ubah nilai list "hasil_kali" pada index "i" dan "j" dengan ditambah nilai hasil kali dari nilai list "matrix1" pada index "i" dan "k" dengan nilai list "matrix2" pada index nilai dari iterator "k" dan nilai dari iterator "j"
52. Perulangan for yang mengiterasi nilai jumlah item pada list "hasil_kali" menggunakan iterator "i"
53. Tampilkan nilai list "hasil_kali" pada index nilai dari iterator "i"
54. Reset nilai list "hasil_kali" dengan string kosong
"""
