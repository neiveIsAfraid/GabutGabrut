import math

pilihan = 0
while pilihan != 4:
    print("Menu\n1.Persegi\n2.Persegi Panjang\n3.Segitiga\n4.Exit\n")
    pilihan = int(input(": "))

    if pilihan == 1:
        print("\n\n===Persegi===\n1.Luas\n2.Keliling")
        luas_or_keliling = int(input(": "))
        if luas_or_keliling == 1:
            sisi = float(input("Panjang Sisi: "))
            print(f"\n\033[32mLuas: {sisi * sisi} cm\033[0m\n")
            lanjut = input("Tekan enter untuk lanjut\n\n")

        elif luas_or_keliling == 2:
            sisi = float(input("Panjang sisi: "))
            print(f"Keliling: {4 * sisi}")
            lanjut = input("Tekan enter untuk lanjut\n\n")

    elif pilihan == 2:
        print("\n\n===Persegi Panjang===\n1.Luas\n2.Keliling\n")
        luas_or_keliling = int(input(": "))
        if luas_or_keliling == 1:
            panjang = float(input("Panjang: "))
            lebar = float(input("Lebar: ")) 
            print(f"Luas: {panjang * lebar}\n")
            lanjut = input("Tekan enter untuk lanjut\n\n")

        elif luas_or_keliling == 2:
            panjang = float(input("Panjang: "))
            lebar = float(input("Lebar: "))
            print(f"Keliling: {2 * (panjang + lebar)}")
            lanjut = input("Tekan enter untuk lanjut\n\n")

    elif pilihan == 3:
        print("3.Segitiga")
        print("\n\n===Segitiga Sama Sisi===\n1.Luas\n2.Keliling\n")
        luas_or_keliling = float(input(": "))
        if luas_or_keliling == 1:
            panjang = float(input("Panjang: "))
            print(f"Luas: {(1/4 * panjang**2)* math.sqrt(3)}\n")
            lanjut = input("Tekan enter untuk lanjut\n\n")

        elif luas_or_keliling == 2:
            panjang = float(input("Panjang: "))
            print(f"Keliling: {3 * panjang}")
            lanjut = input("Tekan enter untuk lanjut\n\n")
    else:
        print("\033[31mNot in choice.\033[0m")
