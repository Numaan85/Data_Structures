class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None
    
def tree():
    data=int(input("Enter a node"))
    if data ==-1:
        return
    root=Node(data)
    print("Enter left Node")
    left_input=tree()
    print("Enter right node")
    right_input=tree()
    root.left=left_input
    root.right=right_input
    return root

def printTRee(root):
    if root is None:
        return
    print(root.data,end=",")
    printTRee(root.left)
    printTRee(root.right)


def node_at_depth_k(root,k):
    if root ==None:
        return
    if k==0:
        print(root.data)
        return
    node_at_depth_k(root.left,k-1)
    node_at_depth_k(root.right,k-1)

def depthV2(root,k,d=0):
    if root is None:
        return
    if d==k:
        print(root.data,end=" ")
        return
    depthV2(root.left,k,d+1)
    depthV2(root.right,k,d+1)
    



root=tree()
node_at_depth_k(root,2)
depthV2(root,2)