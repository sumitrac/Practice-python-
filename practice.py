print(" ------------------------------------")
print("| Practice python loops and iteration |")
print(" -------------------------------------\n")

num = 0
while(num <= 10):
    print(num)
    num += 2

print("\n")
sum = 0
i = 1

while i <= 5:
    sum = sum + i
    i = i + 1    # update counter

print(f"The Sum is {sum}")

# problem 1
for i in range(2):
    print("dance!")  #dance! #dance! 

# problem 2
for i in range(10):
    print(i) # 0,1,2,3,4,5,6,7,8,9


# problem 3
for i in range(3):
    print("coding!")
print("fun!") #coding! coding! coding! fun!

# problem 4
for x in range(5):
    print(f"{x} chicken(s)") #0 chicken(s) 1 chicken(s) 2 chicken(s) 3 chicken(s) 4 chicken(s)

# problem 5
for i in range(10):
    print(i*10) #0 10 20 30 40 50 60 70 80 90

# problem 6
for i in range(1, 5):
    print("hello") #hello hello hello hello 

# problem 7
for i in range(1, 4):
    print(f"{i} animal(s)") #1 animal(s) 2 animal(s) 3 animal(s)

# problem 8
for i in range(1, 4):
    print(i * i) #1 4 9 

print("\n")
# problem 9
total = 0
for i in range(1, 4):
    total = total + 1
 
print(total) # 12------------------

# problem 10
for x in range(1, 11):
    if x == 5:
        print("You got a winner!") #none none none none none, you got a winner!

