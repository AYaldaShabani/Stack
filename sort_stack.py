from my_stack import Stack
class sort_stack(Stack):
   
    # algorithm
    # Create a temporary stack say tmpStack.
    # While input stack is NOT empty do this: 
    #     Pop an element from input stack call it temp
    #     while temporary stack is NOT empty and top of temporary stack is greater than temp, 
    #     pop from temporary stack and push it to the input stack
    #     push temp in temporary stack
    # The sorted numbers are in tmpStack
    def __init__(self , my_stack) -> None:
        super().__init__()
        self.tempstack = Stack()
        
        while not my_stack.isEmpty():
            
            temp = my_stack.pop()
            while not self.tempstack.isEmpty() and self.tempstack.peek() > temp:
                my_stack.push(self.tempstack.pop())
            self.tempstack.push(temp)
    
    def pop(self):
        return self.tempstack.pop()





stack = Stack()
stack.push(30)
stack.push(10)
stack.push(20)
sorted_stack = sort_stack(stack)
print(sorted_stack.pop()) # Output: 1
print(sorted_stack.pop()) # Output: 3