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


# check how many times a word appears in a str
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i+8: i + 12].lower() == 'good'
    print("Emma appeared ", count, "times")
test = "Emma is good developer. Emma good a goodgoodgOod"
count_emma(test)

# take the mu, 
#answer should be [25, 35, 40, 60, 90]
import time
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