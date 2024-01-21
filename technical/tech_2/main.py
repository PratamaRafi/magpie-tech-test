def smallest5(n):
    # convert string to a list 
    digits = [int(digit) for digit in n]

    # loop every digit for get lowest value 
    min_value = float('inf')
    for i in range(len(digits)):
        if digits[i] == 5:
            temp = int(''.join(map(str, digits[:i] + digits[i+1:])))
            min_value = min(min_value, temp)

    return min_value

# test result removing 5
print(smallest5("12345"))  
print(smallest5("5005")) 
print(smallest5("5369"))  
print(smallest5("645231"))  
print(smallest5("5215")) 
print(smallest5("8651263505")) 
