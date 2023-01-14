import queue
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def MinBST(root):
    if root==None:
        return -1000
    minleft=MinBST(root.left)
    minright=MinBST(root.right)
    return min(minleft,minright,root.data)

def MaxBST(root):
    if root==None:
        return 1000
    leftMax=MaxBST(root.left)
    rightMax=MaxBST(root.right)
    return max(leftMax,rightMax,root.data)

def checkBST(root):
    leftMax=MaxBST(root.left)
    rightMin=MinBST(root.right)
    if root.data>rightMin or root.data<=leftMax:
        return False
    left=checkBST(root.left)
    right=checkBST(root.right)
    return left and right

def checkBST2(root):
    if root ==None:
        return 1000, -1000, True
    leftMax,leftMin,isleftBST=checkBST2(root.left)
    rightMax,rightMin,isrightBST=checkBST2(root.right)
    minimum=min(leftMin,rightMin,root.data)
    print(minimum)
    maximum=max(leftMax,rightMax,root.data)
    print(maximum)
    isBST=True
    if root.data< leftMax or root.data > rightMin:
        isBST=False
    if not(isleftBST) or not(isrightBST):
        isBST=False
    return maximum,minimum,isBST


def tree():
    q=queue.Queue()
    rootdata=int(input("Enter root of Tree"))
    if rootdata==-1:
        return
    root=Node(rootdata)
    q.put(root)
    while (not(q.empty())):
        current=q.get()
        print("Enter left node of:",current.data)
        left_data=int(input())
        if left_data!=-1:
            left=Node(left_data)
            current.left=left
            q.put(left)
        print("Enter the right node of:",current.data)
        right_data=int(input())
        if right_data!=-1:
            right=Node(right_data)
            current.right=right
            q.put(right)
    return root

root=tree()
print(checkBST2(root))