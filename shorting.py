string = input()
b= list(string)
sorts=''
L_case=[]
U_case=[]
No_odd=[]
No_even=[]
for i in range(len(b)):
    if (ord(b[i]) >=97 and ord(b[i])<= 122 ):
        L_case.append(b[i])
    elif(ord(b[i])>=65 and ord(b[i])<=90):
        U_case.append(b[i])
    elif(ord(b[i]) >= 48 and ord(b[i])<=57):
        if(ord(b[i]) % 2 != 0):
            No_odd.append(b[i])
        else:
            No_even.append(b[i])
L_case.sort()
U_case.sort()
No_odd.sort()
No_even.sort()
L_case = L_case + U_case + No_odd + No_even
string = sorts.join(L_case)
print(string)    # the sorted element 