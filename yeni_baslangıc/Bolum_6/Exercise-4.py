import os
menu=print("""              ****************************************ÖZDEMİR TUR****************************************
              **                                                                                       **
              **                                      Koltuklar   -1                                   **
              **                                      Yolcu ekleme-2                                   **
              **                                      Çıkış       -E                                   **
              **                                                                                       **
              *******************************************************************************************


""")


#Program başlamadaan önce dosya kontrolü yapıyor yok ise dosya bulunamadı esle ile uyarı verecek
q=os.path.exists('d:/pydoc/bus.txt')
if q==True:

    while 1 :

        B=open('d:/pydoc/bus.txt')
        koltuk=[]
        koltuk2=[]
        for i in B:
            ii=i.replace(' ','')
            iii=ii.strip()
            koltuk.append(iii)
            if len(koltuk) == 6:        #burda boytunu bildirmeme mecbur kıldı  burayı anla !!!
                a=str(koltuk[0]+koltuk[1]+koltuk[2]+koltuk[3]+koltuk[4]+koltuk[5])
                koltuk2.append(a)

        secim=input('İşlem seçiniz:')

        if secim=='1':
            B = open('d:/pydoc/bus.txt')
            a=B.read()
            print('KOLTUKLAR')

            print(a)

        elif secim=='2':
            A=[]

            for h in koltuk2[0]:
                A.append(h)
            seckol=int(input('Koltuk seçiniz:'))

            if  not A[seckol-1]==  'x':
                A[seckol - 1]='x'
                gurpkoltuk=[A[0]+A[1]+' '+A[2]+A[3]+'\n',
                            A[4]+A[5]+' '+A[6]+A[7]+'\n',
                            A[8]+A[9]+' '+A[10]+A[11]+'\n',
                            A[12]+A[13]+' '+A[14]+A[15]+'\n',
                            A[16]+A[17]+' '+A[18]+A[19]+'\n',
                            A[20]+A[21]+' '+A[22]+A[23]]
                B = open('d:/pydoc/bus.txt', 'w')
                B.close()
                for a in gurpkoltuk:
                    aa=a.strip()
                    B = open('d:/pydoc/bus.txt','a')
                    B.write(aa+'\n')
                    B.close()


            else:
                print('seçilen koltuk dolu.')


        elif secim=='E' or secim=='e':
            print('Program sonlanıyor...')
            break
        else:
            print('Hatalı seçim yaptınız.')
else:
    print('Dosya bulunamadı')