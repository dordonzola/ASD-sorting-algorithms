from random import randint, seed
from time import time


class Node:
    def __init__(self):
        self.next = None
        self.value = None



def partition(A, end):
    s = A
    pivot = A
    pivot_copies = Node()

    while A.next != end:
        if pivot.value > A.next.value:
            temp = A.next
            A.next = A.next.next
            temp.next = s
            s = temp
        elif pivot.value == A.next.value:
            temp = A.next
            A.next = A.next.next
            temp.next = pivot_copies.next
            pivot_copies.next = temp
        else:
            A = A.next

    pivot_copies = pivot_copies.next
    if pivot_copies != None:
        temp = pivot.next
        pivot.next = pivot_copies
        while pivot_copies.next != None: pivot_copies = pivot_copies.next
        pivot_copies.next = temp
        return (s, pivot, pivot_copies)

    return (s, pivot, pivot)


def quicksort(A, end):
    if A != end:
        A, p_start, p_end = partition(A, end)
        A = quicksort(A, p_start)
        p_end.next = quicksort(p_end.next, end)

    return A


# ||||||||||||||||||
# Koniec rozwiązania
# ||||||||||||||||||

def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next


def printlist(L):
    while L != None:
        print(L.value, "->", end=" ")
        L = L.next
    print("|")


seed(42)

n = 10
T = [randint(1, 100) for i in range(1000000)]
L = tab2list(T)

start = time()
L = quicksort(L, None)
print(time() - start)

if L == None:
    print("List jest pusta, a nie powinna!")
    exit(0)

P = L
while P.next != None:
    if P.value > P.next.value:
        print("Błąd sortowania")
        exit(0)
    P = P.next

print("OK")
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Alogrytm bierze jako pivot pierwszy element z przekazanej listy, mniejsze od niego elementy przepina na poczatek listy,
# natomiast równe pivotowi do osobnej listy z wartownikiem (pivot_copies), którą w razie potrzeby (jeśli pivot się powtórzył)
# łączy z pozostałymi elementami. Partition zwraca wskazanie na poczatek listy, a takze na pierwszy i ostatni element o wartosci pivota
#
# Funkcje quicksort oraz partition przyjmuja dwa argumenty, wskazania na poczatek i koniec zakresu listy odsylaczowej, który ma zostać posortowany
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
