yerlesimyerleri = ['Bolu', 'Yozgat', 'inebolu', 'Manavgat', 'Çanakkale', 'çan', 'Kırıkkale', 'Tirebolucuk']

def ara(kelime, altkelime):  #gircegimiz input alt kelime
    if altkelime[0] == '*' and altkelime[-1] == '*':
        kucuk = kelime.lower()
        if kucuk.find(altkelime[1:-1].lower()) != -1:   #burda != -1 ifadesi tam anlaşılamadı burayı anlayana kadar araştır ve kullanım şekli çok önemli eğer sonuç bulunduysa ekrana çıktı alır.
            return kelime
    else:
        if kelime == altkelime:
            return kelime

def bul(altkelime):
    for u in yerlesimyerleri:
        r = ara(u, altkelime)
        if r:
            print(r)

aranacakkelime = input('Aramak istediğiniz yerleşim yeri:')
bul(aranacakkelime)
