masukan_pengguna = int(input(": "))
to_iterate = masukan_pengguna + 1
for i in range(to_iterate, 0, -1):
    if i % 2 != 0:
        print(i * "-")
    else:
        print(i * "*")

"""
Kerjakan no 4bc
"""