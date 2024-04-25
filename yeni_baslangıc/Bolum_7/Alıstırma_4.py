#from collections import Counter  count benziyor daha iyisi -Counter-
print('''
LOG KAYIT İNCELEME SİSTEMİ

1-IP Erişim
2-Tarihsel işlem erişim
3-Saat işlem erişim
4-dsoya erişim
''')

#Dosya yapısı örneği  2024/04/29 11:20 - 192.168.1.181 - admin - Dosya Silme - sunum.ppt silindi.
#                        [1]tarih            [2]İP     [3]kul       [4]giris        [5]cıkıs

dosya=open('d:/pydoc/log.txt',encoding='utf-8')
liste = []
for i in dosya:
    liste.append(i)

secim=input('Secim yapınız:')
ipliste=[]
ip = None

def again(liste):
    sayac={}
    for eleman in liste:
        sayac[eleman]=sayac.get(eleman,0)+1 # eleman varsa 0 döndürür yoksa +1 ekler elman value

        sirali_sayac=sorted(sayac.items(), key=lambda x: x[1], reverse=True)
        return sirali_sayac



if secim == '1':
    # hangi ip kaç defa erişimiş ona bakacagız
    for i in liste:
        if i.strip() != '': # Tırnak varsa içeri giremez
            i.strip()
            ip= i.split('-')

            ipliste.append(ip[1])


    en_cok_tekrar_edenler = again(ipliste)
    print("En çok tekrar eden elemanlar:")
    for eleman, sayi in en_cok_tekrar_edenler:
        print(eleman, ":", sayi)





elif secim == '2':
    #dosya hangi gün ne zaman erişilmiş xadlı dosya şu zamanlarda eişilmiştir
    pass
elif secim == '3':
    #dosya hangi saatlerde kaç defa erişilmiş x dosyasına şu saatlerd eişilmiştir
    pass
elif secim == '4':
    #hangi dosya kaç defa erişilmiş x dosyasına y defa erişilmiş
    pass

else:
    #hatalı işlem
    pass
