class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None


def print_revrse(head):
    if head is None or head.next is None:
        return head
    small_head=print_revrse(head.next)
    tail = head.next
    tail.next=head
    head.next=None
    return small_head


def print_len(head):
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
head=print_revrse(head)
print_len(head)