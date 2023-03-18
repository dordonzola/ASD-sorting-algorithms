

def merge(left, right, mid, tab):
    l1 = mid - left + 1
    l2 = right - mid
    
    L = []
    R = []
    
    for i in range(l1):
        L.append(tab[left + i])
    for i in range(l2):
        R.append(tab[mid + i + 1])
    
    i = 0
    j = 0
    k = left
    
    while i < l1 and j < l2 :
        if L[i] <= R[j]:
            tab[k] = L[i]
            i += 1
        else:
            tab[k] = R[j]
            j += 1
        k += 1
        
    while i < l1 :
        tab[k] = L[i]
        i += 1
        k += 1
    while j < l2 :
        tab[k] = R[j]
        j += 1
        k += 1
        
def mergesort(tab, l, r):
    if l < r:
        mid = (l + r) // 2
        mergesort(tab, l, mid)
        mergesort(tab, mid + 1, r)
        merge(l, r, mid, tab)
    
    
T = [12,1,6,3,8,9]
mergesort(T,0,5)
print(T)
    