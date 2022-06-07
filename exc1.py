def min_max(list):
    max = int(list[0])
    min = int(list[0])
    #print(min,max)
    for i in list:
        i = int(i)
       # print (i)
        if i > max:
            max = i
        if i < min:
            min = i
    return min,max


def incarca_fisier(fisier):
    f = open(fisier)
    m=[[x for x in linie.split()] for linie in f]
    return m

g = open("egale.txt","w")
#a = input("file name: ")
m = incarca_fisier("fisier1.in")
count = 0
linelist =[]
for ls in m:
    ok = 1
    for ls2 in ls:
        if ls[0] != ls2:
            ok = 0
    if(ok == 1):
        linelist.append(count)
    count+=1

minmaxlist = []
for ls in m:
    min, max = min_max(ls)
    minmaxlist.append(min)
    minmaxlist.append(max)

#print(minmaxlist)
a,b=min_max(minmaxlist)
print(a,b)
#print(a,b)


