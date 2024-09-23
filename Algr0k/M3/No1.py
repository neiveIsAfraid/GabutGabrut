number = int(input("Give me a number: "))
to_iterate = number

while to_iterate >= 0:
    if to_iterate % 2 != 0:
        print(f"The {to_iterate} is an odd number")
    to_iterate-=1

"""
Buatlah program untuk mencetak bilangan ganjil dari N sampai dengan 1 dimana
N adalah bilangan bulat masukkan pengguna. Sebagai contoh ketika pengguna
memasukkan 10, maka komputer akan mencetak 9 7 5 3 1.
"""
