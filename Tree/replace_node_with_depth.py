class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def tree():
    data=int(input("Enter the nodes"))
    if data==-1:
        return 
    root=Node(data)
    print("left Node")
    left=tree()
    print("Right Node data")
    right=tree()
    root.left=left
    root.right=right
    return root

def printTree(root):
    if root == None:
        return
    print(root.data,end=",")
    printTree(root.left)
    printTree(root.right)

def depthV2(root,k=0,d=0):
    if root is None:
        return
    if d==k:
        root.data=k
    depthV2(root.left,k+1,d+1)
    depthV2(root.right,k+1,d+1)
    return root

root=tree()
printTree(root)
root=depthV2(root)
printTree(root)