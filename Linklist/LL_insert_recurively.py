#Debug the program

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

def insert(head,i,num):
    if i<0:
        return head
    if head is None:
        return None
    if i==0:
        newNode=Node(num)
        newNode.next=head
        return newNode
    small_head = insert(head.next,i-1,num)
    head.next=small_head
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
i=int(5)
num=int(65)
head=insert(head,i,num)
print_value(head)