class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.right=None
        self.left=None
    
def tree():
    data=int(input())
    if data==-1:
        return
    root=Node(data)
    left=tree()
    right=tree()
    root.left=left
    root.right=right
    return root

def node_is_present(root,value):
    if root ==None:
        return
    if root.data==value:
        return True
    left=node_is_present(root.left,value)
    right=node_is_present(root.right,value)
    if left is True  or right is True:
        return True
    else:
        return False

root=tree()
print(node_is_present(root,7))