def menupembuka():
    import os
    os.system("CLS")
    print("""
    ==============================
        Program Matriks Dengan
            Eliminasi Gauss
    ==============================\n
    Pilih Yang Ingin Anda Cari:
    [1] Matriks 3 x 3 (3 Variabel Dicari)
    [2] Matriks 4 x 4 (4 Variabel Dicari)
    [3] Keluar\n
    """)
    pil = int(input("Silahkan Pilih : "))
    pilihanmenu(pil)

#----------------------------------------------------------
def pilihanmenu(pil):
    import os
    if pil == 1:
        jumlahvariabel_3()
    elif pil == 2:
        jumlahvariabel_4()
    elif pil == 3:
        os.system("CLS")
        print("""
        ==================================================
            Terima Kasih Telah Menggunakan Program Ini
        ==================================================
        """)
        exit()

#----------------------------------------------------------

# Jika Jumlah Variabel yang Dicari = 3
def jumlahvariabel_3():
    import os
    os.system("CLS")
    baris1 = []
    baris2 = []
    baris3 = []

    p = 11
    q = 21
    r = 31

    print("\n")
    print("              \xB1\xB1 BARIS PERTAMA \xB1\xB1           ")
    print("--------------------------------------------------------")
    for i in range(4):
        print("Masukan angka matriks pada baris pertama","(","a",p,")", ":", end = " ")
        baris1.append(float(input()))
        p += 1

    print("\n")
    print("               \xB1\xB1 BARIS KEDUA \xB1\xB1            ")
    print("--------------------------------------------------------")
    for i in range(4):
        print("Masukan angka matriks pada baris pertama","(","a",q,")", ":", end = " ")
        baris2.append(float(input()))
        q += 1

    print("\n")
    print("              \xB1\xB1 BARIS KETIGA \xB1\xB1            ")
    print("--------------------------------------------------------")
    for i in range(4):
        print("Masukan angka matriks pada baris pertama","(","a",r,")", ":", end = " ")
        baris3.append(float(input()))
        r += 1


    print("\n\n")
    print("Berikut Adalah Matriks Anda")
    print("---------------------------\n")
    print("|",   baris1[0],"\t ", baris1[1],"\t",baris1[2],"\t",baris1[3],"\t", "|")
    print("|",   baris2[0],"\t ", baris2[1],"\t",baris2[2],"\t",baris2[3],"\t", "|")
    print("|",   baris3[0],"\t ", baris3[1],"\t",baris3[2],"\t",baris3[3],"\t", "|")
    input("\nTekan [ENTER] Untuk Melanjutkan Program")
    print("\n\n")

    # Iterasi Pertama
    ## Baris Kedua
    a21_1 = baris2[0]-(baris2[0]/baris1[0])*baris1[0]
    a22_1 = baris2[1]-(baris2[0]/baris1[0])*baris1[1]
    a23_1 = baris2[2]-(baris2[0]/baris1[0])*baris1[2]
    a24_1 = baris2[3]-(baris2[0]/baris1[0])*baris1[3]
    
    ## Baris Ketiga
    a31_1 = baris3[0]-(baris3[0]/baris1[0])*baris1[0]
    a32_1 = baris3[1]-(baris3[0]/baris1[0])*baris1[1]
    a33_1 = baris3[2]-(baris3[0]/baris1[0])*baris1[2]
    a34_1 = baris3[3]-(baris3[0]/baris1[0])*baris1[3]


    # Iterasi Kedua
    ## Baris Ketiga
    a32_2 = a32_1-(a32_1/a22_1)*a22_1
    a33_2 = a33_1-(a32_1/a22_1)*a23_1
    a34_2 = a34_1-(a32_1/a22_1)*a24_1


    # Hasil Nilai Variabel 
    C = a34_2/a33_2
    B = (a24_1-(a23_1*C))/a22_1
    A = (baris1[3]-(baris1[2]*C)-(baris1[1]*B))/baris1[0]


    # Format Penulisan Hasil
    print("\n")
    print("Nilai Variabel yang Anda Dapatkan Sebagai Berikut")
    print("-------------------------------------------------")
    print("\n")
    print("A = ",format(A, '.2f'), "  B = ",format(B, '.2f'), "  C = ", format(C, '.2f'))
    input("\nTekan [ENTER] Untuk Melanjutkan Program")

    # Kembali ke menu
    os.system("CLS")
    print("\n--------------------------------------")
    print("Perhitungan Program Anda Telah Selesai")
    print("--------------------------------------")
    print("""
    \nApakah Anda Ingin Kembali ke Menu Utama?
    (1) Ya
    (2) Tidak, keluar saja\n
    """)
    pilihan = input("Silahkan Pilih : ")
    if pilihan == "ya" or "Ya" or 1:
        menupembuka()
    elif pilihan == "tidak" or "Tidak" or "tidak, keluar saja" or 2:
        os.system("CLS")
        print("""
        ==================================================
            Terima Kasih Telah Menggunakan Program Ini
        ==================================================
        """)
        exit()


#----------------------------------------------------------

# Jika Jumlah Variabel yang Dicari = 4
def jumlahvariabel_4():
    import os
    os.system("CLS")
    baris1 = []
    baris2 = []
    baris3 = []
    baris4 = []

    p = 11
    q = 21
    r = 31
    s = 41

    print("\n")
    print("              \xB1\xB1 BARIS PERTAMA \xB1\xB1           ")
    print("--------------------------------------------------------")
    for i in range(5):
        print("Masukan angka matriks pada baris pertama","(","a",p,")", ":", end = " ")
        baris1.append(float(input()))
        p += 1

    print("\n")
    print("               \xB1\xB1 BARIS KEDUA \xB1\xB1            ")
    print("--------------------------------------------------------")
    for i in range(5):
        print("Masukan angka matriks pada baris pertama","(","a",q,")", ":", end = " ")
        baris2.append(float(input()))
        q += 1

    print("\n")
    print("              \xB1\xB1 BARIS KETIGA \xB1\xB1            ")
    print("--------------------------------------------------------")
    for i in range(5):
        print("Masukan angka matriks pada baris pertama","(","a",r,")", ":", end = " ")
        baris3.append(float(input()))
        r += 1

    print("\n")
    print("             \xB1\xB1 BARIS KEEMPAT \xB1\xB1            ")
    print("--------------------------------------------------------")
    for i in range(5):
        print("Masukan angka matriks pada baris pertama","(","a",r,")", ":", end = " ")
        baris4.append(float(input()))
        s += 1

    print("\n\n")
    print("Berikut Adalah Matriks Anda")
    print("---------------------------\n")
    print("|",  baris1[0],"\t ", baris1[1],"\t",baris1[2],"\t",baris1[3],"\t",baris1[4], "|")
    print("|",  baris2[0],"\t ", baris2[1],"\t",baris2[2],"\t",baris2[3],"\t",baris2[4], "|")
    print("|",  baris3[0],"\t ", baris3[1],"\t",baris3[2],"\t",baris3[3],"\t",baris3[4], "|")
    print("|",  baris4[0],"\t ", baris4[1],"\t",baris4[2],"\t",baris4[3],"\t",baris4[4], "|")
    input("\nTekan [ENTER] Untuk Melanjutkan Program")
    print("\n\n")

    # Iterasi Pertama
    ## Baris Kedua
    a21_1 = baris2[0]-(baris2[0]/baris1[0])*baris1[0]
    a22_1 = baris2[1]-(baris2[0]/baris1[0])*baris1[1]
    a23_1 = baris2[2]-(baris2[0]/baris1[0])*baris1[2]
    a24_1 = baris2[3]-(baris2[0]/baris1[0])*baris1[3]
    a25_1 = baris2[4]-(baris2[0]/baris1[0])*baris1[4]
    
    ## Baris Ketiga
    a31_1 = baris3[0]-(baris3[0]/baris1[0])*baris1[0]
    a32_1 = baris3[1]-(baris3[0]/baris1[0])*baris1[1]
    a33_1 = baris3[2]-(baris3[0]/baris1[0])*baris1[2]
    a34_1 = baris3[3]-(baris3[0]/baris1[0])*baris1[3]
    a35_1 = baris3[4]-(baris3[0]/baris1[0])*baris1[4]

    ## Baris Keempat
    a41_1 = baris4[0]-(baris4[0]/baris1[0])*baris1[0]
    a42_1 = baris4[1]-(baris4[0]/baris1[0])*baris1[1]
    a43_1 = baris4[2]-(baris4[0]/baris1[0])*baris1[2]
    a44_1 = baris4[3]-(baris4[0]/baris1[0])*baris1[3]
    a45_1 = baris4[4]-(baris4[0]/baris1[0])*baris1[4]

    # Iterasi Kedua
    ## Baris Ketiga
    a32_2 = a32_1-(a32_1/a22_1)*a22_1
    a33_2 = a33_1-(a32_1/a22_1)*a23_1
    a34_2 = a34_1-(a32_1/a22_1)*a24_1
    a35_2 = a35_1-(a32_1/a22_1)*a25_1

    ## Baris Keempat
    a42_2 = a42_1-(a42_1/a22_1)*a22_1
    a43_2 = a43_1-(a42_1/a22_1)*a23_1
    a44_2 = a44_1-(a42_1/a22_1)*a24_1
    a45_2 = a45_1-(a42_1/a22_1)*a25_1

    # Iterasi Ketiga
    ## Baris Keempat
    a43_3 = a43_2-(a43_2/a33_2)*a33_2
    a44_3 = a44_2-(a43_2/a33_2)*a34_2
    a45_3 = a45_2-(a43_2/a33_2)*a35_2

    # Hasil Nilai Variabel 
    D = a45_3/a44_3
    C = (a35_2-(a34_2*D))/a33_2
    B = (a25_1-(a24_1*D)-(a23_1*C))/a22_1
    A = (baris1[4]-(baris1[3]*D)-(baris1[2]*C)-(baris1[1]*B))/baris1[0]


    # Format Penulisan Hasil
    print("\n\n")
    print("Nilai Variabel yang Anda Dapatkan Sebagai Berikut")
    print("-------------------------------------------------")
    print("\n")
    print("A = ",format(A, '.2f'), "  B = ",format(B, '.2f'), "  C = ", format(C, '.2f'), "  D = ", format(D, '.2f'))
    input("\nTekan [ENTER] Untuk Melanjutkan Program")

    # Kembali ke menuutama
    os.system("CLS")
    print("\n--------------------------------------")
    print("Perhitungan Program Anda Telah Selesai")
    print("--------------------------------------")
    print("""
    \nApakah Anda Ingin Kembali ke Menu Utama?
    (1) Ya
    (2) Tidak, keluar saja\n
    """)
    pilihan = input("Silahkan Pilih : ")
    if pilihan == "ya" or "Ya" or 1:
        menupembuka()
    elif pilihan == "tidak" or "Tidak" or "tidak, keluar saja" or 2:
        os.system("CLS")
        print("""
        ==================================================
            Terima Kasih Telah Menggunakan Program Ini
        ==================================================
        """)
        exit()


