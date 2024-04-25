F=open('d:/ddk/kitap.txt')

kitaplarlistesi=[]

for i in F:
    ls=i.strip()
    ll=ls.split(':')

    kitaplarlistesi.append([int(ll[0]),ll[1],ll[2],ll[3],int(ll[4])])

F.close()

print(kitaplarlistesi)
