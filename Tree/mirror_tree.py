class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


def tree():
    data=int(input("Enter the node"))
    if data==-1:
        return
    root=Node(data)
    print("left")
    left=tree()
    print("right")
    right=tree()
    root.left=left
    root.right=right
    return root

def print_tree(root):
    if root==None:
        return
    print(root.data,end=",")
    print_tree(root.left)
    print_tree(root.right)

def mirror(root):
    if root==None:
        return
    left=mirror(root.right)
    right=mirror(root.left)
    root.left=left
    root.right=right
    return root



root=tree()
print_tree(root)
root=mirror(root)
print_tree(root)