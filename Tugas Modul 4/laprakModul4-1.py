def tampilkan_motor(motor_tersedia):
    """Fungsi untuk menampilkan daftar motor"""
    list_motor_dengan_Nomor = [f"{i+1}. {motor}" for i, motor in enumerate(motor_tersedia)]
    for item in list_motor_dengan_Nomor:
        print(item)

def tambah_motor(motor_tersedia, motor_baru):
    """Method untuk menambahkan motor baru"""
    motor_tersedia.append(motor_baru)
    tampilkan_motor(motor_tersedia)
