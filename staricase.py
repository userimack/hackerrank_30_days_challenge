import sys
n = int(raw_input().strip())

# for i in range(n+1):
#     for j in range(n-i,0,-1):
#         print ("  ",sep='', end=' ')
#     for j in range(i):
#         print ("#", sep='',end=' ')
#     print ("\r")

for i in range(1,n+1):
    for j in range(n-i,1,-1):
        sys.stdout.write(' ')
    for j in range(i):
        sys.stdout.write("#")
    print('\r')