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

def height(root):
    if root is None:
        return 0
    left=height(root.left)
    right=height(root.right)
    return 1+ (max(left,right))

def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)
root=Tree()
#printTree(root)
print(height(root))