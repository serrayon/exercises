import time

print('------------------ Answer #1 --------------')
# Given two integer numbers return their product only if the product is 
# equal to or lower than 1000, else return their sum.
number1 = 20
number2 = 30
def addMult(x,y):
    if x * y <= 1000:
        return x  * y
    else:
        return x + y 
print(addMult(number1,number2))

print('------------------ Answer #2 --------------')
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i

print('------------------ Answer #3 --------------')
#Exercise 3: Print characters from a string that are present at an even index number
'''Orginal String is  pynative
Printing only even index chars
p
n
t
v'''
# accept input string from a user
try:
    word = input('Enter word ')
    print("Original String:", word)

# get the length of a string
    size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
    print("Printing only even index chars")
    for i in range(0, size - 1, 2):
        print("index[", i, "]", word[i])
    
except EOFError as e:
    print(e)
print('------------------ Second Answer for #3 --------------')
# accept input string from a user
try:
    
    word = input('Enter word ')
    print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
    x = list(word)
    for i in x[0::2]:
        print(i)
except EOFError as e:
    print(e)

print('------------------ Answer #4 --------------')
#Exercise 4: Remove first n characters from a string
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

print('------------------ Answer #5 --------------')
#Exercise 5: Check if the first and last number of a list is the same
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

print('------------------ Answer #6 --------------')
#Exercise 6: Display numbers divisible by 5 from a list
num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)

print('------------------ Answer #7 --------------')
#Exercise 7: Return the count of a given substring from a string
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i+8: i + 12].lower() == 'good'
    print("Emma appeared ", count, "times")
test = "Emma is good developer. Emma good a goodgoodgOod"
count_emma(test)
print('------------------ Second Answer for #7 --------------')
str_x = "Emma is good developer. Emma is a writer"
# use count method of a str class
cnt = str_x.count("Emma")
print(cnt)

print('------------------ Answer #8 --------------')
#Exercise 8: Print the following pattern, similar to the Mario problem from CS-50
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''
for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")


print('------------------ Answer #9 --------------')
#Exercise 9: Check Palindrome Number
'''
original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number'''
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)

print('------------------ Second Answer for #10 --------------')
#Exercise 10: Create a new list from a two list using the following condition
# create new list from list1 and list2  
#answer should be [25, 35, 40, 60, 90]

st = time.process_time()
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new = [x for x in list1 if x%2!=0]
newnew = [x for x in list2 if x%2==0]
new.extend(newnew)
print(new)
et = time.process_time()
res = et - st /60
print(f'CPU time : {res} seconds')

print('------------------ Second Answer for #10 --------------')
# solution below is the solution provided by PYnative 
def merge_list(list1, list2):
    result_list = []
    
    # iterate first list
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list
print(merge_list(list1,list2))
et = time.process_time()
res = et - st / 60 
print(f'CPU time for second: {res} seconds')

print('------------------ Answer #11 --------------')
# 

    

