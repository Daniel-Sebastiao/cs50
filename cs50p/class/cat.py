# Loops
# Ways to execute a code repeatedly
# Using While
iterator = 0
while iterator < 3:
    print("meow")
    iterator += 1

# Using For att: For is usually used to loop over list, which is a data type in Python.
for i in range(3):
    print("meow")

# When not using a variable, do the following...
for _ in range(3):
    print("meow")

# Using a controlled infinity loop
while True:
    n = int(input("How many times do you want to meow? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")



