def insertionsort(T):
    for i in range(1,len(T)):
        tmp=T[i]
        index=i
        for j in range(i-1,-1,-1):
            if T[j]>tmp:
                T[j],T[index]=T[index],T[j]
                index=j

    return T

T=[8,3,6,2,9,5,4,1,2,7]
print(insertionsort(T))