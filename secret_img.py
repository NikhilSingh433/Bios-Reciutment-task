image_names = list(input().split())

no_bmp = 0
no_jpg = 0
no_png = 0
s = ''
for name in image_names :
    j =s.join(name)
	
    if (j.endswith('.png')) :
        no_png = no_png +1
    elif(j.endswith('.jpeg')) :
        no_jpg =no_jpg +1
    elif(j.endswith('.bmp') ):
        no_bmp =no_bmp + 1

print(no_png,no_bmp,no_jpg)
