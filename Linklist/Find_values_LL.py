class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def Find_values(head,data):
    if head.data ==data:
        print(head.data)
        return head.data
    if head is None:
        return None
    Find_values(head.next,data)


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

head =Taking_value()
data=int(3)
Find_values(head,data)