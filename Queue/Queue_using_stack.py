class Queue:
    def __init__(self) -> None:
        self.__arr1=[]
        self.__arr2=[]

    def enque(self,data):
        while (len(self.__arr1)!=0):
            self.__arr2.append(self.__arr1.pop())
        self.__arr1.append(data)
        while (len(self.__arr2)!=0):
            self.__arr1.append(self.__arr2.pop())


    def deque(self):
        if (len(self.__arr1)==0):
            return -1
        return self.__arr1.pop()
    
    def front(self):
        return self.__arr1[-1]
    
    def size(self):
        return len(self.__arr1)
    
    def isEmpty(self):
        return self.size() ==0

q=Queue()
q.enque(17)
q.enque(29)
q.enque(37)
print(q.front())
print(q.size)