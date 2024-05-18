import modul as mod

print("Selamat Datang di Program Manajemen Stok Barang!")
print("Pilihan:")
print("1. Tambah Data Barang")
print("2. Edit Data")
print("3. Hapus Data Barang")
print("4. Cari Data")
print("5. Tampilkan Data Barang")
print("6. Tampilkan Jumlah Data")
print("7. Keluar")
        
while True:
    pilihan = input("Masukkan pilihan: ")
    print("============================")
        
    if pilihan == '1':
        mod.tambah_data()
    elif pilihan == '2':
        mod.edit_data()
    elif pilihan == '3':
        mod.hapus_data()
    elif pilihan == '4':
        mod.cari_data()
    elif pilihan == '5':
        mod.tampilkan_data()
    elif pilihan == '6':
        mod.tampilkan_jumlah()
    elif pilihan == '7':
        print("Terima Kasih Sudah Menggunakan Program Ini")
        break
    else:
        print("Pilihan Tidak Valid, Silakan Coba Lagi")

