from my_stack import Stack
def daily_tempratures(temprature):
    tempratures = []
    for i in range(len(temprature)):
        tempratures.append(temprature[i])

    temprature_compare =Stack()
    how_many_days_left = []
    for i in range(len(tempratures)):
        
        temp = tempratures[i]
        temprature_compare.push(temp)
        temprature_compare.peek()
        j = i+1
        while j < len(tempratures) - i:
            
            if tempratures[j] > temprature_compare.peek():
                
                how_many_days_left.append(int(temprature_compare.size()))
                break
            else: 
                temprature_compare.peek()
                
                temprature_compare.push(tempratures[j])
                j += 1 
        while  not temprature_compare.isEmpty():
           
            temprature_compare.pop()
    result = '['
    for i in range(len(how_many_days_left)):
        
        result = result + str(how_many_days_left[i]) + ", "
    
    return result


print(daily_tempratures([73, 74, 75, 71, 69, 72, 76, 73]))
 # Output: [1, 1, 4, 2, 1, 1, 0, 0]
