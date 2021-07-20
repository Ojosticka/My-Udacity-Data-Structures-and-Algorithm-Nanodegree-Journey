
def Add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    #initialize the borrow 
    carry = 1
    #loop through the array from the end
    for i in range(len(arr), 0, -1):
        digit = carry + arr[i-1]
        
        carry = digit // 10
        if carry == 0:
            arr[i-1] = digit
            break
        else:
            arr[i-1] = digit%10
    
    #prepend carry to array
    arr = [carry] + arr
    
    pos = 0
    while arr[pos] == 0:
        pos += 1
        
    return arr[pos:]

    pass