import math

def luasSegitiga() :
    alas = float(input("Masukkan nilai Alas : "))
    tinggi = float(input("Masukkan nilai Tinggi : "))
    luas = 0.5 * alas * tinggi
    print("Luas Segitiga adalah :", luas)

def luasPersegiPanjang() :
    panjang = float(input("Masukkan nilai Panjang : "))
    lebar = float(input("Masukkan nilai Lebar : "))
    luas = panjang * lebar
    print("Luas Persegi Panjang adalah : ", luas)

def luasLingkaran() :
    r = float(input("Masukkan nilai Jari-Jari : "))
    luas = math.pi * r ** 2
    print("Luas Lingkaran adalah : ", luas)

def luasTabung() :
    tinggi = float(input("Masukkan nilai tinggi : "))
    r = float(input("Masukkan nilai Jari-Jari : "))
    luas = 2 * math.pi * r * (r + tinggi)
    print("Luas Tabung adalah : ", luas)

while True :
    print("====== Menu Hitung Luas Bangun Datar ======")
    print("1. Segitiga.")
    print("2. Persegi Panjang.")
    print("3. Lingkaran.")
    print("4. Tabung.")
    print("5. Keluar.")
    pilihan = input("Pilih menu (1-5) : ")

    if pilihan == "1" :
        luasSegitiga()
    elif pilihan == "2" :
        luasPersegiPanjang()
    elif pilihan == "3" :
        luasLingkaran()
    elif pilihan == "4" :
        luasTabung()
    elif pilihan == "5" :
        print("Terima kasih! Selamat datang kembali ^-^")
        break
    else :
        print("Menu tidak ada! pilih kembali")
