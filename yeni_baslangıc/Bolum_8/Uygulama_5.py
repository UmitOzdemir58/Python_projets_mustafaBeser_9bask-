import sys

try:
    isimler = sys.argv[1:]
    for isim in isimler:
        print(isim)
except IndexError:
    print("Hata: Eksik giriş. Lütfen bir veya daha fazla isim girin.")
