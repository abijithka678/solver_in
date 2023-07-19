'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
#val = ord('a')
#print(val)
max = int(input("Enter the maximum number of students : "))
details =[]
scorelist = []
max_list = []
#character =[]
#lit = []
for i in range(max):
    name = input("Enter the name of the student : ")
    score = input("Enter the score of the student :")
    details.append([name,score])
#print(details)
for rootlist in details:
   # for content in rootlist:
        scorelist.append(rootlist[1])
#print(scorelist)
max_score = sorted(scorelist)
#print("Maximum score among list :"+str(max_score))
length = len(max_score)
#print(length)
for rootlist in details:
    if rootlist[1] == max_score[length-1]:
        print("Maximum scored Student : "+str(rootlist[0]))
        max_list.append(rootlist[0])
max_list.sort()
for lines in max_list:
    print("Name of students is "+lines)
'''
        
print(max_list)
for characters in max_list:
        character.append(characters[0])
print(character)
for let in character:
    val = ord(f'{let}')
    lit.append(val)
print(lit)
'''
    

        
