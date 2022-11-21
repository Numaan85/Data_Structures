class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_len(head):
    count=0
    while head is not None:
        print(str(head.data) + "->",end="")
        head=head.next
    print("None")



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
print_len(head)