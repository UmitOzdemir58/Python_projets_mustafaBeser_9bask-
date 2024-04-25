QS='adi=mustafa&soyadi=beser&yas=40&ili=yozgat'
dic={}

for i in QS.split('&'):
    a=i.split('=')
    dic[a[0]]=a[1]
print(dic)