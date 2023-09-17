def factorial(n):
    if n == 0:
        return 1 
    return n * factorial(n-1) 
n = [1,2,3,4,5,6,7,8,9] 
for i in n:
    print(f'{i}! = {factorial(i)}') 
