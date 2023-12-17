# Program Kasir Sederhana 2.0
print("""
==================================
            Warung Gilang
        Makanan dan Minuman
==================================
               Menu
              Masakan
----------------------------------
| Kode |     Nama    |   Harga   |
----------------------------------
|  NP  | Nasi Pecel  |  Rp 7000  |
|  NG  | Nasi Goreng |  RP 10000 |
|  NC  | Nasi Campur |  RP 8000  |

               Menu
              Minuman
----------------------------------
| Kode |     Nama    |   Harga   |
----------------------------------
|  ET  |    Es Teh   |  Rp 3000  |
|  TH  |  Teh Hangat |  RP 4000  |
|  EJ  |   Es Jeruk  |  RP 5000  |

         =================
         Selamat Menikmati
         =================
""")

import os
def pause():
    os.system("pause")

# Input pesanan oleh user
print("")
pesan_makanan = input("Silahkan Masukkan Kode Makanan Pesanan Anda : ")
if pesan_makanan == "NP" :
    n1 = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
    print("Nama Makanan : Nasi Pecel\nHarga : Rp 7000")
    total_0= 7000*n1
elif pesan_makanan == "NG" :
    n1 = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
    print("Nama Makanan : Nasi Goreng\nHarga : Rp 10000")
    total_0 = 10000*n1
elif pesan_makanan == "NC" :
    n1 = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
    print("Nama Makanan : Nasi Campur\nHarga : Rp 8000")
    total_0 = 8000*n1
elif pesan_makanan == "-" :
    n1 = 0
    print("Silahkan Masukkan Jumlah Pesanan Anda : ", n1)
    total_0 = 0*n1
print("")
print("--------------------------------------")
print("Total Harga Makanan Anda : ", total_0)
print("--------------------------------------")
print("\n")

# Konfirmasi input pesanan kedua
print("1. lanjut pesan makanan lagi\n2. lanjut pesan minuman\n3. udah, totalin aja\n")
plh = int(input("Silahkan Pilih Opsi :  "))
print("\n")
if plh == 1 :
    pesan_makanan = input("Silahkan Masukkan Kode Makanan Pesanan Anda : ")
    if pesan_makanan == "NP" :
        n2a = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Makanan : Nasi Pecel\nHarga : Rp 7000")
        total_1a = 7000*n2a
    elif pesan_makanan == "NG" :
        n2a = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Makanan : Nasi Goreng\nHarga : Rp 10000")
        total_1a = 10000*n2a
    elif pesan_makanan == "NC" :
        n2a = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Makanan : Nasi Campur\nHarga : Rp 8000")
        total_1a = 8000*n2a
    elif pesan_makanan == "-" :
        n2a = 0
        print("Silahkan Masukkan Jumlah Pesanan Anda : ", n2a)
        total_1a = 0*n2a
    t = total_0 + total_1a
    print("")
    print("------------------------------------------")
    print("Total Harga Makanan Anda : ", total_1a)
    print("------------------------------------------")
    print("\n")

elif plh == 2 :
    pesan_minuman = input("Silahkan Masukkan Kode Minuman Pesanan Anda : ")
    if pesan_minuman == "ET" :
        n2b = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Minuman : Es Teh\nHarga : Rp 3000")
        total_1b = 3000*n2b
    elif pesan_minuman == "TH" :
        n2b = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Minuman : Teh Hangat\nHarga : Rp 4000")
        total_1b = 4000*n2b
    elif pesan_minuman == "EJ" :
        n2b = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Minuman : Es Jeruk\nHarga : Rp 5000")
        total_1b = 5000*n2b
    elif pesan_minuman == "-" :
        n2b = 0
        print("Silahkan Masukkan Jumlah Pesanan Anda : ", n2b)
        total_1b = 0*n2b
    t = total_0 + total_1b
    print("")
    print("------------------------------------------")
    print("Total Harga Minuman Anda : ", total_1b)
    print("------------------------------------------")
    print("\n")

elif plh == 3 :
    t = total_0
    print("\n")
    print("==================================")
    print("Total Harga Pesanan Anda : ", t)
    print("")
    raise SystemExit

# Konfirmasi input pesanan ketiga
print("1. lanjut pesan makanan lagi\n2. udah cukup, lanjut pesan minuman\n3. udah, totalin aja\n")
plh = int(input("Silahkan Pilih Opsi :  "))
print("\n")
if plh == 1 :
    pesan_makanan = input("Silahkan Masukkan Kode Makanan Pesanan Anda : ")
    if pesan_makanan == "NP" :
        n3a = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Makanan : Nasi Pecel\nHarga : Rp 7000")
        total_2a = 7000*n3a
    elif pesan_makanan == "NG" :
        n3a = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Makanan : Nasi Goreng\nHarga : Rp 10000")
        total_2a = 10000*n3a
    elif pesan_makanan == "NC" :
        n3a = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Makanan : Nasi Campur\nHarga : Rp 8000")
        total_2a = 8000*n3a
    p = t + total_2a
    print("") 
    print("------------------------------------------")
    print("Total Harga Makanan Anda : ", total_2a)
    print("------------------------------------------")
    print("\n")

elif plh == 2 :
    pesan_minuman = input("Silahkan Masukkan Kode Minuman Pesanan Anda : ")
    if pesan_minuman == "ET" :
        n3b = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Minuman : Es Teh\nHarga : Rp 3000")
        total_2b = 3000*n3b
    elif pesan_minuman == "TH" :
        n3b = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Minuman : Teh Hangat\nHarga : Rp 4000")
        total_2b = 4000*n3b
    elif pesan_minuman == "EJ" :
        n3b = int(input("Silahkan Masukkan Jumlah Pesanan Anda : "))
        print("Nama Minuman : Es Jeruk\nHarga : Rp 5000")
        total_2b = 5000*n3b
    p = t + total_2b
    print("")
    print("------------------------------------------")
    print("Total Harga Makanan Anda : ", total_2b)
    print("------------------------------------------")
    print("\n")

elif plh == 3 :
    p = t
    print("\n")
    print("==================================")
    print("Total Harga Pesanan Anda : ", p)
    print("")
    raise SystemExit

    
