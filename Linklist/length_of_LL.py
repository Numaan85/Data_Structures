class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_len(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    print(count)
    return count



def taking_input():
    input_list=[int(ele) for ele in input().split()]
    head=None
    for curr in input_list:
        newNode = Node(curr)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next= newNode
            tail=newNode
    return head

head =taking_input()
size=print_len(head)
print(type(size))