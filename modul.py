stok_barang = []
def tambah_data ():
    nama_barang = str(input("Masukan Nama Barang : "))
    stok = int(input("Masukan Stok Barang : "))

    stok_baru = {f"nama": nama_barang, "stok": stok}
    stok_barang.append(stok_baru)
    
def edit_data():
    edit = int(input("Edit Data Index Ke: "))
    if edit <= len(stok_barang):
        nama_baru= input("Masukkan Nama: ")
        stok_baru = int(input("Masukkan Stok: "))
        stok_barang[edit] = {"nama": nama_baru, "stok": stok_baru}
        print("Data Berhasil Diedit")
    else:
        print("Index Tidak Valid")

def hapus_data():
    hapus = int(input("Hapus Data Index Ke : "))
    stok_barang.pop(hapus)
    print("Data Berhasil Dihapus")

def cari_data():
    cari_nama = str(input("Cari Nama Barang : "))
    print("===== Hasil Pencarian =====")
    for i in stok_barang:
        print(f"•", i["nama"], ",", "stok :", i["stok"])
        return
    print("Data Barang Kosong")

def tampilkan_data():
    print("===== Toko Elektronik =====")
    if not stok_barang:
        print("----- Data Barang Kosong -----")
    else:
        for i in stok_barang:
            print(f"•", i["nama"], ",", "stok :", i["stok"])

def tampilkan_jumlah():
    print(f"Jumlah Data Tersimpan :", len(stok_barang), "Barang")


        

        

  