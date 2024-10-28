
contacts = {
    "Anto": "+628 6534 3425",
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
  try:
    pilihan = int(input(f"\n{"=" * 12} MENU {"=" * 12}\n\n1. Tampilkan seluruh kontak\n2. Cari kontak dengan nama\n3. Tambah kontak\n4. Hapus kontak\n5. Keluar\n:"))
  except ValueError:
    print("\033[41mMohon memasukkan nomor menu... (e.g., '1')\033[0m")
    input("Tekan enter untuk melanjutkan")
    
  if pilihan == 1:
    nama_kontak = list(contacts.keys())
    
    for i in range(len(nama_kontak)):
      print(f"{i + 1}. {nama_kontak[i]}")
    
    while True:
      try:  
        pilihan_2 = int(input("\n1. Tampilkan nomor dari kontak\n2. Kembali ke menu\n: "))
        break
      except ValueError:
        print("\033[41mMohon memasukkan nomor menu... (e.g., '1')\033[0m")
        input("Tekan enter untuk melanjutkan")
    
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
    while True:
      try:
        banyak_masukan = int(input("Berapa banyak kontak yang ingin anda masukkan\n: "))
        break
      except ValueError:
        print("\033[41mMohon masukkan angka yang benar... (e.g., '1')\033[0m")
        input("Tekan enter untuk melanjutkan")
    
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
  
  elif pilihan > 5:
    print("\033[41mTidak termasuk dalam pilihan...\033[0m")
    input("Tekan enter untuk melanjutkan...")
  
  pilihan = 0
