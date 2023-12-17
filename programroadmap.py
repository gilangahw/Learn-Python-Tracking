import os
def menuutama():
    import os
    os.system("CLS")
    print("""
    ===================================
        Progres Belajar Python dari 
           Youtube Kelas Terbuka
    ===================================\n
    Daftar Menu:
    [1] Lihat Progres
    [2] Tambah Progres
    [3] Cari Progres
    [4] Hapus Progres
    [5] Update Progres\n
    """)
    pil = int(input("Silahkan pilih menu : "))
    pilihanmenu(pil)
#-----------------------------------------------------
def pilihanmenu(pil):
    if pil == 1:
        lihatprogres()
    elif pil == 2:
        tambahprogres()
    elif pil == 3:
        cariprogres()
    elif pil == 4:
        hapusprogres()
    else:
        print("Anda Telah Keluar Dari Program")
        raise SystemExit
#-----------------------------------------------------
def lihatprogres():
    print("\n=== Berikut Adalah Data Progres Anda ===\n")
    buka = open("roadmappython.txt")
    isi = buka.readlines()
    isi.sort()

    if len(isi) != 0:
        print("\tEpisode\t\t       Progres\t\t\tJudul")
        print("---------------------------------------------------------------------------------------------------------")
        for x in isi:
            pecah = x.split(",")
            print("     Episode ke : "+pecah[0]+"\t\t"+pecah[1]+"\t\t\t"+pecah[2])

    elif len(isi) == 0:
        print("=== Data Progres Anda Masih Kosong ===")
        
    buka.close()
    print("\n\nTekan [Enter] Untuk Kembali ke Menu")
    input()
    menuutama()
#-----------------------------------------------------
def tambahprogres():
    print("\n=== Silahkan Tambah Progres Baru Anda ===\n")
    buka = open("roadmappython.txt", "a")
    e = int(input("Episode ke                   : "))
    j = input("Silahkan Masukkan Judul Anda : ")
    p = input("Status Progres               : ")
    buka.writelines(str(e)+","+j+","+p+"\n")
    print("\nTekan [Enter] Untuk Kembali ke Menu")
    buka.close()
    input()
    menuutama()

#-----------------------------------------------------
def cariprogres():
    os.system("CLS")
    print("\n=== Anda Berada di Menu Cari Progres ===\n")
    buka = open("roadmappython.txt")
    bacaisi = buka.readlines()
    mencari = int(input("Silahkan Masukan Episode yang Ingin Anda Cari : "))
    dataepisode = []
    for x in bacaisi:
        pecah = x.split(",")
        if str(mencari) in pecah[0]:
            dataepisode = pecah
            print("\n")
            print("\tEpisode\t\t       Progres\t\t\tJudul")
            print("---------------------------------------------------------------------------------------------------------")
            print("     Episode ke : "+dataepisode[0]+"\t\t"+dataepisode[1]+"\t\t\t"+dataepisode[2])
            break
    
    stringjoin = ",".join(bacaisi)
    listsplit = stringjoin.split(",")
    
    if str(mencari) not in listsplit:
        os.system("CLS")
        print("\n\n\n>>> Data Anda Tidak Ditemukan <<<\n\n\n")

    buka.close()
    print("\nTekan [Enter] Untuk Kembali ke Menu")
    input()
    menuutama()

#-----------------------------------------------------
def hapusprogres():
    import os
    print("\n=== Anda Berada di Menu Hapus Progres ===\n")
    buka = open("roadmappython.txt", "r+")
    bacaisi = buka.readlines()
    dataepisode = []
    print("\tEpisode\t\t       Progres\t\t\tJudul")
    print("---------------------------------------------------------------------------------------------------------")
    for x in bacaisi:
        pecah = x.split(",")
        print("     Episode ke : "+pecah[0]+"\t\t"+pecah[1]+"\t\t\t"+pecah[2])

    mencaridata = int(input("\n\nSilahkan Pilih Episode yang Ingin Dihapus Dari Progres : "))
    print()
    os.system("cls")
    buka.close()

    buka = open("roadmappython.txt")
    bacaisi = buka.readlines()
    for x in bacaisi:
        pecah = x.split(",")

        if str(mencaridata) in pecah[0]:
            dataepisode = pecah
            print("\tEpisode\t\t       Progres\t\t\tJudul")
            print("----------------------------------------------------------------------------------------")
            print("     Episode ke : "+dataepisode[0]+"\t\t"+dataepisode[1]+"\t\t\t"+dataepisode[2]+"\n")
    
    buka.close()
    buka = open("roadmappython.txt")
    bacaisi = buka.readlines()
    pecahstring = ",".join(bacaisi)
    gabunglist = pecahstring.split(",")
    panjangisi = len(gabunglist)
    yakinhapus = input("Apakah Anda Yakin Ingin Menghapus Data Ini?  ")
    print()
            
    if yakinhapus == "ya" or "Ya" or "y":
        for i in range(panjangisi):
            if gabunglist[i] == str(mencaridata):
                del gabunglist[i]
                del gabunglist[i]
                del gabunglist[i]
                pecahlagi = ",".join(gabunglist)
                gabunglagi = pecahlagi.splitlines()
                break
    buka.close()

    buka = open("roadmappython.txt", "w")
    buka.writelines(gabunglagi)
    buka.close()
        
    buka = open("roadmappython.txt", "w")
    for i in gabunglagi:
        pecah2 = i.split(",")
        if len(pecah2) == 4:
            del pecah2[0]

        panjangkalimat = len(pecah2)

        for i in range(panjangkalimat):
            x = pecah2[i:3]
            gabung3 = ",".join(x)
            pecah3 = gabung3.splitlines()
            buka.writelines(pecah3 + list("\n"))
            break
    
    buka.close()
    os.system("CLS")
    print("\n>>> Data Anda Berhasil Dihapus <<<\n\n")
    print("Tekan [Enter] Untuk Kembali ke Menu")
    input()
    menuutama()
        
menuutama()

