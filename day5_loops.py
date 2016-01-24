#Python3
#from sys import stdout
T = int(input())

for loop in range(T):    
    a,b,N = input().split()
    a=int(a)
    b=int(b)
    N=int(N)
    for i in range(N):
        s=a;
        for j in range(i+1):
            s+=(2**j)*b
        print (s, end=" ")
    print('\r')


# #Python2
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# T = int(raw_input())
# for loop in range(T):    
#     a,b,N = raw_input().split()
#     a=int(a)
#     b=int(b)
#     N=int(N)
#     for i in range(N):
#         s=a;
#         for j in range(i+1):
#             s+=(2**j)*b
#         print (s),
#     print "\r"
