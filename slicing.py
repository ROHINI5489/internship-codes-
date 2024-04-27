l={True:1,'two':2,1.1:3}
del(1)
for i in l.keys():
    if i==True:
        del l(i)
print(l)