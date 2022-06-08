numbers = list(input().split())
def Palindrome(number):
    return number == number[::-1]

output=False;
isPositive=True;

for number in numbers:
    isPositive = isPositive and int(number)>0
    answer = Palindrome(number)
    output = output or answer

print(isPositive and output)
