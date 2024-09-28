# Simple Quiz Program
print("Tampilkan Jumlah huruf dari kalimat yang dimasukkan ")
string_template = 0
confirm = "y"

while confirm == "y":
    kalimat_masukan = input("Masukkan Kalimat: ")
    for i in range(1, len(kalimat_masukan)+1):
        string_template+= 1
    print(f"Kata anda: '{kalimat_masukan}', memiliki {string_template} huruf dengan spasi")
    print("\n\nLanjutkan program ? ")
    confirm = input("Lanjut ? (y\\n) ")
    string_template = 0


"""

""" 