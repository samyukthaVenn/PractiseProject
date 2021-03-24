#These are practise python programs
#1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.

print("Hello world")
myList = [1,-2,-2,'x','x',2,2,4,6,5,3,4,4]
for x in range(len(myList)):
    print(myList, 'debug')
    if((myList.count(x))>1):
        print(x,'is duplicate')

