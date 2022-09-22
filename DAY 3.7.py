def comb(L):      
    for i in range(len(L)):
        for j in range(len(L)):
            for k in range(len(L)):
                if (i!=j and j!=k and i!=k):
                    print("[",L[i],",",L[j],",",L[k],"]")
list=[]
r=int(input("Enter the Range : "))
for i in range(r):
    i=int(input("Enter the nums : "))
    list.append(i)
comb(list)
