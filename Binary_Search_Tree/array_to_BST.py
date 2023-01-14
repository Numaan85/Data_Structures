class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

def sorted_Array_to_BST(arr):
    if not arr:
        return None
    mid=len(arr)//2
    root=Node(arr[mid])
    root.left=sorted_Array_to_BST(arr[:mid])
    root.right=sorted_Array_to_BST(arr[mid+1:])
    return root

def printTree(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left !=None:
        print(root.left.data,end=",")
    if root.right !=None:
        print(root.right.data,end=",")
    print("")
    printTree(root.left)
    printTree(root.right)

arr=[1,2,3,4,5,6,7]
root=sorted_Array_to_BST(arr)
printTree(root)