class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

def printAll(n):
    while n!=None:
        print(n.value, end=" ")
        n=n.next

def tworz(T):
    last=None
    for i in range(len(T)-1, -1, -1):
        el=Node(T[i],last)
        last=el

    return last


def selectionsort(first):
    tmp = first

    while tmp is not None:

        n = tmp.next
        mini = tmp

        while n is not None:
            if  n.value < mini.value:
                mini = n

            n = n.next

        x = tmp.value
        tmp.value = mini.value
        mini.value = x
        tmp = tmp.next

T=[7,5,9,1,3,2,5]
n=tworz(T)
selectionsort(n)
printAll(n)


