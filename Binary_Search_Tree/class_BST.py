class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self) -> None:
        self.root=None
        self.node=0
    
    def helperSearch(self,root,data):
        if root==None:
            return None
        if root==data:
            return True
        if root.data>data:
            return self.helperSearch(root.left,data)
        else:
            return self.helperSearch(root.right,data)

    def search(self,data):
        return self.helperSearch(self.root,data)

    def isprint(self,root):
        if root==None:
            return
        print(root.data,end=":")
        if root.left !=None:
            print(root.left.data,end=",")
        if root.right !=None:
            print(root.right.data,end=",")
        print("")
        self.isprint(root.left)
        self.isprint(root.right)
        
        
    def printtree(self):
        self.isprint(self.root)

    def helperInsert(self,root,data):
        if root==None:
            root=Node(data)
            return root
        if root.data> data:
            root.left= self.helperInsert(root.left,data)
            return root
        else:
            root.right= self.helperInsert(root.right,data)
            return root
    
    def insert(self,data):
        self.node+=1
        self.root = self.helperInsert(self.root,data)
    
    def minimum(self,root):
        if root==None:
            return 1000
        if root.left==None:
            return root.data
        return self.minimum(root.left)

    def helperDelete(self,root,data):
        if root==None:
            return False,None
        
        if root.data< data:
            delete,newright=self.helperDelete(root.right,data)
            root.right=newright
            return delete,root
        if root.data> data:
            delete,newleft=self.helperDelete(root.left,data)
            root.left=newleft
            return delete,root
        if root.left==None and root.right==None:
            return True,None
        if root.left==None:
            return True,root.right
        if root.right==None:
            return True, root.left
        
        replacement=self.minimum(root.right)
        root.data=replacement
        delete,newright=self.helperDelete(root.right,replacement)
        root.right=newright
        return True,root


    def delete(self,data):
        delete,newroot= self.helperDelete(self.root,data)
        if delete:
            self.node-=1
        self.root=newroot
        return delete
    def count(self):
        return self.node


tree=BST()
tree.insert(10)
tree.insert(20)
tree.insert(6)
print(tree.count())
tree.printtree()
print(tree.delete(10))