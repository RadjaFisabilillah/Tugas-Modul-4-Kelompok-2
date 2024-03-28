print ('===KELOMPOK 2 PENYEDIAAN MOTOR===')

print('Damai Raya Fakhruddin (21120123130096)')
print('Herdika Putra Devara (21120123140112)')
print('Muhammad Ilham (21120123120003)')
print('Radja Fisabilillah (21120123130102)')
print('\nKelompok 2 shift 1')

def tampilkan_motor(motor_tersedia):
    """Fungsi untuk menampilkan daftar motor"""
    list_motor_dengan_Nomor = [f"{i+1}. {motor}" for i, motor in enumerate(motor_tersedia)]
    for item in list_motor_dengan_Nomor:
        print(item)

def tambah_motor(motor_tersedia, motor_baru):
    """Method untuk menambahkan motor baru"""
    motor_tersedia.append(motor_baru)

def hapus_motor(motor_tersedia, motor_hapus):
    """Method untuk menghapus motor"""
    if motor_hapus in motor_tersedia:
        motor_tersedia.remove(motor_hapus)
    else:
        print('Motor tidak terdapat pada list (perhatikan penulisan)')

def reset_motor():
    """Function tanpa parameter untuk mereset daftar motor"""
    return ['Honda Beat', 'Yamaha NMAX', 'Suzuki Satria']

def main():
    """Fungsi utama"""
    motor_tersedia = reset_motor()

    while True:
        tampilkan_motor(motor_tersedia)

        tambah_atau_hapus = input("Pilih opsi Tambah, Hapus, RESET, STOP: ")

        if tambah_atau_hapus == "Tambah":
            tertambah_motor = input('Masukkan motor baru: ')
            tambah_motor(motor_tersedia, tertambah_motor)

        elif tambah_atau_hapus == "Hapus":
            terkurang_motor = input('Tulis motor yang ingin dihapus: ')
            hapus_motor(motor_tersedia, terkurang_motor)

        elif tambah_atau_hapus == "RESET":
            motor_tersedia = reset_motor()

        elif tambah_atau_hapus == "STOP":
            tampilkan_motor(motor_tersedia)  # Cetak daftar motor sebelum program berakhir
            break

        else:
            print("Tolong perhatikan penulisan")

if __name__ == "__main__":
    main()
