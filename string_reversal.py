from my_stack import Stack
def reverse_string(input_string):
    stack = Stack()
    str = input_string
    for i in range(len(str)):
        stack.push(str[i])
    
    reverse = ''
    while not stack.isEmpty():
        reverse = reverse + stack.pop()
    
    return reverse


print(reverse_string("hello"))