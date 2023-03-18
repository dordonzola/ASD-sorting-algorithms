def selectionsort(T,k):
    for i in range(len(T)):
        mini=(T[i]//k)%10
        index=i
        for j in range(i,len(T)):
            if (T[j]//k)%10<mini:
                mini=(T[j]//k)%10
                index=j
        T[i],T[index]=T[index],T[i]

    return T


def radixsort(T):
    maxi=max(T)

    k=1
    while maxi/k>0:
        selectionsort(T,k)
        k*=10


T=[72,34,75,94,91,696,32,89,13,]
radixsort(T)
print(T)