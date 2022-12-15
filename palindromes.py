# 5 ways to solve a string palindrome and 2 for integers 

# 1 indexing 
def palindrome(string):
    string = string.lower().replace(' ','')
    return string==string[::-1]
    
test = 'Madam Im Adam' 
test2 = 'Was it a car or a cat I saw'

print(palindrome(test))

#2 reversed method 
def palin(string):
    string = string.lower().replace(' ','')
    reverseS = ''.join(reversed(string))
    return string == reverseS
    
print(palin(test2))

#3 for loop
def palindromeFor(string):
    string = string.lower().replace(' ','')
    reverseString = ''
    for i in range(len(string),0,-1):
        reverseString += string[i-1]
    return string == reverseString
    
test = 'Madam Im Adam' 
test2 = 'Was it a car or a cat I saw'

print(palindromeFor(test))

#4 while loop
def palindromeWhile(string):
    string = string.lower().replace(' ','')
    first = 0 
    last = len(string)-1
    
    while  first < last:
        if string[first] ==  string[last]:
            first += 1 
            last -= 1 
        else:
            return False 
    return True
print(palindromeWhile(test2))

# 5 recursion 
def palinRecur(string):
    string = string.lower().replace(' ','')
    if len(string) < 1:
        return True 
    else:
        if string[0]==string[-1]:
            return palinRecur(string[1:-1])
        else:
            return False
            
            
test = input(F'Choose a phrase: ')
print(palinRecur(test))

#(--------------------integer-------------------------)

# easiest way is to typecast and index
def palinNum(number):
    number = str(number)
    return number== number[::-1]
    
test = 1212
print(palinNum(test))

# solution 2 
def palindromeNumber(number):
    original = number
    reverseNum = 0
    while number>0:
        remainder = number%10
        reverseNum = (reverseNum*10)+remainder
        number = number//10
        
    if original == reverseNum:
        print(f'{original} is a palindrome')
    else:
        print(f'{original} is not a palindrome')
        
test2 = 121
palindromeNumber(test2)
            
