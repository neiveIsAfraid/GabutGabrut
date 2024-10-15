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

"""
