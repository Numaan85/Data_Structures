class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def delete_node(head,position):
    if position<0 or position>int(print_len(head)):
        return head
    else:
        count=0
        prev=None
        current=head
        next=None
        while count<position:
            prev=current
            current=current.next
            next=current.next
            count+=1
        #Error in deleting first node
        if prev is None:
            prev=head
            head=head.next
            prev.next=None
        elif next is None:
            prev.next=None
        else:
            prev.next=next
    return head



def print_len(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    print(count)
    return count

def insert(head,i,num):
    if i<0 or i>int(print_len(head)):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count+=1
    newNode=Node(num)
    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    newNode.next=curr


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
# i=int(0)
# num=int(65)
# head=insert(head,i,num)
position=int(0)
head=delete_node(head,position)
print_len(head)
print_value(head)