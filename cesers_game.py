def caesar_encrypt(word):
    c = ''
    for i in word:
        if (i == ''):
            c += ''
        else:
            c += (chr(ord(i) + 3))
    return c

def caesar_decrypt(word):
    c = ''
    for i in word:
        if (i == ''):
            c += ''
        else:
            c += (chr(ord(i) - 3))
    return c
  
number=input()
inc_dec = int(input("1 for encryption and 0 for decryption :"))
message = input()
if (inc_dec == 1):
    print(caesar_encrypt(message))
elif(inc_dec == 0):
    print(caesar_decrypt(message))
else:
    print("Enter incdec = 1 to encrytion and incdec = 0 ")