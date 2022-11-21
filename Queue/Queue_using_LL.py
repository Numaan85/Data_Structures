class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
class Queue:
    def __init__(self) -> None:
        self.__head=None
        self.__tail=None
        self.__size=0
    
    def enqueue(self,data):
        if self.__size==0:
            self.__head=Node(data)
            self.__tail=self.__head
            self.__size+=1
        else:
            self.__tail.next=Node(data)
            self.__tail=self.__tail.next
            self.__size+=1
    
    def dequeue(self):
        if self.__size==0:
            return -1
        else:
            element=self.__head.data
            self.__head=self.__head.next
            self.__size-=1
            return element
    
    def isEmpty(self):
        return self.count()==0
    
    def count(self):
        return self.__size

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

