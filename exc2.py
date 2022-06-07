def deviruseaza(prop):
    final = ''
    prop = prop.split()
    for i in prop:
        start = i[0]
        end = i[-1]
        if(len(i)>1):
            string = end + str(i[1:-1]) + start
        else:
            string = i[0]
        final = string + ' '+ final
    return final

def prime(n, numar_maxim = 0):
    list = []
    for num in range(2, n):
        d = 2
        for d in range(2, num):
            if (num % d == 0):
                d = num
                break
        if (num == 2):
            list.append(2)
        if (d != num):
            list.append(num)
        #print(list, i)
    if numar_maxim == 0:
        return list
    else:
        return list[0:numar_maxim]


#prop = "aorectc aropozitip este aceasta"
#prop = deviruseaza(prop)
#list = prime(10)
#print(list)
g=open("intrare_devirusata.out","w")
f=open("intrare.in")
propozitii =[linie.rstrip('\n') for linie in f]
numere = prime(len(propozitii)+1)
for i in numere:
    propozitii[i-1] = deviruseaza(propozitii[i-1])
for i in propozitii:
    g.write(i)
    g.write('\n')

