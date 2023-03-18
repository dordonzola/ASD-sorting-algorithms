def bubblesort(T):
    for i in range(len(T)):
        for j in range(1,len(T)):
            if T[j]<T[j-1]:
                T[j],T[j-1]=T[j-1],T[j]
    return T

T=[7,4,1,8,3,6,2,0]
print(bubblesort(T))