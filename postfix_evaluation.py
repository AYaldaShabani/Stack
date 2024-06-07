from my_stack import Stack
def evaluate_postfix(expreesion):
    stack = Stack()
    #removing withe spaces
    exp = ''
    for i in expreesion:
        if(not i.isspace()):
            exp += i 
    
    for i in exp:
        if i.isdigit():
            stack.push(i)
        else:
            value1 = stack.pop()
            value2 = stack.pop()
           

            stack.push(str(int(eval(value2 + i + value1))))

    return stack.pop()

print(evaluate_postfix("3 4 + 2 * 7 /")) # Output: 2