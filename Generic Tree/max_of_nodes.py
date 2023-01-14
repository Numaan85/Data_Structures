class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.children=list()

def printTree2(root):
    if root==None:
        return
    print(root.data, end=":")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree2(child)

def max_of_nodes(root):
    if root==None:
        return
    for child in root.children:
        return max(max_of_nodes(child))

def takingInput():
    rootData=int(input("Enter the root data"))
    if rootData== -1:
        return None
    root=Node(rootData)
    print("Enter number of child for",root.data)
    no_of_nodes=int(input())
    for i in range(no_of_nodes):
        child=takingInput()
        root.children.append(child)
    return root


root=takingInput()
printTree2(root)
print(max_of_nodes(root))