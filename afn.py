import sys
def bt(k,tata):
    for i in range(nrtranzitii):
        if tranzitii[i][2]==cuvant[k] and tata==tranzitii[i][0]:
            if k==len(cuvant)-1:
                if tranzitii[i][1] in starifinale:
                    print("acceptat")
                    sys.exit(0)
            else:
                bt((k+1), (tranzitii[i][1]))
    print( "respins")
    sys.exit(0)




f=open("informatii.txt")
nodstart=int(f.readline())
nrstarifinale=int(f.readline())
starifinale=f.readline().split()
i=0
for x in starifinale:
    y=int(x)
    starifinale[i]=y
    i+=1

nrtranzitii=int(f.readline())
nrnoduri=int(f.readline())
tranzitii=[]
for line in f:
    a=line.split()
    tranzitii.append([int(a[0]),int(a[1]),(a[2])])
print(tranzitii)
cuvant=input()
stiva=[]
vizitat=[]
stiva.append(0)
vizitat.append(0)
litera=cuvant[0]
bt(0,0)

'''
for litera in cuvant:
    for tranzitie in tranzitii:
        if tranzitie[0]==nodstart and litera in tranzitie[2]:
            nodstart=tranzitie[1]
            break
if nodstart in starifinale:
    print("acceptat")
else:
    print("respins")'''