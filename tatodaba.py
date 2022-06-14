import random

mula = None

while mula != 0:
    nom1 = random.randint(1,10)
    nom2 = random.randint(1,10)
    print()
    print()

    print(" --------------------------------------------- ")
    print("|  SELAMAT DATANG KE PROGRAM T A T O D A B A  |")
    print(" --------------------------------------------- ")
    print()
    print("Anda akan diberi dua nombor secara rawak. Pilih operasi di bawah.")
    print("1. Operasi Tambah")
    print("2. Operasi Tolak")
    print("3. Operasi Darab")
    print("4. Operasi Bahagi")
    print()
    pilihan = int(input("Pilihan Anda: "))
    if pilihan == 1:
        jawapan = None
        hasiltambah = nom1 + nom2
        while jawapan != hasiltambah:
            print()
            print("OPERASI TAMBAH")
            print("--------------")
            print(nom1, "+", nom2, "= ?")
            jawapan = int(input("Jawapan anda: "))
            print()
            if jawapan != hasiltambah:
                print("Cuba lagi!")
                print()
            else:
                print("Tahniah, anda berjaya!")
                pilihan1 = int(input("Anda ingin teruskan dengan operasi lain? (0 = tamat, selain 0 = teruskan): "))
                if pilihan1 == 0:
                    mula = 0  
    elif pilihan == 2:
        jawapan = None
        hasiltolak = nom1 - nom2
        while jawapan != hasiltolak:
            print()
            print("OPERASI TOLAK")
            print("--------------")
            print(nom1, "-", nom2, "=")
            jawapan = int(input("Jawapan anda: "))
            print()
            if jawapan != hasiltolak:
                print("Cuba lagi!")
                print()
            else:
                print("Tahniah, anda berjaya!")
                pilihan1 = int(input("Anda ingin teruskan dengan operasi lain? (0 = tamat, selain 0 = teruskan): "))
                if pilihan1 == 0:
                    mula = 0  
    elif pilihan == 3:
        jawapan = None
        hasildarab = nom1 * nom2
        while jawapan != hasildarab:
            print()
            print("OPERASI DARAB")
            print("--------------")
            print(nom1, "x", nom2, "=")
            jawapan = int(input("Jawapan anda: "))
            print()
            if jawapan != hasildarab:
                print("Cuba lagi!")
                print()
            else:
                print("Tahniah, anda berjaya!")
                pilihan1 = int(input("Anda ingin teruskan dengan operasi lain? (0 = tamat, selain 0 = teruskan): "))
                if pilihan1 == 0:
                    mula = 0 
    elif pilihan == 4:
        jawapan = None
        hasilbahagi = round((nom1 / nom2), 2)
        while jawapan != hasilbahagi:
            print()
            print("OPERASI BAHAGI")
            print("--------------")
            print(nom1, "/", nom2, "=")
            jawapan = float(input("Jawapan anda (bundarkan 2 tempat perpuluhan): "))
            print()
            if jawapan != hasilbahagi:
                print("Cuba lagi!")
                print()
            else:
                print("Tahniah, anda berjaya!")
                pilihan1 = int(input("Anda ingin teruskan dengan operasi lain? (0 = tamat, selain 0 = teruskan): "))
                if pilihan1 == 0:
                    mula = 0 
    else:
        print("Pilihan anda salah. Masukkan pilihan yang betul")
