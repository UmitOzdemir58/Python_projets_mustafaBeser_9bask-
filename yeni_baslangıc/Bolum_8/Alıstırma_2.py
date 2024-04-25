import os
import time
klasor='C:/Program Files/Common Files/System'
file_stat=os.stat(klasor)
a=None
for i in os.listdir(klasor):
    dosya=os.path.join(klasor,i)
    durum=os.stat(dosya)
    a=len(i)
    if os.path.isdir(dosya):
        print('<file> ',time.ctime(durum.st_ctime),i)
    elif os.path.isdir(dosya):
        print('<folder> ',time.ctime(durum.st_ctime),i)

print('There are',int(a/2),'folders and files')
print('size:',file_stat.st_size)