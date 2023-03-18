def selectionsort(T):
    for i in range(len(T)):
        mini=T[i]
        index=i
        for j in range(i+1,len(T)):
            if T[j]<mini:
                mini=T[j]
                index=j
        T[i],T[index]=T[index],T[i]

    return T

T=[5,7,2,9,3,8,1,5]
print(selectionsort(T))