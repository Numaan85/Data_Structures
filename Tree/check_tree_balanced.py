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

def isBalanced(root):
    if root ==None:
        return True
    
    l1=height(root.left)
    l2=height(root.right)
    if l1-l2>1 or l2-l1>1:
        return False
    left=isBalanced(root.left)
    right=isBalanced(root.right)
    if left and right:
        return True
    else:
        return False

def balanced2(root):
    if root ==None:
        return 0,True
    
    h1,left=balanced2(root.left)
    h2,right=balanced2(root.right)
    h=1+max(h1,h2)
    if h1-h2 >1 or h2-h1 > 1:
        return h,False
    if left and right:
        return h,True
    else:
        return h,False


def printTree(root):
    if root==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)
root=Tree()
print(isBalanced(root))
print(balanced2(root))