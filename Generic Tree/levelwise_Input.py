import queue

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.children=list()

def printTree2(root):
    if root==None:
        return
    print(root.data, end=":")
    for child in root.children:
        print(child.data,end=",")
    print()
    for child in root.children:
        printTree2(child)

def levelwise():
    q=queue.Queue()
    rootData=int(input("Enter the root"))
    if rootData==-1:
        return None
    root=Node(rootData)
    q.put(root)
    while not(q.empty()):
        current=q.get()
        print("Enter the no of child of: ",current.data)
        no_of_child=int(input())
        for i in range(no_of_child):
            print("Enter the child of ", current.data)
            childdata=int(input())
            child=Node(childdata)
            current.children.append(child)
            q.put(child)
    return root


root=levelwise()
printTree2(root)