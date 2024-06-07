from my_stack import Stack
def infix_to_postfix(expression):
    #removing white space :
    exp = ''
    for i in expression:
        if(not i.isspace()):
            exp += i 
    stack = Stack()
    result = ''
    for i in exp:
        if i.isdigit():
            result += i 
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while  not stack.isEmpty() and  not stack.peek() == "(":
                item = stack.pop()
                result += str(item)
            stack.pop() #pop "("
        else:
            while not stack.isEmpty() and piorityOP(stack.peek()) >= piorityOP(i):
               item = stack.pop()
               result += str(item)
            stack.push(i)

    while not stack.isEmpty():
        item = stack.pop()
        result += str(item)

    return " ".join(result)

 



def piorityOP(operator):
    if operator == "^":
        return 3
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "+" or operator == "-":
        return 1 
    else :
        return -1
    
print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )")) # Output: "3 4 2 * 1 5 - / +"