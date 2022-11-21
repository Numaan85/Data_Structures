class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printll(head):
    while head is not None:
        print(str(head.data) +"->",end="")
        head=head.next
    print("None")


def Taking_input():
    inputList=[int(ele) for ele in input().split()]
    head=None
    for currdata in inputList:
        #if currdata ==-1:
            #break
        newNode=node(currdata)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head

head=Taking_input()
printll(head)