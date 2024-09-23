import math

pilihan = 0
while pilihan != 4:
    print("Menu\n1.Persegi\n2.Persegi Panjang\n3.Segitiga\n4.Exit\n")
    pilihan = int(input(": "))

    if pilihan == 1:
        print("\n\n===Persegi===\n1.Luas\n2.Keliling")
        luas_or_keliling = int(input(": "))
        if luas_or_keliling == 1:
            panjang = int(input("Panjang: "))
            lebar = panjang
            print(f"\n\033[32mLuas: {panjang * lebar} cm\033[0m\n")
            lanjut = input("Tekan enter untuk lanjut\n\n")

        elif luas_or_keliling == 2:
            panjang = int(input("Panjang: "))
            lebar = panjang
            print(f"Keliling: {2 * (panjang + lebar)}")
            lanjut = input("Tekan enter untuk lanjut\n\n")

    elif pilihan == 2:
        print("\n\n===Persegi Panjang===\n1.Luas\n2.Keliling\n")
        luas_or_keliling = int(input(": "))
        if luas_or_keliling == 1:
            panjang = int(input("Panjang: "))
            lebar = int(input("Lebar: ")) 
            satuan = ""
            print(f"Luas: {panjang * lebar} {satuan}\n")
            lanjut = input("Tekan enter untuk lanjut\n\n")

        elif luas_or_keliling == 2:
            panjang = int(input("Panjang: "))
            lebar = int(input("Lebar: "))
            satuan = ""
            print(f"Keliling: {2 * (panjang + lebar)} {satuan}")
            lanjut = input("Tekan enter untuk lanjut\n\n")

    elif pilihan == 3:
        print("3.Segitiga")
        print("\n\n===Segitiga Sama Sisi===\n1.Luas\n2.Keliling\n")
        luas_or_keliling = int(input(": "))
        if luas_or_keliling == 1:
            panjang = int(input("Panjang: "))
            satuan = ""
            print(f"Luas: {(1/4 * panjang**2)* math.sqrt(3)} {satuan}\n")
            lanjut = input("Tekan enter untuk lanjut\n\n")

        elif luas_or_keliling == 2:
            panjang = int(input("Panjang: "))
            satuan = ""
            print(f"Keliling: {3 * panjang} {satuan}")
            lanjut = input("Tekan enter untuk lanjut\n\n")
    else:
        print("\033[31mNot in choice.\033[0m")

"""
Buatlah program luas dan keliling bidang persegi, persegi panjang, dan segitiga
dengan pilihan menu. Selama menu keluar tidak dipilih, program terus berjalan.
"""
