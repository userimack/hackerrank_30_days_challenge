def find_gcd(x,y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
   #write base condition
    #return find_gcd(b,a%b)
#Take input
a,b = raw_input().split()
gcd=find_gcd(int(a),int(b))
print gcd
