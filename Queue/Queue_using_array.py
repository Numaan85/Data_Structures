class Queue:
    def __init__(self) -> None:
        self.__arr=[]
        self.__count=0
        self.__front=0

    def enque(self,data):
        self.__arr.append(data)
        self.__count+=1
    
    def dequeue(self):
        if self.__count==0:
            return -1
        element = self.__arr[self.__front]
        self.__front+=1
        self.__count-=1
        return element

    def front(self):
        if self.__count==0:
            return -1
        else:
            return self.__arr[self.__front]
    
    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.size==0

q=Queue()
n=int(10)
q.enque(n)
print(q.dequeue())