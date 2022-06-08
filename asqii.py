strings = list(input().split())
a = list(strings[0])
b = list(strings[1])
sum = 0
num = 0
for i in a:
        sum = sum + ord(i)


for i in b:
    num = num + ord(i)

if (sum == num):
    print("True")
else:
    print("False")