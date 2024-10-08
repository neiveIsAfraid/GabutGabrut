contacts = {
    "Anto": "+628 6534 3425 ",
    "Budi": "+628 5578 0979",
    "Andi": "+628 5578 2156",
    "Arif": "+628 5578 1432",
    "Axel": "+628 5578 0789",
    "Risqy":"+628 5578 1231",
    "John": "+628 5578 1453",
    "James":"+628 5578 0789"
}

pilihan = 0
while pilihan != 5:
    pilihan = int(input(f"\n{"=" * 12} MENU {"=" * 12}\n\n1. Tampilkan seluruh kontak\n2. Cari kontak dengan nama\n3. Tambah kontak\n4. Hapus kontak\n5. Keluar\n:"))

    if pilihan == 1:
        nama_kontak = list(contacts.keys())
        for i in range(len(nama_kontak)):
            print(f"{i + 1}. {nama_kontak[i]}")
        pilihan_2 = int(input("\n1. Tampilkan nomor dari kontak\n2. Kembali ke menu\n: "))
        if pilihan_2 == 1:
            key = input("\nNama: ")
            if key in contacts:
                print(f"Kontak ditemukan\n{key}: {contacts[key]}")
                input("Tekan enter untuk melanjutkan...")
            else:
                print(f"Kontak dengan nama \033[31m{key}\033[0m tidak ditemukan")
                input("Tekan enter untuk melanjutkan...")
        else:
            continue

    elif pilihan == 2:
        key = input("Nama: ")
        if key in contacts:
            print(f"Kontak ditemukan\n{key}: {contacts[key]}")
            input("Tekan enter untuk melanjutkan...")
        else:
            print(f"Kontak dengan nama \033[31m{key}\033[0m tidak ditemukan")
            input("Tekan enter untuk melanjutkan...")


    elif pilihan == 3:
        banyak_masukan = int(input("Berapa banyak kontak yang ingin anda masukkan\n: "))
        for i in range(banyak_masukan):
            print(f"Kontak {i + 1}")
            key = input("Nama: ")
            value = input("Nomor Telepon: ")
            contacts[key] = value
            print(f"Kontak {key} Berhasil ditambahkan")
            input("Tekan enter untuk melanjutkan...")
    
    elif pilihan == 4:
        untuk_dihapus = input("Masukan kontak yang ingin dihapus\n: ")
        if untuk_dihapus in contacts:
            contacts.pop(untuk_dihapus, None)
            print(f"Kontak {untuk_dihapus} berhasil dihapus")
            input("Tekan enter untuk melanjutkan...")
        else:
            print(f"Kontak dengan nama \033[31m{untuk_dihapus}\033[0m tidak ditemukan\nTidak ada yang dilakukan")
            input("Tekan enter untuk melanjutkan...")
          
"""
1-10. Buat dictionary "contacts" dengan template nama kontak sebagai permulaan

12. Deklarasi variabel "pilihan" dengan nilai default 0, bertipe data integer
13. Buat perulangan while dengan kondisi ketika pilihan tidak sama dengan 5 ulangi blok kode berikut secara terus menerus
14. Deklarasi ulang variabel "pilihan" dengan masukan pengguna berupa pilihan menu dalam program, bertipe data integer

16. eksekusi kondisional ketika nilai dari variabel pilihan sama dengan 1, eksekusi kode berikut
17. Buat variabel "nama_kontak" dengan nilai keys (mengambil nama kontak) dari dictionary "contacts"
18. Perulangan for dengan iterable jumlah item dari list "nama_kontak" dan iterator "i"
19. Tampilkan nama kontak, menggunakan nilai dari list "nama_kontak" pada index sesuai dengan iterator "i"
20. Deklarasi variabel "pilihan_2" dengan nilai bertipe data integer dari masukan pengguna berupa pilihan apakah pengguna ingin menampilkan nomor dari kontak atau tidak
21. Eksekusi kondisional jika nilai dari variabel "pilihan_2" sama dengan 1, untuk menampilkan nomor kontak, eksekusi blok kode berikut 
22. deklarasi variabel "key" dengan masukan pengguna bertipe data string dengan nilai nama dari kontak yang nomornya ingin ditampilkan
23. eksekusi kondisional dengan kondisi bila nilai dari variabel "key" terdapat didalam dictionary "contacts", eksekusi blok kode berikut
24. Tampilkan "Kontak ditemukan" dengan string formatting mengambil nilai dari keys "key" dan value yang terdapat pada key tersebut didalam dictionary "contacts"
25. Fungsi input yang digunakan untuk men-delay perulangan while
26-27. Jika nilai variabel "key" tidak ditemukan didalam dictionary "contacts" tampilkan string "Kontak dengan nama" nilai yang terdapat dalam variabel "key" "tidak ditemukan", highlight merah ketika nilai "key" ditampilkan
28. Fungsi input yang digunakan untuk men-delay perulangan while
29 - 30. Eksekusi kondisional apabila nilai "pilihan_2" selain daripada 1, lanjutkan program ini

32. Eksekusi kondisional ketika pengguna memasukan nilai 2 pada variabel "pilihan" untuk mencari kontak dengan nama, eksekusi blok kode berikut
33. deklarasi variabel "key" dengan nilai masukan berupa Nama yang ingin dicari
34. Kondisi kondisional jika nilai variabel "key" terdapat didalam dictionary "contacts" eksekusi blok kode berikut
35. Tampilkan "Kontak ditemukan" dengan string formatting mengambil nilai dari variabel "key" dan value yang terdapat pada key pair tersebut didalam dictionary "contacts"
36. Fungsi input yang digunakan untuk men-delay perulangan while
37-38. Jika nilai variabel "key" tidak ditemukan didalam dictionary "contacts" tampilkan string "Kontak dengan nama" nilai yang terdapat dalam variabel "key" "tidak ditemukan", highlight merah ketika nilai "key" ditampilkan
39. Fungsi input yang digunakan untuk men-delay perulangan while

42. eksekusi kondisional dengan kondisi bila nilai variabel "pilihan" sama dengan 3, eksekusi blok kode berikut
43. deklarasi variabel "banyak_masukan" yang mengambil nilai masukan bertipe data integer dari pengguna, menu untuk menambahkan kontak
44. perulangan for yang berulang sesuai dengan nilai variabel "banyak_masukan"
45. Tampilkan String "Kontak" dengan menggunakan string formatting mengambil nilai dari iterator "i" ditambah 1
46. Deklarasi variabel "key" dengan nilai masukan pengguna berupa Nama kontak yang ingin ditambahkan
47.  Deklarasi variabel "value" dengan nilai masukan pengguna berupa nomor kontak yang ingin ditambahkan

48. Masukkan nilai dari variabel "key" pada dictionary "contacts" sebagai key dengan nilai key dari variabel "value"
49. Tampilkan string "Kontak" dengan nilai variabel "key" "berhasil ditambahkan"
50. Fungsi input yang digunakan untuk men-delay perulangan while
52. Eksekusi kondisional dengan kondisi bila nilai variabel "pilihan" bernilai sama dengan 4, eksekusi blok kode berikut
53. Deklarasi variabel "untuk_dihapus" dengan masukan pengguna berupa nama dari kontak yang ingin dihapus

54. Kondisi kondisional, jika nilai variabel "untuk_dihapus" terdapat didalam dictionary "contacts" eksekusi blok kode berikut
55. Hapus nilai dari key dictionary "contacts" yang sesuai dengan nilai variabel "untuk_dihapus" 
56. Tampilkan "Kontak" dengan string formatting nilai dari variabel "untuk_dihapus" "berhasil dihapus"
57. Fungsi input yang digunakan untuk men-delay perulangan while
58-59. Jika nilai variabel "untuk_dihapus" tidak ditemukan didalam dictionary "contacts" tampilkan string "Kontak dengan nama" nilai yang terdapat dalam variabel "untuk_dihapus" "tidak ditemukan", highlight merah ketika nilai "key" ditampilkan buat baris baru dan tampilkan "Tidak ada yang dilakukan"
60. Fungsi input yang digunakan untuk men-delay perulangan while
"""
