class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def makelist(T):
    last=None
    for i in range(len(T)-1,-1,-1):
        first=Node()
        first.val=T[i]
        first.next=last
        last=first
    return first

def print_all(first):
    while first!=None:
        print(first.val,end = ' ')
        first = first.next


def insertion_sort(head):
    guard=Node()
    guard.next=head

    prev=guard
    first=guard.next
    while first is not None:
        key=first.val

        change=False
        prev_i=guard
        i=guard.next
        while i!=first:
            if i.val>key:
                #odpinamy firsta
                prev.next=first.next
                #przypinamy firsta w miejsce i
                prev_i.next=first
                first.next=i

                #ustawiamy flagę
                change=True
                break
            i=i.next
            prev_i=prev_i.next

        if change==True:
            first=prev.next
        else:
            first=first.next
            prev=prev.next


    return guard.next




T=[5,4,3,2,1]

head=makelist(T)
print_all(head)
print('\n')
head=insertion_sort(head)
print_all(head)