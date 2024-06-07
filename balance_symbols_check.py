from my_stack import Stack
def is_balanced(expression):
    
    stack = Stack()
    for bracket in expression:
        if bracket in ["(" , "{" , "["]:
            stack.push(bracket)
        else :#which means its closing bracket
            if stack.isEmpty():
                return False
            if stack.peek() == "(":
                if bracket == ")":
                    stack.pop()
                else:
                    return False

            elif stack.peek() == "{":
                if bracket == "}":
                    stack.pop()
                else:
                    return False


            elif stack.peek() == "[":
                if bracket == "]":
                    stack.pop()
                else:
                    return False
                
    if stack.isEmpty():
        return True 
    else:
        return False


print(is_balanced("{[()]}")) # Output: True
print(is_balanced("({[)")) # Output: False
