n = int(input("number of test cases: "))   # number of test cases
for i in range(0,n): 
    a, b, r = list(map(int,input("enter a , b and r: ").strip().split()))
    chopstick_in_jar = input("Number of chopstick in the Jar: ")   # number of chop stick 
    length_of_chopsticks = list(map(int,input("Enter Lengths of chopstick: ").strip().split()))
    chop = 0
#find the possible number of triangles
    for len in length_of_chopsticks: 
         c = int(len)
         if a+b > c and a+c > b and b+c > a: 
            chop = chop + 1

    print(chop) 

    if chop > r:

        print("Natsu")
    else: 
        print("Grey")
