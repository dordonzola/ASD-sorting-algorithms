#radixsort na liczbach, różny rozmiar
def insertionsort(T, k):
    for i in range(1, len(T)):
        tmp1 = (T[i] // k) % 10
        index = i
        for j in range(i - 1, -1, -1):
            if (T[j] // k) % 10 > tmp1:
                T[index], T[j] = T[j], T[index]
                index = j
    return T


def radixsort(T):
    maxi = max(T)

    k = 1
    while maxi / k > 0:
        insertionsort(T, k)
        k *= 10
    return T


T = [472, 926, 156, 859, 826, 274]
print(radixsort(T))



