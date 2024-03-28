while True:
    buku_tersedia = ['Sherlock Holmes', 'Mahmoud Darwis', 'Dune']

    while True :
        list_buku_dengan_Nomor = [f"{i+1}. {buku}" for i, buku in enumerate(buku_tersedia)]

        for item in list_buku_dengan_Nomor:
            print(item)

        tambah_atau_hapus = input("pilih opsi Tambah, Hapus, STOP:")

        if tambah_atau_hapus == "Tambah" :

            tertambah_buku = str(input('Masukkan buku baru:'))

            buku_tersedia.append(tertambah_buku)

            for item in list_buku_dengan_Nomor:
                    print(item)
                    
        elif tambah_atau_hapus == "Hapus" :
            terkurang_buku = str(input('Tulis buku yang ingin dihapus:'))

            if terkurang_buku in buku_tersedia:

                buku_tersedia.remove(terkurang_buku)

                for item in list_buku_dengan_Nomor:
                    print(item)

            else:
                print('buku tidak terdapat pada list (perhatikan penulisan)')

        elif tambah_atau_hapus == "STOP":
            break

        else:
            print("Tolong Perhatikan Penulisan")
