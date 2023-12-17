# Program mencari momen primer, reaksi dan momen maksimal
# Momen pada titik yang ditinjau, geser  maksimum, geser
# Pada titik yang ditinjau pada struktur jepit-sendi dan 
# Mencari tegangan lentur dan tegangan geser pada penampang komposit

# Pembukaan
print("""
**************************************************************
***                 >>> Selamat Datang<<<                  ***
***           Program Mencari Reaksi Momen Primer          ***
***          Momen Maksimal, Geser, Geser Maksimum         ***
***                Pada Titik Yang Ditinjau                ***
***           Ditinjau Pada Struktur Jepit Sendi           ***
***        Dan Mencari Tegangan Lentur Serta Geser         ***
***                Pada Penampang Komposit                 ***      
***                                                        ***
***                      Disusun Oleh                      ***
***        Gilang Fathir Ahwadzi (215060100111047)         ***
***                                                        ***
***                     Dosen Pengampu                     ***
***               R. IR. Hendro Suseno, DEA                ***
***                                                        ***
***            Tugas Akhir Pemrograman Komputer            ***
***                 Universitas Brawijaya                  ***
***                    Fakultas Teknik                     ***
***                Departemen Teknik Sipil                 ***
***                        Malang                          ***
**************************************************************

""")

print("""
*************************************
    Selamat Datang di Program SJS   
*************************************
""")

# import library python untuk manipulasi script dan fungsi
import os
def pause():
    os.system("pause")
import math

while True:
    print("Apakah Anda Siap Memasuki Perhitungan Program Ini?")
    print("Pilih 1 Jika Anda Siap")
    print("Pilih 9 Jika Anda Ingin Keluar Dari Program Ini")

    # input nilai
    lanjut_program = int(input("Silahkan Masukkan Pilihan Anda : "))
    if lanjut_program == 1 :
        print("\n")
        sl = int(input("Silahkan Masukkan Nilai Panjang Bentang Keseluruhan : "))
        sa = int(input("Silahkan Masukkan Nilai Panjang Sebagian Bentang Dari Kiri : "))
        q = int(input("Silahkan Masukkan Nilai Beban Merata Segitiga : "))
        p = int(input("Silahkan Masukkan Nilai Beban Terpusat : "))
        x = int(input("Silahkan Masukkan Titik Yang Ingin Ditinjau : "))
    elif lanjut_program == 9 :
        raise SystemExit

    # konfirmasi nilai inputan
    print("""
    """)
    print("*********************************")
    print("* Berikut Hasil Input Data Anda *")
    print("*********************************")
    print("")
    print("SL :", sl, "Meter" )
    print("SA :", sa, "Meter" )
    print("Q :", q, "Kilogram/Meter" )
    print("P :", p, "Kilogram/Meter" )
    print("x :", x, "Meter" "\n\n" )
    pause()

    # memulai perhitungan reaksi
    print("==================================")
    print(" Anda Berada di Subprogram SBSSBT ")
    print("==================================\n\n")

    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan FMAB Selesai  <<  ")
    print("**---------------------------------------**")
    fmab = -q*(sa**2)/2*(sa/sl/5-3*sa/sl/4+0.66666667)-p*(sl-sa)*(sl**2-(sl-sa)**2)*1/2*1/(sl**2)
    print("")
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan RA Selesai  <<  ")
    print("**-------------------------------------**")
    ra = q*sl*1/6-fmab/sl+p/2
    print("")
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan RB Selesai  <<  ")
    print("**-------------------------------------**")
    rb = q*sl*1/12+fmab/sl+p*1/2
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan FMAX Selesai  <<  ")
    print("**---------------------------------------**")
    fmax = ra*(math.sqrt(ra*sl*1/q))-q*1/3*1/sl*((math.sqrt(ra*sl*1/q))**3)+fmab
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan DMAX Selesai  <<  ")
    print("**---------------------------------------**")
    dmax = ra
    print("\n")

    #   percabangan untuk perhitungan fmx dan dx
    if x < sl/2 :
        print("**--------------------------------------**")
        print("  >>  Proses Perhitungan FMX Selesai  <<  ")
        print("**--------------------------------------**")
        fmx = ra*x-q*(x**3)*1/3*1/sl+fmab
        print("")
        print("**-------------------------------------**")
        print("  >>  Proses Perhitungan DX Selesai  <<  ")
        print("**-------------------------------------**")
        dx = ra-q*(x**2)*1/sl
        print("\n")
    elif x > sl/2 :
        print("**--------------------------------------**")
        print("  >>  Proses Perhitungan FMX Selesai  <<  ")
        print("**--------------------------------------**")
        fmx = rb*(sl-x)
        print("")
        print("**-------------------------------------**")
        print("  >>  Proses Perhitungan DX Selesai  <<  ")
        print("**-------------------------------------**")
        dx = -rb
        print("\n\n")
    pause()

    # memulai perhitungan tegangan lentur dan geser
    ## input nilai dari user
    print("================================")
    print(" Anda Berada di Subprogram TLTG ")
    print("================================\n\n")

    print("--------------------------")
    b = float(input("Silahkan Masukkan Nilai\nPanjang Alas Penampang (B)\n(Dalam Satuan Meter)\n"))
    print("--------------------------")
    h1 = float(input("Silahkan Masukkan Nilai\nTinggi Penampang 1 (H1)\n(Dalam Satuan Meter)\n"))
    print("--------------------------")
    h2 = float(input("Silahkan Masukkan Nilai\nTinggi Penampang 2 (H2)\n(Dalam Satuan Meter)\n"))
    print("------------------------------------")                                 
    e1 = float(input("Silahkan Masukkan Nilai\nModulus Elastisitas Penampang 1 (E1)\n(Dalam Satuan Kilogram/Meter^2)\n"))
    print("------------------------------------")                                 
    e2 = float(input("Silahkan Masukkan Nilai\nModulus Elastisitas Penampang 2 (E2)\n(Dalam Satuan Kilogram/Meter^2)\n"))

    ## proses perhitungan nilai-nilai kebutuhan untuk menghitung tegangan lentur dan geser
    bkb = e1/e2
    if e2 > e1 :
        b1 = b
        b2 = b*bkb
    elif e2 < e1 :
        b1 = b*bkb
        b2 = b

    print("\n")
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan A1 Selesai  <<  ")
    print("**-------------------------------------**")
    a1 = b1*h1
    print("")
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan A2 Selesai  <<  ")
    print("**-------------------------------------**")
    a2 = b2*h2
    print("")
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan X1 Selesai  <<  ")
    print("**-------------------------------------**")
    x1 = b1/2
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan X2 Selesai  <<  ")
    print("**-------------------------------------**")
    x2 = b1/2
    print("")
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan Y1 Selesai  <<  ")
    print("**-------------------------------------**")
    y1 = h1+h2+(h1/2)
    print("")
    print("**-------------------------------------**")
    print("  >>  Proses Perhitungan Y2 Selesai  <<  ")
    print("**-------------------------------------**")
    y2 = h1+(h2/2)
    print("")
    print("**--------------------------------------**")
    print("  >>  Proses Perhitungan TBX Selesai  <<  ")
    print("**--------------------------------------**")
    tbx = ((a1*x1)+(a2*x2))/(a1+a2)
    print("")
    print("**--------------------------------------**")
    print("  >>  Proses Perhitungan TBY Selesai  <<  ")
    print("**--------------------------------------**")
    tby = ((a1*y1)+(a2*y2))/(a1+a2)
    print("")
    print("**----------------------------------------**")
    print("  >>  Proses Perhitungan ZIMAX Selesai  <<  ")
    print("**----------------------------------------**")
    zimax1 = a1*((tby-y1)**2)+b1*(h1**3)*1/12
    zimax2 = a2*((tby-y2)**2)+b2*(h2**3)*1/12
    zimax = zimax1 + zimax2
    print("\n\n")
    pause()

    ## perhitungan tegangan lentur dan geser
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TLAA Selesai  <<  ")
    print("**---------------------------------------**")
    tlaa = -fmax*(h1+(h2/2))*(1/zimax)
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TLBB Selesai  <<  ")
    print("**---------------------------------------**")
    tlbb = -fmax*(h2/2)*1/zimax
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TLCC Selesai  <<  ")
    print("**---------------------------------------**")
    tlcc = tlbb*bkb
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TLDD Selesai  <<  ")
    print("**---------------------------------------**")
    tldd = -tlbb*bkb
    print("")
    print("**----------------------------------------**")
    print("  >>  Proses Perhitungan TLMAX Selesai  <<  ")
    print("**----------------------------------------**")
    tlmax = -tlbb*bkb
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TGAA Selesai  <<  ")
    print("**---------------------------------------**")
    tgaa = dmax*0*(h1/2+h2/2)*(1/zimax)*(1/b1)
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TGBB Selesai  <<  ")
    print("**---------------------------------------**")
    tgbb = dmax*a1*(h1/2+h2/2)*(1/zimax)*(1/b1)
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TGCC Selesai  <<  ")
    print("**---------------------------------------**")
    tgcc = dmax*a1*(h1/2+h2/2)*(1/zimax)*(1/b2)
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TGNN Selesai  <<  ")
    print("**---------------------------------------**")
    tgnn = dmax*((a2/2*h2/4)+a1*(h1/2+h2/2))*(1/zimax)*(1/b2)
    print("")
    print("**---------------------------------------**")
    print("  >>  Proses Perhitungan TGDD Selesai  <<  ")
    print("**---------------------------------------**")
    tgdd = dmax*a1*(h1/2+h2/2)*(1/zimax)*(1/b2)
    print("\n\n")
    pause()


    # menampilkan hasil
    print("=================================")
    print(" Anda Berada di Subprogram Hasil ")
    print("=================================")
    print("")
    print("")
    print("------------------------------------------")
    print(" Hasil Perhitungan Reaksi di Titik A (RA) ")
    print("------------------------------------------")
    print("     RA = ", format(ra, '.2f'), "Kilogram")
    print("==========================================")
    print("")
    print("------------------------------------------")
    print(" Hasil Perhitungan Reaksi di Titik B (RB) ")
    print("------------------------------------------")
    print("     RB = ", format(rb, '.2f'), "Kilogram")
    print("==========================================")
    print("")
    print("-------------------------------------------")
    print(" Hasil Perhitungan Momen di Titik A (FMAB) ")
    print("-------------------------------------------")
    print("     FMAB = ", format(fmab, '.2f'), "Kilogram.Meter")
    print("===========================================")
    print("")
    print("-----------------------------------------")
    print(" Hasil Perhitungan Momen Maksimum (FMAX) ")
    print("-----------------------------------------")
    print("     FMAX = ", format(fmax, '.2f'), "Kilogram.Meter")
    print("=========================================")
    print("")
    print("-----------------------------------------")
    print(" Hasil Perhitungan Geser Maksimum (DMAX) ")
    print("-----------------------------------------")
    print("     DMAX = ", format(dmax, '.2f'), "Kilogram")
    print("=========================================")
    print("")
    print("-----------------------------------------")
    print("           Hasil Perhitungan FMX         ")
    print("-----------------------------------------")
    print("     FMX = ", format(fmx, '.2f'), "Kilogram.Meter")
    print("=========================================")
    print("")
    print("-----------------------------------------")
    print("           Hasil Perhitungan DX          ")
    print("-----------------------------------------")
    print("     DX = ", format(dx, '.2f'), "Kilogram")
    print("=========================================")
    print("")
    print("------------------------------------------")
    print(" Hasil Perhitungan Tegangan Lentur (TLAA) ")
    print("------------------------------------------")
    print("     TLAA = ", format(tlaa, '.2f'), "Kilogram/Meter^2")
    print("==========================================")
    print("")
    print("------------------------------------------")
    print(" Hasil Perhitungan Tegangan Lentur (TLBB) ")
    print("------------------------------------------")
    print("     TLBB = ", format(tlbb, '.2f'), "Kilogram/Meter^2")
    print("==========================================")
    print("")
    print("------------------------------------------")
    print(" Hasil Perhitungan Tegangan Lentur (TLCC) ")
    print("------------------------------------------")
    print("     TLCC = ", format(tlcc, '.2f'), "Kilogram/Meter^2")
    print("==========================================")
    print("")
    print("------------------------------------------")
    print(" Hasil Perhitungan Tegangan Lentur (TLDD) ")
    print("------------------------------------------")
    print("     TLDD = ", format(tldd, '.2f'), "Kilogram/Meter^2")
    print("==========================================")
    print("")
    print("-------------------------------------------")
    print(" Hasil Perhitungan Tegangan Lentur (TLMAX) ")
    print("-------------------------------------------")
    print("     TLMAX = ", format(tlmax, '.2f'), "Kilogram/Meter^2")
    print("===========================================")
    print("")
    print("-----------------------------------------")
    print(" Hasil Perhitungan Tegangan Geser (TGAA) ")
    print("-----------------------------------------")
    print("     TGAA = ", format(tgaa, '.2f'), "Kilogram/Meter^2")
    print("=========================================")
    print("")
    print("-----------------------------------------")
    print(" Hasil Perhitungan Tegangan Geser (TGBB) ")
    print("-----------------------------------------")
    print("     TGBB = ", format(tgbb, '.2f'), "Kilogram/Meter^2")
    print("=========================================")
    print("")
    print("-----------------------------------------")
    print(" Hasil Perhitungan Tegangan Geser (TGCC) ")
    print("-----------------------------------------")
    print("     TGCC = ", format(tgcc, '.2f'), "Kilogram/Meter^2")
    print("=========================================")
    print("")
    print("-----------------------------------------")
    print(" Hasil Perhitungan Tegangan Geser (TGNN) ")
    print("-----------------------------------------")
    print("     TGNN = ", format(tgnn, '.2f'),"Kilogram/Meter^2")
    print("=========================================")
    print("")
    print("-----------------------------------------")
    print(" Hasil Perhitungan Tegangan Geser (TGDD) ")
    print("-----------------------------------------")
    print("     TGDD = ", format(tgdd, '.2f'),"Kilogram/Meter^2")
    print("=========================================")
    print("\n\n")
    pause()

    # fungsi penutup
    def selesai():
        print("\n\n")
        print("    Sekian Hasil Perhitungan program Kami   ")
        print("")
        print("============================================")
        print(" Terima Kasih Telah Menggunakan Program Ini ")
        print("============================================")
        raise SystemExit

    # konfirmasi pengulangan perhitungan
    print("==========================================")
    print("       Perhitungan Anda Telah Selesai     ")
    print(" Apakah Anda Ingin Mengulang Perhitungan? ")
    print("==========================================")
    print("")
    print("1. Ya, Saya Ingin Mengulang Perhitungan\n2. Tidak, Saya Ingin Keluar Dari Program")
    n = int(input("Silahkan Masukkan Pilihan Anda : "))
    if n == 1:
        True
        print("\n")
    elif n == 2:
        selesai()

   





    

