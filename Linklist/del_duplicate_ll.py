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



def del_duplicate(head,val):
    if head is None:
        return
    l=len(head)
    curr=head
    next=curr.next
    while next is not None:
        if curr.data == val:
            curr.next=next.next
            next=next.next
        else:
            curr=curr.next
            next=next.next
    return head





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
val=6
head=del_duplicate(head,val)
print_value(head)