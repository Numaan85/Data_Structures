class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def delete(head,i):
    if head is None:
        return None
    next=head.next
    if i==0:
        pass
    small_head=delete(head.next,i-1)





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