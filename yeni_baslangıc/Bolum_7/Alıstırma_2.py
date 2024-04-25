ceviri={
    'ş':'s','Ş':'S',
    'ğ':'g','Ğ':'G',
    'ı':'i','İ':'I',
    'ü':'u','Ü':'U',
    'ö':'o','Ö':'O'
}

metin=input('Lütfen string(harf) metin giriniz: ')



cumle=''
for i in metin:
    if i in ceviri:
        a=ceviri[i]
        i=a

        cumle=cumle+i


    elif not i in ceviri:
        cumle = cumle + i
    continue


print(cumle)


#var ise değiş yok ise elif yap ordan değiştir