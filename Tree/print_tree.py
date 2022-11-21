class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def printTree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left !=None:
        print(root.left.data,end=",")
    if root.right !=None:
        print(root.right.data,end=",")
    print("")
    printTree(root.left)
    print("recursion1")
    printTree(root.right)
    print(" recursion")

btn1=Node(2)
btn2=Node(3)
btn3=Node(5)
btn4=Node(7)
btn5=Node(8)
btn6=Node(1)
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
btn3.left=btn6
printTree(btn1)