import queue
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def between(root,k1,k2):
    if root==None:
        return
    if root.data>k2:
        between(root.left,k1,k2)
    elif root.data<k1:
        between(root.right,k1,k2)
    else:
        print(root.data)
        between(root.left,k1,k2)
        between(root.right,k1,k2)


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
between(root,10,40)