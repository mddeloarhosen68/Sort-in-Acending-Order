from array import *

#Ex:1
values = array('i',[33,44,22,11])
print(sorted(values))

#Ex:2
vals = array('i',[9,2,8,6,7])
print(vals)
for i in range(5):
   for j in range(i+1,5):
        if vals[i]>=vals[j]:
            vals[i],vals[j]=vals[j],vals[i]

print(vals)