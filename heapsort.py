def heapify (T,n,i):
    l=2*i+1
    r=2*i+2
    m=i
    if l<n and T[l]>T[m]: m=l
    if r<n and T[r]>T[m]: m=r
    if m!=i:
        T[i],T[m]=T[m],T[i]
        heapify(T,n,m)

def parent(i):
    return (i - 1) // 2

def buildheap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1): #zaczynamy od rodzica ostatniego dziecka(bo pozniejsze elementy nie beda malymi kopcami)
        heapify(T,n,i)

def heapsort(T):
    n=len(T)
    buildheap(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]#wstawiamy aktualny max element na koniec nieposortowanej czesci tablicy
        heapify(T,i,0)

def add(T,el):
    T.append(el)
    heapsort(T)
    return T


T=[7,4,5,2,3,1,8,4]
heapsort(T)
print(T)
#print(add(T,3))
