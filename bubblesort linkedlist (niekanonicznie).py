class Node():
    def __init__(self, val=None,next=None):
        self.val = val
        self.next = next

def tworz(T):
    last=None
    for i in range(len(T)-1, -1, -1):
        el=Node(T[i],last)
        last=el

    return last

def printAll(n):
    while n!=None:
        print(n.val, end=" ")
        n=n.next

def bubble_sort(n):
    sorted=False
    while not sorted:
        first=n
        sorted=True

        while n.next!=None:
            if n.val>n.next.val:
                x=n.val
                n.val=n.next.val
                n.next.val=x

                sorted =False

            n=n.next

    return first

T=[4,6,2,8,4,2,1,6,4,3]
printAll(bubble_sort(tworz(T)))