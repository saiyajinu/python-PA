def citire_matrice(fisier):
    f=open(fisier)
    m=[[x for x in linie.split()] for linie in f]
    for i in range(len(m)-1):
        if len(m[i]) != len(m[i+1]):
            return None
    return m

def multimi(m ,*numere):
    reuniune= set()
    intersectie = None
    for x in numere:
        ls_poz= set([y for y in m[x] if int(y) >= 0 and int(str(y)[0]) == int(y)%10])
        ls_neg= set([y for y in m[x] if int(y) < 0])
        #print(ls_poz,ls_neg)
        if intersectie == None:
           intersectie = ls_neg
        else:
            intersectie = intersectie & ls_neg
        reuniune = reuniune | ls_poz
    return intersectie, reuniune


m=citire_matrice("fisier1.in")
i,r=multimi(m,len(m)-1,len(m)-2,len(m)-3)
def cheie(x):
    return int(x)
print(sorted(r,key = cheie))
i,r=multimi(m,0,len(m)-1)
print(len(i))
