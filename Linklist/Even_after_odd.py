class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printll(head):
    while head is not None:
        print(str(head.data) +"->",end="")
        head=head.next
    print("None")

def Even_after_odd(head):
    if head is None:
        return None
    odd_head=None
    even_head=None
    while head is not None:
        if (head.data)%2==1:
            if odd_head is None:
                odd_head=head
                odd_tail=head
            odd_tail.next=head
            head=head.next
            odd_tail=odd_tail.next
        else:
            if even_head is None:
                even_head = head
                even_tail=head
            even_tail.next=head
            head=head.next
            eventail=eventail.next
    odd_tail.next=even_head
    return odd_head



def Taking_input():
    inputList=[int(ele) for ele in input("Enter Number").split()]
    head=None
    for currdata in inputList:
        #if currdata ==-1:
            #break
        newNode=node(currdata)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head

head=Taking_input()
head=Even_after_odd(head)
printll(head)