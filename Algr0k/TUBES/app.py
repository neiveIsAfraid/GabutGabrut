import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate

def menu_login_tampilan():
    dialog = QDialog()
    dialog.setWindowTitle("Login")
    dialog.setGeometry(600, 300, 300, 150)
    dialog.setStyleSheet("background-color: white;")
    layout = QVBoxLayout(dialog)

    input_username = QLineEdit()
    input_username.setPlaceholderText("Masukkan Username")
    layout.addWidget(input_username)

    input_password = QLineEdit()
    input_password.setPlaceholderText("Masukkan Password")
    input_password.setEchoMode(QLineEdit.Password)
    layout.addWidget(input_password)

    tombol_login = QPushButton("Login")
    tombol_login.setStyleSheet("background-color: #4CAF50; color: white;")
    layout.addWidget(tombol_login)

    tombol_register = QPushButton("Register")
    tombol_register.setStyleSheet("background-color: #2196F3; color: white;")
    layout.addWidget(tombol_register)
    def login():
        global berkas_pengguna
        username = input_username.text()
        password = input_password.text()
        if validasi_login(username, password):
            dialog.accept()
            berkas_pengguna = username
        else:   
           QMessageBox.warning(dialog, "Login Gagal", "Username atau Password salah.")
        
    def validasi_login(username, password):
        with open('user.csv', "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
                    
    def register():
        username = input_username.text()
        password = input_password.text()
        if register_user(username, password):
            QMessageBox.information(dialog, "Register Berhasil", "Berhasil !!! Silahkan login dengan username dan password.")
        else:
            QMessageBox.warning(dialog, "Register Gagal", "Username tersebut telah digunakan.")
    
    def register_user(username, password):
        with open('user.csv', "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    return False

        with open('user.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        return True
    
    tombol_login.clicked.connect(login)
    tombol_register.clicked.connect(register)
    if dialog.exec() == QDialog.Accepted:
        return True
    
def setup_ui():
    global laman_anggaran, transaksi, total_pengeluaran_harian_teks, total_pengeluaran_mingguan_teks, total_pengeluaran_bulanan_teks, tabel_laporan, combo_periode_anggaran, input_mulai_anggaran, input_akhir_anggaran, input_nominal_anggaran, input_kategori_anggaran, tabel_anggaran, total_pengeluaran_teks, combo_periode, filter_tanggal_input, tabel, filter_combo, laman_transaksi, tab_widget, laman_transaksi, input_deskripsi, input_kategori, input_nominal, input_tanggal

    window = QWidget()
    window.setWindowTitle("CashTrack")
    window.setGeometry(100, 100, 1000, 800)
    tab_widget = QTabWidget(window)
    
    laman_transaksi = QWidget()
    layout_utama_transaksi = QVBoxLayout()
    layout_tombol = QHBoxLayout()
    layout_filter = QHBoxLayout()
    layout_input = QHBoxLayout()

    input_tanggal = QDateEdit()
    input_tanggal.setDisplayFormat("dd-MM-yyyy")
    input_tanggal.setDate(QDate.currentDate())
    input_tanggal.setCalendarPopup(True)
    layout_input.addWidget(input_tanggal)

    input_deskripsi = QLineEdit()
    input_deskripsi.setPlaceholderText("Deskripsi")
    layout_input.addWidget(input_deskripsi)

    input_kategori = QLineEdit()
    input_kategori.setPlaceholderText("Kategori")
    layout_input.addWidget(input_kategori)

    input_nominal = QLineEdit()
    input_nominal.setPlaceholderText("Nominal")
    layout_input.addWidget(input_nominal)

    layout_utama_transaksi.addLayout(layout_input)

    tombol_tambah = QPushButton("Tambah Transaksi")
    tombol_tambah.setStyleSheet("background-color: #4CAF50; color: white;")
    tombol_tambah.clicked.connect(tambah_transaksi)
    layout_tombol.addWidget(tombol_tambah)

    tombol_edit = QPushButton("Edit Transaksi")
    tombol_edit.setStyleSheet("background-color: #4CAF50; color: white;")
    tombol_edit.clicked.connect(edit_transaksi)
    layout_tombol.addWidget(tombol_edit)
    
    tombol_delete = QPushButton('Hapus Transaksi')
    tombol_delete.setStyleSheet("background-color: #F44336; color: white;")
    tombol_delete.clicked.connect(hapus_transaksi)
    layout_tombol.addWidget(tombol_delete)
    layout_utama_transaksi.addLayout(layout_tombol)

    filter_combo = QComboBox()
    filter_combo.setFixedWidth(200)

    filter_combo.addItem("Tampilkan Semua")
    filter_combo.currentIndexChanged.connect(filter_transaksi)
    layout_filter.addWidget(filter_combo)

    filter_tanggal_input = QLineEdit()
    filter_tanggal_input.setPlaceholderText('Filter Tanggal')
    filter_tanggal_input.textChanged.connect(filter_tanggal_transaksi)
    layout_filter.addWidget(filter_tanggal_input)
    layout_utama_transaksi.addLayout(layout_filter)

    tabel = QTableWidget()
    tabel.setColumnCount(4)
    tabel.setHorizontalHeaderLabels(['Tanggal', 'Deskripsi', 'Kategori', 'Nominal'])
    tabel.setColumnWidth(0, 150)
    tabel.setColumnWidth(1, 540)
    tabel.setColumnWidth(2, 150)
    layout_utama_transaksi.addWidget(tabel)
    laman_transaksi.setLayout(layout_utama_transaksi)

    laman_beranda = QWidget()


    teks_akun = QLabel(f"Akun: {berkas_pengguna}", laman_beranda)
    teks_akun.setStyleSheet("font-size: 20px; ")
    teks_akun.setGeometry(30,0,500,100)

    total_pengeluaran_harian_teks = QLabel("Pengeluaran Hari Ini: ", laman_beranda)
    total_pengeluaran_harian_teks.setStyleSheet("font-size: 20px; ")
    total_pengeluaran_harian_teks.setGeometry(30,50,500,100)

    total_pengeluaran_mingguan_teks = QLabel("Pengeluaran Minggu Ini: ", laman_beranda)
    total_pengeluaran_mingguan_teks.setStyleSheet("font-size: 20px;")
    total_pengeluaran_mingguan_teks.setGeometry(30,90,500,100)
    
    total_pengeluaran_bulanan_teks = QLabel("Pengeluaran Bulan Ini: ", laman_beranda)
    total_pengeluaran_bulanan_teks.setStyleSheet("font-size: 20px;")
    total_pengeluaran_bulanan_teks.setGeometry(30,130,500,100)
    
    tombol_pengeluaran_total = QPushButton("Tampilkan Pengeluaran", laman_beranda)
    tombol_pengeluaran_total.clicked.connect(tampilkan_total_pengeluaran)
    tombol_pengeluaran_total.setStyleSheet("background-color: #2196F3; color: white; font-size: 20px;")
    tombol_pengeluaran_total.setGeometry(5,685,965,50)

    scroll_tips = QScrollArea(laman_beranda)
    scroll_tips.setWidgetResizable(True)
    scroll_tips.setGeometry(0,240, 975,400)
    scroll_tips.setStyleSheet("background-color: white;")

    scroll_content = QWidget()
    scroll_layout = QVBoxLayout(scroll_content)

    header_judul = QLabel("Artikel Artikel Keuangan Menarik")
    header_judul.setStyleSheet("font-size: 20px; font-weight:bold;")

    tautans = QTextBrowser(scroll_content)
    tautans.setOpenExternalLinks(True)
    tautans.append("""
                    <a href ='https://www.milestones.org/map/browse-articles/money-management-skills-for-young-adults' style="color:black;font-size:18px;">Money Management Skills for Young Adults</a> <br><br>
                    <a href ='https://www.manulife.co.id/id/artikel/tips-mengatur-keuangan-dengan-membuat-catatan-pengeluaran.html' style="color:black;font-size:18px;">Tips Mengatur Keuangan dengan Membuat Catatan Pengeluaran</a> <br><br>
                    <a href ='https://www.djkn.kemenkeu.go.id/kanwil-sumut/baca-artikel/14590/Pentingnya-Manajemen-Keuangan-dalam-Kehidupan-Sehari-Hari.html' style="color:black;font-size:18px;">Pentingnya Manajemen Keuangan dalam Kehidupan Sehari-Hari</a> <br><br>
                    <a href ='https://www.investopedia.com/articles/personal-finance/111813/five-rules-improve-your-financial-health.asp' style="color:black;font-size:18px;">5 Ways to Improve Your Financial Health</a> <br><br>
                    <a href='https://www.investopedia.com/how-to-create-a-budget-and-stop-wasting-money-8745869' style="color:black;font-size:18px;">Stop Wasting Money: How to Start a Budget and Stick To It</a> <br><br>
                    <a href='https://mediakeuangan.kemenkeu.go.id/article/show/7-tips-mengatur-keuangan-agar-tabunganmu-terus-bertambah' style="color:black;font-size:18px;">7 tips mengatur keuangan agar tabunganmu terus bertambah</a>
                  
                  """)

    scroll_layout.addWidget(header_judul)
    scroll_layout.addWidget(tautans)
    

    scroll_tips.setWidget(scroll_content)

    laman_anggaran = QWidget()
    layout_tanggal_anggaran = QHBoxLayout()
    layout_anggaran = QVBoxLayout()
    
    layout_tombol_anggaran = QHBoxLayout()
    layout_text_anggaran = QHBoxLayout()

    input_kategori_anggaran = QLineEdit()
    input_kategori_anggaran.setPlaceholderText("Kategori Anggaran")
    layout_anggaran.addWidget(input_kategori_anggaran)

    input_nominal_anggaran = QLineEdit()
    input_nominal_anggaran.setPlaceholderText("Nominal Anggaran")
    layout_anggaran.addWidget(input_nominal_anggaran)

    label_mulai = QLabel("Tanggal Mulai")
    label_mulai.setStyleSheet("font-weight: bold;")
    layout_text_anggaran.addWidget(label_mulai)
    
    label_akhir = QLabel("Tanggal Akhir")
    label_akhir.setStyleSheet("font-weight: bold;")
    layout_text_anggaran.addWidget(label_akhir)

    input_mulai_anggaran = QDateEdit()
    input_mulai_anggaran.setDisplayFormat("dd-MM-yyyy")
    input_mulai_anggaran.setDate(QDate.currentDate())
    input_mulai_anggaran.setCalendarPopup(True)
    layout_tanggal_anggaran.addWidget(input_mulai_anggaran)
    
    input_akhir_anggaran = QDateEdit()
    input_akhir_anggaran.setDisplayFormat("dd-MM-yyyy")
    input_akhir_anggaran.setDate(QDate.currentDate())
    input_akhir_anggaran.setCalendarPopup(True)
    layout_tanggal_anggaran.addWidget(input_akhir_anggaran)
    layout_anggaran.addLayout(layout_text_anggaran)
    layout_anggaran.addLayout(layout_tanggal_anggaran)

    combo_periode_anggaran = QComboBox()
    combo_periode_anggaran.addItems(["Harian", "Mingguan", "Bulanan"])
    layout_anggaran.addWidget(combo_periode_anggaran)
    
    tombol_tambah_anggaran = QPushButton('Tambah Anggaran')
    tombol_tambah_anggaran.setStyleSheet("background-color: #4CAF50; color: white;")
    tombol_tambah_anggaran.clicked.connect(tambah_anggaran)
    layout_tombol_anggaran.addWidget(tombol_tambah_anggaran)

    tombol_edit_anggaran = QPushButton('Edit Anggaran')
    tombol_edit_anggaran.setStyleSheet("background-color: #4CAF50; color: white;")
    tombol_edit_anggaran.clicked.connect(edit_anggaran)
    layout_tombol_anggaran.addWidget(tombol_edit_anggaran)

    tombol_delete_anggaran = QPushButton('Hapus Anggaran',)
    tombol_delete_anggaran.setStyleSheet("background-color: #F44336; color: white;")
    tombol_delete_anggaran.clicked.connect(delete_anggaran)
    layout_tombol_anggaran.addWidget(tombol_delete_anggaran)
    
    tabel_anggaran = QTableWidget(laman_anggaran)
    tabel_anggaran.setColumnCount(5)  
    tabel_anggaran.setHorizontalHeaderLabels(['Kategori', 'Anggaran', 'Periode', 'Tanggal Mulai', 'Tanggal Akhir'])
    tabel_anggaran.setColumnWidth(0, 200)
    tabel_anggaran.setColumnWidth(1, 150)
    tabel_anggaran.setColumnWidth(2, 150)
    tabel_anggaran.setColumnWidth(3, 230)
    tabel_anggaran.setColumnWidth(4, 230)

    layout_anggaran.addLayout(layout_tombol_anggaran)
    layout_anggaran.addWidget(tabel_anggaran)
    laman_anggaran.setLayout(layout_anggaran)
    
    laman_laporan = QWidget()
    layout_laporan = QVBoxLayout(laman_laporan)

    tabel_laporan = QTableWidget(laman_laporan)
    tabel_laporan.setColumnCount(4)
    tabel_laporan.setHorizontalHeaderLabels(['Kategori', 'Anggaran', 'Pengeluaran Aktual', 'Kesesuaian'])
    tabel_laporan.setColumnWidth(0, 240)
    tabel_laporan.setColumnWidth(1, 240)
    tabel_laporan.setColumnWidth(2, 240)
    tabel_laporan.setColumnWidth(3, 240)
    layout_laporan.addWidget(tabel_laporan)

    tombol_tampilkan_laporan = QPushButton('Hasilkan Laporan')
    tombol_tampilkan_laporan.setStyleSheet("background-color: #2196F3; color: white; height:40px; font-size: 20px;")
    tombol_tampilkan_laporan.clicked.connect(hasilkan_laporan)
    layout_laporan.addWidget(tombol_tampilkan_laporan)
    
    tab_widget.addTab(laman_beranda, "Beranda")
    tab_widget.addTab(laman_transaksi, "Transaksi")
    tab_widget.addTab(laman_anggaran, "Anggaran")
    tab_widget.addTab(laman_laporan, "Laporan")
    
    layout_utama = QVBoxLayout(window)
    layout_utama.addWidget(tab_widget)
    window.setLayout(layout_utama)

    muat_transaksi()
    muat_anggaran()
    tampilkan_total_pengeluaran()
    return window

def tambah_transaksi():
    tanggal = input_tanggal.date().toString("dd-MM-yyyy")
    deskripsi = input_deskripsi.text()
    kategori = input_kategori.text().upper()
    jumlah = input_nominal.text()

    if not tanggal or not deskripsi or not kategori or not jumlah or deskripsi == ' ' or kategori == ' ' or jumlah == ' ':
        QMessageBox.warning(laman_transaksi, "Peringatan", "Silakan isi semua kolom")
        return
    
    try:
        jumlah = float(jumlah)
        if jumlah <= 0:
            QMessageBox.warning(laman_transaksi, "Peringatan", "Nominal kurang dari 0")
            return
    except:
        QMessageBox.warning(laman_transaksi, "Peringatan", "Nominal tidak valid")
        return
    
    with open(f"transaksi{berkas_pengguna}.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, deskripsi, kategori, jumlah])
        
    fungsi_reset()
    muat_transaksi()

def muat_transaksi():
    global transaksi
    try:
        with open(f'transaksi{berkas_pengguna}.csv', "r") as file:
            reader = csv.reader(file)
            transaksi = []
            for row in reader:
                transaksi.append(row)
        update_tabel_transaksi(transaksi)
        update_opsi_filter()
    except:
        transaksi = []

def update_tabel_transaksi(data):
    tabel.setRowCount(0)
    for row in data:
        posisi_row = tabel.rowCount()
        tabel.insertRow(posisi_row)
        for kolom, item in enumerate(row):
            tabel.setItem(posisi_row, kolom, QTableWidgetItem(item))

def edit_transaksi():
    baris_yang_dipilih = tabel.currentRow()
    if baris_yang_dipilih < 0:
        QMessageBox.warning(laman_transaksi, "Edit gagal", "Silahkan pilih transaksi yang ingin di edit")
        return
    tanggal = input_tanggal.date().toString("dd-MM-yyyy")
    deskripsi = input_deskripsi.text()
    kategori = input_kategori.text().upper()
    jumlah = input_nominal.text()
    if not tanggal or not deskripsi or not kategori or not jumlah:
        QMessageBox.warning(laman_transaksi, "Edit Gagal", "Pastikan tanggal, deskripsi, kategori, dan nominal sudah terisi")
        return
    try:
        jumlah = float(jumlah)
    except:
        QMessageBox.warning(laman_transaksi, "Edit Gagal", "Nominal harus berupa angka")
        return
    transaksi[baris_yang_dipilih] = [tanggal, deskripsi, kategori, jumlah]
    simpan_transaksi()
    fungsi_reset()
    muat_transaksi()

def hapus_transaksi():
    tabel_dipilih = tabel.currentRow()
    if tabel_dipilih < 0:
        QMessageBox.warning(laman_transaksi, "Delete Gagal", "Silakan pilih transaksi yang ingin dihapus")
        return
    del transaksi[tabel_dipilih]
    simpan_transaksi()
    muat_transaksi()

def simpan_transaksi():
    with open(f"transaksi{berkas_pengguna}.csv","w") as file:
        writer = csv.writer(file)
        writer.writerows(transaksi)

def filter_transaksi():
    kategori_dipilih = filter_combo.currentText()
    data_filter = []
    if kategori_dipilih == "Tampilkan Semua":
        data_filter = transaksi
    elif kategori_dipilih:
        for row in transaksi:
            if len(row) > 2 and row[2] == kategori_dipilih:
                data_filter.append(row)
    update_tabel_transaksi(data_filter)

def update_opsi_filter():
    filter_combo.clear()
    kategori = set()

    for row in transaksi:
        if len(row) > 2:
            kategori.add(row[2])

    if kategori:
        kategori_sorted = sorted(kategori)
        filter_combo.addItem("Tampilkan Semua")
        filter_combo.addItems(kategori_sorted)

def filter_tanggal_transaksi():
    filter_tanggal = filter_tanggal_input.text()
    data_filter = []
    for row in transaksi:
        if row[0].startswith(filter_tanggal):
            data_filter.append(row)
    update_tabel_transaksi(data_filter)

def tampilkan_total_pengeluaran():
    total_pengeluaran_harian = 0.0
    total_pengeluaran_mingguan = 0.0
    total_pengeluaran_bulanan = 0.0
    for row in transaksi:
        if len(row) > 3:
            jumlah = float(row[3])
            string_tanggal = row[0]
            tanggal = QDate.fromString(string_tanggal, "dd-MM-yyyy")
            tanggal_sekarang = QDate.currentDate()

            if tanggal == tanggal_sekarang:
                total_pengeluaran_harian += jumlah
            if tanggal >= tanggal_sekarang.addDays(-tanggal_sekarang.dayOfWeek() + 1) and tanggal < tanggal_sekarang.addDays(7 - tanggal_sekarang.dayOfWeek() + 1):
                total_pengeluaran_mingguan += jumlah
            if tanggal.month() == tanggal_sekarang.month() and tanggal.year() == tanggal_sekarang.year():
                total_pengeluaran_bulanan += jumlah
    
    total_pengeluaran_harian_teks.setText(f"Pengeluaran Hari Ini: {total_pengeluaran_harian}")
    total_pengeluaran_mingguan_teks.setText(f"Pengeluaran Minggu Ini: {total_pengeluaran_mingguan}")
    total_pengeluaran_bulanan_teks.setText(f"Pengeluaran Bulan Ini: {total_pengeluaran_bulanan}")

def muat_anggaran():
    global anggaran
    try:
        with open(f"anggaran{berkas_pengguna}.csv","r") as file:
            reader = csv.reader(file)
            anggaran = []
            for row in reader:
                anggaran.append(row)
        perbarui_tabel_anggaran(anggaran)
    except:
        anggaran = []

def tambah_anggaran():
    kategori = input_kategori_anggaran.text().upper()
    jumlah = input_nominal_anggaran.text()
    periode = combo_periode_anggaran.currentText()
    mulai = input_mulai_anggaran.date().toString("dd-MM-yyyy")
    akhir = input_akhir_anggaran.date().toString("dd-MM-yyyy")

    tanggal_mulai = input_mulai_anggaran.date()
    tanggal_akhir = input_akhir_anggaran.date()
    if not kategori or not jumlah or not periode or not mulai or not akhir:
        QMessageBox.warning(laman_anggaran, "Peringatan", "Silakan isi semua form")
        return
    
    if periode == "Harian" and mulai != akhir:
        QMessageBox.warning(laman_anggaran, "Error", "Untuk anggaran harian, tanggal akhir harus sama dengan tanggal mulai.")
        return
    elif periode == "Mingguan" and tanggal_akhir > tanggal_mulai.addDays(7):
        QMessageBox.warning(laman_anggaran, "Error", "Untuk anggaran mingguan, tanggal akhir tidak boleh lebih dari 7 hari dari tanggal mulai.")
        return
    elif periode == "Bulanan" and tanggal_mulai > tanggal_akhir.addDays(30):
        QMessageBox.warning(laman_anggaran, "Error", "Untuk anggaran bulanan, tanggal akhir tidak boleh lebih dari 30 hari dari tanggal mulai.")
        return

    for row in anggaran:
        if row[0] == kategori:
            if row[2] == periode:
                QMessageBox.warning(laman_anggaran, "Peringatan", "Kategori sudah ada, silakan ubah kategori lainnya.")
                return
    try:
        jumlah = float(jumlah)
    except:
        QMessageBox.warning(laman_anggaran, "Peringatan", "Nominal tidak valid")
        return

    with open(f'anggaran{berkas_pengguna}.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow([kategori, jumlah, periode, mulai, akhir])
    
    
    input_kategori_anggaran.clear()
    input_nominal_anggaran.clear()
    muat_anggaran()

def edit_anggaran():
    tabel_dipilih = tabel_anggaran.currentRow()
    if tabel_dipilih < 0:
        QMessageBox.warning(laman_anggaran, "Edit Gagal", "Silahkan pilih anggaran yang ingin diedit")
        return
    kategori = input_kategori_anggaran.text().upper()
    jumlah = input_nominal_anggaran.text()
    periode_indeks = combo_periode_anggaran.currentIndex()
    periode_teks = combo_periode_anggaran.currentText()
    mulai = input_mulai_anggaran.date().toString("dd-MM-yyyy")
    akhir = input_akhir_anggaran.date().toString("dd-MM-yyyy")
    
    if not kategori or not jumlah or periode_indeks < 0 or not mulai or not akhir:
        QMessageBox.warning(laman_anggaran, "Edit Gagal", "Silahkan isi semua data")
        return
    try:
        jumlah = float(jumlah)
        if jumlah <= 0:
            QMessageBox.warning(laman_transaksi, "Peringatan", "Nominal kurang dari 0")
            return
    except:
        QMessageBox.warning(laman_anggaran, "Edit Gagal", "Silahkan isi nominal dengan angka")
        return
    
    for row in anggaran:
        if row[0] == kategori and tabel_dipilih != anggaran.index(row):
            if row[2] == periode_teks:
                QMessageBox.warning(laman_anggaran, "Peringatan", "Kategori sudah ada, silakan ubah kategori lainnya.")
                return

    anggaran[tabel_dipilih] = [kategori, jumlah, periode_teks, mulai, akhir]
    simpan_anggaran()
    muat_anggaran()

def delete_anggaran():
    tabel_dipilih = tabel_anggaran.currentRow()
    if tabel_dipilih < 0:
        QMessageBox.warning(laman_anggaran, "Hapus Gagal", "Silahkan pilih anggaran yang ingin dihapus")
        return
    del anggaran[tabel_dipilih]
    simpan_anggaran()
    muat_anggaran()
    
def simpan_anggaran():
    with open(f'anggaran{berkas_pengguna}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(anggaran)

def perbarui_tabel_anggaran(data):
    tabel_anggaran.setRowCount(0)
    for row in data:
        posisi_row = tabel_anggaran.rowCount()
        tabel_anggaran.insertRow(posisi_row)
        for kolom, item in enumerate(row):
            tabel_anggaran.setItem(posisi_row, kolom, QTableWidgetItem(item))

def hasilkan_laporan():
    laporan = []
    for item in anggaran:
        kategori = item[0]
        jumlah_anggaran = float(item[1])
        tanggal_mulai = QDate.fromString(item[3], "dd-MM-yyyy")
        tanggal_akhir = QDate.fromString(item[4], "dd-MM-yyyy")
        pengeluaran_aktual = 0
        for row in transaksi:
            if row[2] == kategori and tanggal_mulai <= QDate.fromString(row[0], "dd-MM-yyyy") <= tanggal_akhir:
                pengeluaran_aktual += float(row[3])
        
        if pengeluaran_aktual <= jumlah_anggaran:
            status = "Dalam anggaran"
        else:
            status = "Melebihi anggaran"
        laporan.append([kategori, jumlah_anggaran, pengeluaran_aktual, status])

    tabel_laporan.setRowCount(0)
    for row in laporan:
        posisi_baris = tabel_laporan.rowCount()
        tabel_laporan.insertRow(posisi_baris)
        for kolom, barang in enumerate(row):
            tabel_laporan.setItem(posisi_baris, kolom, QTableWidgetItem(str(barang)))

def fungsi_reset():
    input_deskripsi.clear()
    input_kategori.clear()
    input_nominal.clear()

app = QApplication(sys.argv)
if menu_login_tampilan():
    window = setup_ui()
    window.show()
    app.exec()
