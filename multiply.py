product = 1
i = 0
numbers = list(map(int,input().strip().split()))
for i in range(len(numbers)):
    product = product* numbers[i]
    i=i+1


print("\n ", product)
