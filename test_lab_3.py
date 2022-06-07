f=open("autori.in")
n,m=[int(x) for x in f.readline().split()]
#print(n,m)

d={}

for rand in range(n):
    ls=f.readline().split(maxsplit=1)
    #print (ls)
    cod_autor=int(ls[0])
    #print(cod_autor)
    d[cod_autor]=(ls[1].strip(),{})

#print(d)

for rand in range(m):
    ls=f.readline().split(maxsplit=4)
    #print(ls)
    cod_autor = int(ls[0])
    codul_cartii = int(ls[1])
    an_aparitie = int(ls[2])
    nr_pagini = int(ls[3])
    titlu = ls[4].rstrip('\n')
    # d_carti=d[cod_autor][1]
    # d_carti[codul_cartii]=[an_aparitie,nr_pagini,titlu]
    d[cod_autor][1][codul_cartii] = (an_aparitie, nr_pagini, titlu)

def sterge_carte(d,cod_carte):
    cod = int(cod_carte)
    for i in d:
        for c in d[i][1]:
            if c == cod:
                print("Cartea a fost scrisa de", d[i][0])
                del d[i][1][cod]
                return d[i][0]
    print("Cartea nu exista")

def cheie(x):
    return x[0],-x[1],x[2]

def carti_autori(d,cod_autor):
    cod = int(cod_autor)
    lista=[]
    for c in d:
        if c == cod:
            lista = list(d[cod][1].values())
            return d[cod][0], sorted(lista, key=cheie)
    return lista

a = input("cod sterge = ")
sterge_carte(d,a)
a = input("cod sterge = ")
sterge_carte(d,a)

a = input("cod autor = ")
list = carti_autori(d,a)
if(list != []):
    aut = list[0]
    books = list[1]
    print(aut)
    for i in books:
        print (i[2],i[0],i[1])
else:
    print("cod incorect")

a = input("cod autor = ")
list = carti_autori(d,a)
if(list != []):
    aut = list[0]
    books = list[1]
    print(aut)
    for i in books:
        print (i[2],i[0],i[1])
else:
    print("cod incorect")

