from my_stack import Stack
import string
def prefix_to_postfix(expretion):
    stack = Stack()

      #removing withe spaces
    exp = ''
    for i in expretion:
        if(not i.isspace()):
            exp += i 
    #pre to post algoritm : 
    
    # Read the Prefix expression in reverse order (from right to left)
    # If the symbol is an operand, then push it onto the Stack
    # If the symbol is an operator, then pop two operands from the Stack 
    # Create a string by concatenating the two operands and the operator after them. 
    # string = operand1 + operand2 + operator 
    # And push the resultant string back to Stack
    # Repeat the above steps until end of Prefix expression.

    reverse_exp = exp[::-1]
    for i in reverse_exp:
        if i  in ['+', '-' , '*' , '/' , '^']:
            value1 = stack.pop()
            value2 = stack.pop()
            result = value1 + value2 + i 
            stack.push(result)

        else:
            stack.push(i)

    output = ''
    output = output + stack.pop()
    
    return " ".join(output)
print(prefix_to_postfix("* + 3 4 2")) # Output: "3 4 + 2 *"

