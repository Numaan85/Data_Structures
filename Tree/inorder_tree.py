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

def printTree(root):
    if root==None:
        return
    printTree(root.left)
    print(root.data)
    printTree(root.right)
root=Tree()
printTree(root)