# -*- coding: utf-8 -*-
import os
a = os.listdir("C:\\Users\\hp\\Desktop\\Питон\\Шляпа") 
s = 0
f = open('result.txt', 'w')  
for b in a:
    bb=("C:\\Users\\hp\\Desktop\\Питон\\Шляпа\\" +b)
    c=open(bb)
    d=c.read()
    n=d.count("python")
    if n > 0:
        s += n
        f.write(b + str (n))
    else:
        f.write(b + str (0))
    c.close()
print (s)
f.close()
#import os
#a=os.path.join(f,fn)
