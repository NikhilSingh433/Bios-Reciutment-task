no_of_students = int(input())
list = []
num = []
nl = []
for i in range(0,no_of_students):
    name = input()
    marks = float(input())
    num.append(marks)
    list.append([name,marks])
num.sort()   # sorting the marks
num.reverse()
c = num.count(min(num))
number=num[len(num)-c-1]
for i in range(0,no_of_students):
    if(number==list[i][1]):
        nl.append(list[i][0])
        nl.sort()
for x in range(len(nl)):
    print (nl[x])