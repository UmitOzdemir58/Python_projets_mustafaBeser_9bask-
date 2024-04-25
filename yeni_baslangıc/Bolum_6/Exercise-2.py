print('------------------------ GUİDE ------------------------')
print('People search-       1')
print('persen registration -2 ')
print('Guide               -3')
print('Exit                -Q/q')
while 1:
    guide = open('d:/pydoc/telefonrehberi.txt')

    guidelist = []

    for i in guide:
        a = i.split('*')
        guidelist.append([a[0], a[1], int(a[2])])

    secim=input('Yapmak istediniz işlem:')

    if secim=='1':
        person=input("Aramak istediniz kişi'in adı:")
        for q in guidelist:
            if person==q[0]:
                print('kişi adı:',q[0],'    Soyadı:',q[1],'     Numarsı:',q[2])
                break
        else:
            print('Aradınız kişi bulunamadı')

    elif secim=='2':

        guide = open('d:/pydoc/telefonrehberi.txt','a')
        isim=input('Ad:')
        soyad=input('Soyad:')
        tleno=input('Telefon no:')

        kayit=('\n'+isim+'*'+soyad+'*'+tleno)

        guide.write(kayit)
        guide.close()





    elif secim=='3':
        print(" \n \n ---------------------------------------------------KİŞİLER----------------------------------------------")
        for kisi in guidelist:
            print(f'''
            -----------------------
            İsim:        {kisi[0]}
            Soyisim:     {kisi[1]}
            Telefon No:  {kisi[2]}
            -----------------------
        ''')  #burda f bize kolaylık sağlıyor birden kişi olfu zamn o listeyi bize seri bir şekilde yazdırıyor {} içine değişkenleri yazıyoruz ve konumlarnı!!!

    elif secim=='q' or secim=='Q':
        print('Çıkış yapılıyor...')
        break

    else:
        print('Hatalı işlem Yaptınız')


                                        #HATALAR , EKSİKLER  VE IVIR ZIVIRLAR
#Bu programı büyük ve küçük harf duyarlılığına getir
#
#
#
#