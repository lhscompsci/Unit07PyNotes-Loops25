# A while loop is a block of code
# associated with a condition.
# As long as that condition is true,
# the loop body (block of code)
# will continue to execute

#general format:
#while ( some boolean condition ):
#   do something
#   do something else
#   and so on

x = 30
while ( x > 5 ):
    print(x)
    x -= 4 #updater


# access individual digits within a number
num = 9134
print(num % 10)
print(num // 10)
sum = 0
while (num > 0):
    sum += (num%10)
    num = num // 10
print(sum)

# for loop
for num in range(10):
    print(num)

for x in range(3):
    print("Howdy")

for val in range(17,24):
    print(val)

for r in range (1,15,2):
    print(r)

for c in range(25,7,-5):
    print(c)

for bob in "Hello":
    print(bob)


word = "Computer Science"
for w in word:
    if w == "u":
        break
    print(w)