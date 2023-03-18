#words have the same length

def countingsort(A,x):
    C=[0]*24
    B=[0]*len(A)
    for i in range(len(A)):
        C[ord(A[i][x])-97]+=1
    for i in range(1, 24):
        C[i] += C[i - 1]
    for i in range(len(A)-1,-1,-1):
        C[ord(A[i][x])-97]-=1
        B[C[ord(A[i][x])-97]]=A[i]
    for i in range(len(A)):
        A[i]=B[i]

    return A

def radix_letters(T):
    maxi=len(T[0])
    for i in range(maxi - 1, -1, -1):
        countingsort(T, i)


    return T

T=['kot','aka','ala','lot','tfu','ojj']


print(radix_letters(T))
