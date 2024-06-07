class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1
    
    def push(self , item):
        self.top += 1
        self.stack.append(item)
        
        
        
    def pop(self):
        if  self.isEmpty():
            return None
        else:
            item =  self.stack.pop(self.top)
            self.top = self.top -1 
            return item
    def peek(self):
        if self.isEmpty(): 
            return None
        else:
            item =  self.stack[self.top]
            return item
    def isEmpty(self):
        # if self.top >= 0:
        #     return False
        # else:
        #     return True
        if self.top == -1:
            return True
        else :
            return False    
    def size(self):
        return self.top + 1 
    
    def get_max(self):

        if self.isEmpty():
            return None

        else: 
            max = self.stack[self.top]
            for i in range(self.top +1):
                if self.stack[i] > max :
                    max = self.stack[i]
            return max
           
       



    

#example:

# stack = Stack()
# stack.push(100)
# stack.push(10)
# stack.push(20)
# print(stack.get_max()) # output: 100
# print(stack.peek()) # Output: 20
# print(stack.pop()) # Output: 20
# print(stack.isEmpty()) # Output: False