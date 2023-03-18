class Node():
    def _init_(self,val):
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

def bubblesort(head):
    guard = Node()
    guard.next = head
    sorted = False
    while not sorted:
        prev=guard
        first = guard.next

        sorted = True
        while first.next != None:
            if first.val > first.next.val:
                prev.next=first.next
                first.next=first.next.next
                prev.next.next=first

                prev=prev.next
                #first=first
                sorted = False
            else:
                prev = prev.next
                first = first.next

    return guard.next


T=[2,1,6,9,0,5,8]

head=makelist(T)
print_all(head)
print('\n')
head=bubblesort(head)
print_all(head)