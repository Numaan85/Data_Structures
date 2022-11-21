class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    
def Tree():
    root_data =int(input("Enter tree Node"))
    if root_data ==-1:
        return None
    root = Node(root_data)
    print("left")
    leftTree=Tree()
    print("right")
    rightTree=Tree()
    root.left=leftTree
    root.right=rightTree
    return root

def no_of_nodes(root):
    if root is None:
        return 0
    left=no_of_nodes(root.left)
    right=no_of_nodes(root.right)
    return 1+left+right

def printTree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left !=None:
        print("L",root.left.data,end=",")
    if root.right !=None:
        print("R",root.right.data,end=",")
    print(" ")
    printTree(root.left)
    printTree(root.right)
root=Tree()
print(no_of_nodes(root))
printTree(root)