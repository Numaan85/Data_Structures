class stack:
    def __init__(self):
        self.__data=[]
    
    def push(self,item):
        self.__data.append(item)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return 
        return self.__data.pop()
    
    def top(self):
        if self.isEmpty():
            print("stack is empty")
            return 
        
        return self.__data[len(self.__data)-1]
    
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size() == 0

s=stack()
s.push(10)
s.push(20)
s.push(30)
while (s.isEmpty()) is False:
    print(s.pop())