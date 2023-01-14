class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.children=list()

def printTree1(root):
    if root==None:
        return
    print(root.data)
    for child in root.children:
        printTree1(child)

def printTree2(root):
    if root==None:
        return
    print(root.data, end=":")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree2(child)


n1=Node(5)
n2=Node(6)
n3=Node(7)
n4=Node(8)
n5=Node(9)
n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n2.children.append(n5)
printTree1(n1)
printTree2(n1)