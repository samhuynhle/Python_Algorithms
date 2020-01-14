# Recursive function sneed to have a break condition
# break condition prevents infinite loops
# Each time the function is called, the old arguments are saved
# This is called the "call stack"

# Examples of Recursion
def countdown(x):
    if (x==0):
        print("done")
        return
    else:
        print(x, "...")
        countdown(x-1)

def power(num, pwr):
    if power == 0:
        return 1
    else: 
        return num * power(num, pwr-1)

def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)

def efun(num):
    if num==0:
        return 1
    else:
        return num * efun(num-2)

print(efun(8))