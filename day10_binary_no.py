def binary(n):
    if n>1:
        binary(n//2)
    print(n%2,end='')


T = int(input())
for i in range(T):
    n = int(input())
    binary(n)
    print ("\r")