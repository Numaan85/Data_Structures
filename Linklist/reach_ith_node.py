class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_ll(head,target):
    count=1
    while head is not None:
        if head.data == target:
            print(count)
            break
        else:
            head=head.next
            count+=1
    if head is None:
        print("Element Not Found")



def Take_input():
    input_list = [int(ele) for ele in input("Enter Element in LinkList").split()]
    head=None
    for curr in input_list:
        newNode=Node(curr)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head

head=Take_input()

target=int(input("Enter the number to be search in LinkList"))

print_ll(head,target)