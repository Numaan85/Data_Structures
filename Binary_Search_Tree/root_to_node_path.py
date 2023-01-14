import queue
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def root_to_node(root,target):
    if root==None:
        return None
    if root.data==target:
        l=[]
        l.append(root.data)
        return l
    leftOut=root_to_node(root.left,target)
    
    if leftOut!=None:
        leftOut.append(root.data)
        return leftOut

    rightOut=root_to_node(root.right,target)
    if rightOut!=None:
        rightOut.append(root.data)
        return rightOut
    else:
        return None

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
print(root_to_node(root,5))