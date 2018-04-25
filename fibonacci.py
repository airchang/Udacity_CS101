#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    before = 0
    current = 1
    for i in range(0,n-1):
        before, current= current, current+before
    return current


print fibonacci(36)
#>>> 14930352
