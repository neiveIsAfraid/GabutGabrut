"""
Buatlah program penerjemah protein yang menerima masukkan berupa kodon
dan memberikan keluaran berupa nama protein. Sebagai contoh jika masukkan
berupa “UUU” atau “UUC” maka menghasilkan “Phenylalanine”. Terjemahan
protein dapat dilihat dibawah :
     Kodon           Protein
AUG                  Methionine
UUU, UUC             Phenylalanine
UUA, UUG             Leucine
UCU, UCC, UCA, UCG   Serine
UAU, UAC             Tyrosine
UGU, UGC             Cysteine
UGG                  Tryptophan
"""

berapa_kodon = int(input("Berapa kodon bang ? "))

if berapa_kodon == 1:
    pilihan1 = input("Masukkan Kodon: ").upper
    if pilihan1 == "AUG":
        print("Methionine")
    elif pilihan1 == "UGG":
        print("Trytophan")
    else:
        print("\033[33mData Tidak Ditemukan\033[0m")

elif berapa_kodon == 2:
    pilihan1 = input("Masukkan Kodon 1: ")
    pilihan2 = input("Masukkan Kodon 2: ")
    if pilihan1 == "UUU" and pilihan2 == "UUC" or pilihan1 == "UUC" and pilihan2 == "UUU":
        print("Phenylalanine")
    elif pilihan1 == "UUA" and pilihan2 == "UUG" or pilihan1 == "UUG" and pilihan2 == "UUA":
        print("Leucine")
    elif pilihan1 == "UAU" or pilihan2 == "UAC" and pilihan1 == "UAC" or pilihan2 == "UAU":
        print("Tyrosine")
    elif pilihan1 == "UGU" or pilihan2 == "UGC" and pilihan1 == "UGC" and pilihan2 == "UGU":
        print("Tryptophan")
    else:
        print("Data tidak ditemukan")

elif berapa_kodon == 4:
    pilihan1 = input("Masukkan kodon 1: ")
    pilihan2 = input("Masukkan kodon 2: ")
    pilihan3 = input("Masukkan kodon 3: ")
    pilihan4 = input("Masukkan kodon 4: ")

    if pilihan1 == "UCU" and pilihan2 == "UCC" and pilihan3 == "UCA" and pilihan4 == "UCG" or pilihan1 == "UCC" and pilihan2 == "UCA" and pilihan3 == "UCG" and pilihan4 == "UCU" or pilihan1 == "UCA" and pilihan2 == "UCG" and pilihan3 == "UCU" and pilihan4 == "UCC":
        print("Serine")
    else:
        print("Data tidak ditemukan")
else:
    print("Waduh masih belum support bang")