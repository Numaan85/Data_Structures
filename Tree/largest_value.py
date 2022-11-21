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

def largest(root):
    if root ==None:
        return -1
    left=largest(root.left)
    right=largest(root.right)
    large=max(left,right,root.data)
    return large

def printTree(root):
    if root==None:
        return
    print(root.data,end=" ")
    printTree(root.left)
    printTree(root.right)
root=Tree()
printTree(root)
print(largest(root))