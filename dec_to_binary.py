'''
def binary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')

# Take decimal number from user
dec = int(input("Enter an integer: "))
binary(dec)

'''
def binary(n):
    if n>1:
        print(binary(n//2))
    print(n%2,end='')


T = int(input())
for i in range(T):
    n = int(input())
    binary(n)
    print ("\r")