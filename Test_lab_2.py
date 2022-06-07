def modifica_prefix(x,y,prop):
    k=0
    ls=[]
    for cuvant in prop.split():
        if cuvant[:len(x)]==x:
            cuvant=cuvant.lstrip(x)
            cuvant=y+cuvant
            k+=1
        ls.append(cuvant)
    return ' '.join(ls),k

def poz_max(ls):
    max=-1
    pozitii=[]
    for i in range(len(ls)):
        if ls[i] > max:
            max=ls[i]
            pozitii=[]
            pozitii.append(i+1)
        else:
            if ls[i] == max:
                pozitii.append(i+1)
    return pozitii

f=open("propozitii.in")
a=input("a=")
b=input("b=")
ls=[]
g=open("propozitii_modificate.out","w")
for prop in f:
    prop_prefix,k=modifica_prefix(a,b,prop)
    g.write(prop_prefix)
    g.write('\n')
    ls.append(k)
print(poz_max(ls))
f.close()
g.close()
list=[]