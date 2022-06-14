import random

mula = None

while mula != 0:
    nom1 = random.randint(1,10)
    nom2 = random.randint(1,10)
    print()
    print()

    print("Program ini akan membuat operasi matematik pada dua nombor rawak berdasarkan menu berikut.")
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
            print(nom1, "+", nom2, "=")
            jawapan = int(input("Jawapan anda: "))
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
            print(nom1, "-", nom2, "=")
            jawapan = int(input("Jawapan anda: "))
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
            print(nom1, "x", nom2, "=")
            jawapan = int(input("Jawapan anda: "))
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
        hasilbahagi = round((nom1 / nom2),2)
        while jawapan != hasilbahagi:
            print(nom1, "/", nom2, "=")
            jawapan = float(input("Jawapan anda: "))
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
