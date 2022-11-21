class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

def len (head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count


def append_lst_frst(head,n):
    count=0
    curr=head
    l=len(head)
    while count<l - n:
        curr=curr.next
        count=count+1
    h2=curr.next
    curr.next=None
    tail=h2
    l=len(h2)
    count=0
    while count<l-1:
        tail=tail.next
        count+=1
    tail.next=head
    return h2

def print_value(head):
    count=0
    while head is not None:
        print(str(head.data) + "->",end="")
        head=head.next
    print("None")

def Taking_value():
    input_list = [int(ele) for ele in input("Enter list").split()]
    head=None
    for curr in input_list:
        newNode = Node(curr)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head

head=Taking_value()
print(len(head))
n=int(5)
head=append_lst_frst(head,n)
print_value(head)
