# nested loops
for x in range(3):
    print("x is ", x)
    for y in range(2):
        print("y is ", y)
    print("\n")

for x in range(3):
    for y in range(4):
        print("(", x,", ", y ,")")

for i in range(10,0,-1):
    for j in range(i):
        print(" ",end="")
    for j in range(i,10):
        print("*",end="")
    print()

'''
how many lines do you want? __

&&&&&&&
 &&&&&
  &&&
   &
'''