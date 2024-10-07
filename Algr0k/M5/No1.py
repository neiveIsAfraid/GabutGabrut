pilihan = 0
matrix = []
while pilihan != 4:
    pilihan = int(input("\n\n===Matrix Creation===\n\n1.Create Matrix\n2.Change Matrix Value\n3.Show Matrix\n4.Exit\n: "))
    if pilihan == 1:    
        print("\nHow Many will your matrix have")
        row_1 = int(input("row: "))
        column_1 = int(input("column: ")) 
        matrix = []
        for i in range(row_1):
            matrix.append([])
            for j in range(column_1):
                matrix[i].append(0)
        for i in range(row_1):
            print(matrix[i])
    
    elif pilihan == 2:
        if not matrix:
            print("\033[31mCreate the matrix first!!!\033[0m")
            input("(press enter): ")
            continue
        pilihan_2 = int(input("1. Change the matrix in order\n2.Change matrix specifically\n: "))
        if pilihan_2 == 1:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    matrix[i][j] = int(input(f"matrix[{i}][{j}]: {matrix[i][j]}: "))

        elif pilihan_2 == 2:
            row_2 = int(input("Row: "))
            column_2 = int(input("Column: "))
            value = int(input("Value: "))
            matrix[row_2][column_2] = value
            
        
    elif pilihan == 3:
        for i in range(row_1):
            print(matrix[i])


"""
1. Deklarasi variabel "pilihan" dengan nilai default 0
2. Deklarasi variabel "matrix" dengan tipe data list yang kosong
3. Deklarasi perulangan while untuk  mengulang program secara terus menerus
4. membuat variabel pilihan yang menerima masukan menu dari pengguna
5. Eksekusi kondisional dengan kondisi jika variabel "pilihan" bernilai sama dengan 1, eksekusi blok kode berikut
6. Tampilkan introduksi program dan opsi pilihan menu
7. Deklarasi variabel "row_1" dengan masukan pengguna berupa jumlah baris matrix yang diinginkan
8. Deklarasi variabel "column_1" dengan masukan pengguna berupa jumlah kolom matrix yang diinginkan
9. Buat variabel "Matrix" dengan nilai tipe data berupa list kosong
10. Buat perulangan for yang mengiterasi nilai variabel "row_1" menggunakan fungsi range
11. tambahkan list kosong tiap iterasi perulangan kedalam list "matrix"
12. Perulangan for didalam perulangan for yang mengiterasi nilai variabel "column_1" menggunakan fungsi range
13. Tambahkan nilai 0 untuk semua index didalam matrix
14 - 15. Perulangan for yang mengiterasi nilai variabel "row_1" menggunakan fungsi range untuk menampilkan matrix 
17. Eksekusi kondisional, ketika pilihan bernilai sama dengan 2, eksekusi blok kode berikut
18 - 21. eksekusi kondisional, jika matrix belum dibuat, tampilkan "Create matrix first" dengan teks berwarna merah, dan tekan enter untuk melanjutkan
22. Buat variabel "pilihan_2" dengan nilai masukan dari pengguna dengan tipe data integer
23. Kondisi eksekusional, jika nilai variabel "pilihan_2" sama dengan 1 eksekusi blok kode berikut
24. Buat perulangan for yang mengiterasi jumlah item dalam list "matrix" menggunakan fungsi range dengan iterator "i"
25. Buat perulangan for didalam perulangan for yang mengiterasi jumlah item dalam list "matrix" menggunakan fungsi range dengan iterator "j"
26. Masukan nilai ke list "matrix" pada index sesuai nilai dari iterator "i" untuk baris dan "j" untuk kolom menggunakan fungsi input
28. Kondisi eksekusional jika nilai dari "variabel_2" sama dengan 2, eksekusi blok kode berikut
29. deklarasi variabel "row_2" dengan nilai masukan pengguna dan bertipe data integer
30. deklarasi variabel "column_2" dengan nilai masukan pengguna dan bertipe data integer
31. deklarasi variabel "value" dengan nilai masukan pengguna bertipe data integer
32. ubah nilai list "matrix" dengan nilai dari variabel "value" pada index sesuai dengan variabel "row_2" dan "column_2"
35. kondisi eksekusional jika nilai dari variabel "pilihan" sama dengan 3, eksekusi blok kode berikut
36. Perulangan for dengan mengiterasi nilai dari variabel "row_1" dengan iterator "i"
37. tampilkan nilai dari list "matrix" index sesuai dengan nilai dari iterator "i"
"""
