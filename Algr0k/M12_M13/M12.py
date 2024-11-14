from PyQt5.QtWidgets import *

def tambah_barang():
    nama = nama_masukan.text()
    harga = harga_masukan.text()
    if nama and harga:
        data_barang.append((nama, harga))
        update_table()
        nama_masukan.clear()
        harga_masukan.clear()
    else:
        QMessageBox.warning(window, "Input Error", "Nama dan Harga harus diisi!")

def update_table():
    table.setRowCount(0)
    for barang in data_barang:
        posisi_baris = table.rowCount()
        table.insertRow(posisi_baris)
        table.setItem(posisi_baris, 0, QTableWidgetItem(barang[0]))
        table.setItem(posisi_baris, 1, QTableWidgetItem(barang[1]))

def edit_barang():
    tabel_pilihan = table.currentRow()
    if tabel_pilihan >= 0:
        nama = nama_masukan.text()
        harga = harga_masukan.text()
        if nama and harga:
            data_barang[tabel_pilihan] = (nama, harga)
            update_table()
            nama_masukan.clear()
            harga_masukan.clear()
        else:
            QMessageBox.warning(window, "Input Error", "Nama dan Harga harus diisi!")
    else:
        QMessageBox.warning(window, "Edit Error", "Silakan pilih baris yang ingin diedit.")

def hapus_barang():
    tabel_pilihan = table.currentRow()
    if tabel_pilihan >= 0:
        del data_barang[tabel_pilihan]
        update_table()
    else:
        QMessageBox.warning(window, "Delete Error", "Silakan pilih baris yang ingin dihapus.")

app = QApplication([])
data_barang = []
window = QWidget()
window.setWindowTitle("Aplikasi Inventaris Barang")
window.setGeometry(100, 100, 600, 400)
label_nama = QLabel("Nama Barang:", window)
label_nama.setGeometry(20, 20, 100, 30)
nama_masukan = QLineEdit(window)
nama_masukan.setGeometry(120, 20, 400, 30)
label_harga = QLabel("Harga:", window)
label_harga.setGeometry(20, 60, 100, 30)
harga_masukan = QLineEdit(window)
harga_masukan.setGeometry(120, 60, 400, 30)
button_tambah = QPushButton("Tambah", window)
button_tambah.setGeometry(20, 100, 150, 30)
button_edit = QPushButton("Edit", window)
button_edit.setGeometry(195, 100, 150, 30)
button_hapus = QPushButton("Hapus", window)
button_hapus.setGeometry(370, 100, 150, 30)
table = QTableWidget(window)
table.setColumnCount(2)
table.setHorizontalHeaderLabels(["Nama Barang", "Harga"])
table.setGeometry(20, 150, 560, 200)
table.setColumnWidth(0, 280)
table.setColumnWidth(1, 280)
button_tambah.clicked.connect(tambah_barang)
button_edit.clicked.connect(edit_barang)
button_hapus.clicked.connect(hapus_barang)
window.show()
app.exec()

"""
Pembahasan M12
1. Impor modul QtWidgets yang digunakan untuk keperluan GUI (Graphical User Interface)
3. Deklarasi fungsi "tambah_barang"
4. Deklarasi variabel "nama" yang menyimpan data dari kotak teks "nama_masukan" sebagai nama barang bertipe data string
5. Deklarasi variabel "harga" yang menyimpan data dari kotak teks "harga_masukan" sebagai harga barang bertipe data string
6. Eksekusi kondisional dengan kondisi apabila data pada variabel "nama" dan "harga" tidak kosong, eksekusi blok kode berikut ini 
7. Tambahkan data dari variabel "nama" dan "harga" sebagai list kepada list "data_barang"
8. Panggil fungsi "update_table()" yang digunakan untuk memperbarui tampilan 
9. Bersihkan kolom "nama_masukan" pada tampilan 
10. Bersihkan kolom "harga_masukan" pada tampilan
11 - 12. Kondisi kondisional jika kondisi pada pernyataan if tidak terpenuhi, tampilkan kotak pesan kepada pengguna yang menyatakan "Nama dan harga harus diisi" kotak bertipe warning atau peringatan

14. Deklarasi fungsi "update_table()" yang digunakan untuk memperbarui tampilan tabel
15. Reset tampilan baris untuk menampilkan data yang diperbarui
16. Perulangan for yang digunakan untuk mengiterasi nilai list "data_barang" dengan iterator "barang"
17. deklarasi variabel "posisi_baris" yang berisi nilai jumlah total baris pada tabel 
18. Tambahkan baris baru pada tabel dengan method "insertRow" dengan nilai dari variabel "posisi_baris"
19-20. isi item pada tabel dengan data pada list "barang" yang berisi nama barang dan harga barang

22. Deklarasi fungsi "edit_barang"
23. Deklasi variabel "tabel_pilihan" yang memiliki nilai keluaran method currentRow berupa index baris yang dipilih pengguna
24. Eksekusi kondisional yang memiliki kondisi jika "tabel_pilihan" lebih dari sama dengan 0 yang menandakan terdapat baris yang dipilih 
25. Dekalarsi variabel "nama" yang menyimpan data dari kolom teks "nama_masukan"
26. Dekalarsi variabel "harga" yang menyimpan data dari kolom teks "harga_masukan"
27. eksekusi kondisional ketika variabel nama dan harga memiliki sebuah nilai, eksekusi blok kode berikut
28. Isi list data barang pada indeks yang sesuai dengan nilai dari variabel "tabel_pilihan" dengan variabel "nama" dan "harga" sebagai sebuah list
29. panggil variabel "update_table" yang memperbarui tampilan tabel
30. Kosongkan kolom teks "nama_masukan" dengan method clear
31. Kosongkan kolom teks "harga_masukan" dengan method clear
32 - 33. Eksekusi kondisional else, bila variabel nama dan harga tidak memiliki nilai, tampilkan kepada pengguna kotak pesan peringatan bahwa input error dan pesan "Nama dan harga harus diisi"
34 - 35. Eksekusi kondisional else dengan kondisi bila pada variabel "tabel_pilihan" pengguna tidak memilih tabel yang ingin diedit, maka tampilkan kepada pengguna  kotak pesan peringatan bahwa Edit error dan pesan "Silahkan pilih baris yang ingin di edit"

37. Deklarasi fungsi "hapus_barang" untuk menghapus data pada tabel
38. deklarasi variabel "tabel_pilihan" dengan isi variabel berupa indeks dari baris tabel yang dipilih pengguna
39. eksekusi kondisional dengan kondisi bila nilai dari variabel "tabel_pilihan" lebih dari sama dengan 0 yang menandakan terdapat sebuah baris yang dipilih oleh pengguna
40. gunakan fungsi del untuk menghapus nilai dari data barang pada index sesuai dengan nilai variabel "tabel_pilihan"
41. Panggil fungsi "update_table" untuk memperbarui tampilan tabel
42. eksekusi kondisional else yang akan dieksekusi bila pengguna tidak memilih sebuah tabel terlebih dahulu, maka tampilkan kepada pengguna kotak pesan peringatan bahwa Delete error dan pesan "Silahkan pilih baris yang ingin di hapus"

45. Inisialisasi "QApplication" kedalam variabel objek "app" yang digunakan sebagai permulaan aplikasi
46. Deklarasi variabel "data_barang " yang merupakan tipe data list
47. Deklarasi variabel "window" yang merupakan objek dari kelas "QWidget"
48. Merubah judul program yang ditampilkan kepada pengguna dengan "Aplikasi Inventaris Barang"
49. Mengatur ukuran dari tampilan utama program dengan method "setGeometry"

50. Deklarasi variabel "label_nama" yang merupakan objek dari "QLabel" yang menampilkan teks berupa "Nama Barang: " yang digunakan untuk memberi tahu pengguna bahwa kolom disebelahnya merupakan tempat untuk memasukkan nama barang yang ingin di input, objek ini memiliki parent class yaitu "window"
51. Atur ukuran objek "label_nama" dengan method setGeometry untuk mengatur tata letak dan ukuran objek
52. Deklarasi variabel "nama_masukan" yang merupakan objek dari "QLineEdit" yang merupakan kolom untuk memasukkan nama barang yang ingin di input, objek ini memiliki parent class yaitu "window"
53. Atur ukuran objek "nama_masukan" dengan method setGeometry untuk mengatur tata letak dan ukuran objek

54. Deklarasi variabel "label_harga" yang merupakan objek dari "QLabel" yang menampilkan teks berupa "Harga Barang: " yang digunakan untuk memberi tahu pengguna bahwa kolom disebelahnya merupakan tempat untuk memasukkan harga barang yang ingin di input, objek ini memiliki parent class yaitu "window"
55. Atur ukuran objek "label_harga" dengan method setGeometry untuk mengatur tata letak dan ukuran objek
56. Deklarasi variabel "harga_masukan" yang merupakan objek dari "QLineEdit" yang merupakan kolom untuk memasukkan harga barang yang ingin di input, objek ini memiliki parent class yaitu "window"
57. Atur ukuran objek "harga_masukan" dengan method setGeometry untuk mengatur tata letak dan ukuran objek
58. Deklarasi "button_tambah" yang merupakan objek dari kelas "QPushButton" dan memiliki parent class yaitu "window", sebuah tombol dengan tulisan "Tambah"
59. Atur ukuran objek "button_tambah" dengan method setGeometry untuk mengatur tata letak dan ukuran objek
60. Deklarasi "button_edit" yang merupakan objek dari kelas "QPushButton" dan memiliki parent class yaitu "window", sebuah tombol dengan tulisan "Edit"
61. Atur ukuran objek "button_edit" dengan method setGeometry untuk mengatur tata letak dan ukuran objek
62. Deklarasi "button_hapus" yang merupakan objek dari kelas "QPushButton" dan memiliki parent class yaitu "window", sebuah tombol dengan tulisan "Hapus"
63. Atur ukuran objek "button_hapus" dengan method setGeometry untuk mengatur tata letak dan ukuran objek
64. Deklarasi variabel "table" yang merupakan objek dari "QTableWidget" 
65. Atur kolom pada "table" agar memiliki 2 kolom dengan method "setColumnCount" pada objek "table"
66. Beri nama pada judul masing masing kolom dengan "Nama Barang" dan "Harga"
67. Atur ukuran "table" dengan method setGeometry untuk mengatur tata letak dan ukuran tabel
68. Atur lebar kolom pertama pada tabel menjadi 290
69. Atur lebar kolom kedua pada tabel menjadi 290
70. Hubungkan tombol "button_tambah" dengan fungsi "tambah_barang", agar saat tombol tambah dipencet program tahu apa yang harus dilakukan
71. Hubungkan tombol "button_edit" dengan fungsi "edit_barang", agar saat tombol edit dipencet program tahu apa yang harus dilakukan
72. Hubungkan tombol "button_hapus" dengan fungsi "hapus_barang", agar saat tombol hapus dipencet program tahu apa yang harus dilakukan
73. Tampilkan window dengan method "show" untuk tampilan GUI
74. Inisiasi aplikasi yang sudah dibuat
"""
