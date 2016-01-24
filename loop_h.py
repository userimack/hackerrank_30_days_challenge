# T = int(raw_input())


# for loop in range(T):
#     a = int(raw_input()) 
#     b = int(raw_input())
#     N = int(raw_input())
#     for i in range(0,N):
#         sum=a;
#         for j in range(i+1):
#             sum+=(2**j)*b
#         print sum,
#     print "\n"



T = int(raw_input())
for loop in range(T):
    
    a,b,N = raw_input().split()
    a=int(a)
    b=int(b)
    N=int(N)
    for i in range(N):
        s=a;
        for j in range(i+1):
            s+=(2**j)*b
        print (s),
    print "\r"

# from sys import stdout
# T = int(input())

# for loop in range(T):    
#     a,b,N = input().split()
#     a=int(a)
#     b=int(b)
#     N=int(N)
#     for i in range(N):
#         s=a;
#         for j in range(i+1):
#             s+=(2**j)*b
#         print (s, end=" ")
#     stdout.flush()