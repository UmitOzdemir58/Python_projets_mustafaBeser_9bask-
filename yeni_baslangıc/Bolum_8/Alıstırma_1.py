import random

simgeler=['karo','Maça','Sinek','Kupa']
sayilar=[1,2,3,4,5,6,7,8,9,10,'Bacak','kız','Papaz']
kagitlar=[]

for i in simgeler:
    for j in sayilar:
        kagitlar.append(i+' '+str(j))   #simgeler ve sayıları eşleştiriyor

print(len(kagitlar),'Kağıt var. Her oyuncuya 13 tane rasgele dağıltıldı.')
 #Oyuncular
oyuncu1=[]
oyuncu2=[]
oyuncu3=[]
oyuncu4=[]
#for i in range(13): de her oyuncuya sırayala 1 kart verilecek ve toplam her oyuncuda 13 kart olacak
for i in range(13):
    #Oyuncu1
    kagit=random.choice(kagitlar)
    oyuncu1.append(kagit)
    kagitlar.remove(kagit)
    #Oyuncu2
    kagit = random.choice(kagitlar)
    oyuncu2.append(kagit)
    kagitlar.remove(kagit)
    #Oyuncu3
    kagit = random.choice(kagitlar)
    oyuncu3.append(kagit)
    kagitlar.remove(kagit)
    #Oyuncu4
    kagit = random.choice(kagitlar)
    oyuncu4.append(kagit)
    kagitlar.remove(kagit)

print("""
|----------------------------------------------------------|
|  Oyuncu 1    |  Oyuncu 2  |   Oyuncu 3  |   Oyuncu 4     |
|----------------------------------------------------------|
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
   {:<12}    {:<10}    {:<10}    {:<10}  
|----------------------------------------------------------|
""".format(oyuncu1[0], oyuncu2[0], oyuncu3[0], oyuncu4[0],
           oyuncu1[1], oyuncu2[1], oyuncu3[1], oyuncu4[1],
           oyuncu1[2], oyuncu2[2], oyuncu3[2], oyuncu4[2],
           oyuncu1[3], oyuncu2[3], oyuncu3[3], oyuncu4[3],
           oyuncu1[4], oyuncu2[4], oyuncu3[4], oyuncu4[4],
           oyuncu1[5], oyuncu2[5], oyuncu3[5], oyuncu4[5],
           oyuncu1[6], oyuncu2[6], oyuncu3[6], oyuncu4[6],
           oyuncu1[7], oyuncu2[7], oyuncu3[7], oyuncu4[7],
           oyuncu1[8], oyuncu2[8], oyuncu3[8], oyuncu4[8],
           oyuncu1[9], oyuncu2[9], oyuncu3[9], oyuncu4[9],
           oyuncu1[10], oyuncu2[10], oyuncu3[10], oyuncu4[10],
           oyuncu1[11], oyuncu2[11], oyuncu3[11], oyuncu4[11],
           oyuncu1[12], oyuncu2[12], oyuncu3[12], oyuncu4[12]))
