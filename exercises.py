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
#Exercise 11: Write a Program to extract each digit 
#from an integer in the reverse order
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")

print('------------------ Answer #12 --------------')
#Exercise 12: Calculate income tax for the given 
#income by adhering to the below rules
''' Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.'''
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 25000) * 20 / 100

print("Total tax to pay is", tax_payable)

print('------------------ Answer #13 --------------')
#Exercise 13: Print multiplication table form 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")

print('------------------ Answer #14 --------------')
#Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
'''
* * * * *  
* * * *  
* * *  
* *  
*'''
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

print('------------------ Answer #15 --------------')
#Exercise 15: Write a function called exponent(base, exp) that returns an int 
#value of base raises to the power of exp.
'''
case 1
base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

case 2 
base = 5
exponent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)'''

def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)

print('------------------ Answer #16 --------------')
# return list combining both list no duplicates lambda 
def join_list_no_duplicates(list_a,list_b):
   return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
#write lambda below 
join_list_no_duplicates1 = lambda list_a,list_b:list(set(list_a + list_b))
print(join_list_no_duplicates1(list_a,list_b))

print('------------------ Answer #17 --------------')
#Complete the function so it returns a function
def create_quad_func(a,b,c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c
f = create_quad_func(2,4,6)
g = create_quad_func(1,2,3)
print(f(2))
print(g(2))


print('------------------ Answer #18 --------------')
#lexicographacly 
print('Lambdas Exercise')


signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort
#write sorting by integer
print(sorted(signups,key = lambda id:int(id[3:]))) # Integer sort

print('------------------ Answer #19 --------------')
#sort by score reverse will now print highest to lowest
print('Lambdas Exercise')

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]


#Exercise: Sort this by score using lambda!
player_list.sort(key = lambda playyer: playyer.score, reverse = True)
print([player.name for player in player_list])

print('------------------ Answer #20 --------------')

numbers = [1,2,3,4,5,6,7,8,9]
# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)
print(new_list)

new_list = [num*num for num in numbers]
print(new_list)
# give me a list with num for each num in numbers if num is even 
new_list = [num for num in numbers if num % 2 == 0]
print(new_list)
#lambda version filter returns a filter object must be type cast > list
new_list = filter(lambda num: num % 2 ==0,numbers)
print(list(new_list))

print('------------------ Answer #21 --------------')

# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))
print(new_list)
#return a tuple then loop above examples worked with list, sets, tuples
new_list = [(letter,num) for letter in'spam' for num in range(4)]
print(new_list)

print('------------------ Answer #22 --------------')