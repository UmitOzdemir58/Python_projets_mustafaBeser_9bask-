r=input('Çemberin yarıçapı:')
a=r.replace(',','.')
if a.count('.') in [0,1] and a.replace('.','').isnumeric():
    c=2*3.14*float(a)
    b=str(c).replace('.',',')

    print('Çemberin çevresi %s' %b)
else:
    print('Çemberin yarıçapı geçerli bir değer değil')