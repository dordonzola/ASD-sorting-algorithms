def add_blanks(T):
    n = len(T)
    maxi = 0
    for i in range(n):
        maxi = max(maxi, len(T[i]))
    for i in range(n):
        diff = maxi - len(T[i])
        for j in range(diff):
            T[i] += ' '

    return maxi

def remove_blanks(T):
    for i in range(len(T)):
        x = ''
        for j in T[i]:
            if j != ' ':
                x += j
        T[i] = x


def insertion_sort(T, x):
    n = len(T)
    for i in range(1, n):
        key = T[i]
        index=i
        for j in range(i-1,-1,-1):
            if T[j][x]>key[x]:
                T[j],T[index]=T[index],T[j]
                index=j

    return T

def radix_letters(T):
    maxi = add_blanks(T)
    #maxi=len(T[0])
    for i in range(maxi - 1, -1, -1):
        insertion_sort(T, i)
    remove_blanks(T)

    return T

#T=['kot','aka','ala','lot','tfu','ojj']
T = ['ola', 'bts', 'xd', 'ala', 'am', 'ela', 'ula', 'abrakadabra']

print(radix_letters(T))
