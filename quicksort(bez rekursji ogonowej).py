#Zużywa mniej pamięci, ale wolniejszy niż z rekursją

def partition(T,a,b):
    x=T[b]
    i=a-1
    for j in range(a,b):
        if T[j]<=x:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[b]=T[b],T[i+1]
    return i+1

def quicksort(T,a,b):
    while a<b:
        q=partition(T,a,b)
        quicksort(T,a,q-1)
        a=q+1
    return T

T=[5,8,1,9,3,6,4]
print(quicksort(T,0,len(T)-1))

