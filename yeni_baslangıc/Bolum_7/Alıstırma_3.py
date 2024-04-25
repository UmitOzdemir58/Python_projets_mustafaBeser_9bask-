a=open('d:/pydoc/rasgele.txt').read()
ini = []
ini.append(a)
b=''''''
dicup = {}
gecici= None # None= boş veya atanmamış demek

for u in ini:
    b += u

for i in b.split('\n'):
    i=i.strip()
    if i.startswith('['):
        gecici=i
        dicup[gecici] = {}


    elif i.startswith(';'):
        pass

    else:

        for n in i.split('\n'):  # satır sonundan parçalar
            if n.strip() != '':   # '' tırnak varsa içeri girmez

                z,k=n.split('=')

                dicup[gecici][z.strip()]=k.strip()

print(dicup)


# son iki ahahtar değer de sorun var iki dict de aynı elemanlar var

# None= boş veya atanmamış demek



