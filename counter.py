'''
Problem Statement: Little Robert likes mathematics. Today his teacher has given him two integers and asked him to find out how many integers can divide both the numbers. Would you like to help him in completing his school assignment?
'''
import collections
num1 = int(input("Enter two numbers : "))
num2 = int(input())
counter_num1 = 0
counter_num2 = 0
num1_list =[]
num2_list=[]
for i in range(1,num1):
    if num1 % i ==0:
        counter_num1 = counter_num1 + 1
        #Used for testing ----print(i)
        num1_list.append(i)
for j in range(1,num2):
    if num2 % j == 0:
        counter_num2 = counter_num2 + 1
        #Used for testing -----print(j)
        num2_list.append(j)
if counter_num1 > 0:
    print(f"{num1} can be divided by having a count of :"+str(counter_num1))
if counter_num2 > 0:
    print(f"{num2} can be divided by having a count of "+str(counter_num2))
#Used to take intersection of two list
result = collections.Counter(num1_list) & collections.Counter(num2_list)
intersected_list = list(result.elements())
list_length = len(intersected_list)
print()
print("Number of possible divisions are "+ str(list_length))
print()
