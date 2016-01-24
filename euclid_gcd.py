"""
def find_gcd(a,b):
   #write base condition
    if a==b:
        return a
    else:
        return find_gcd(max(a,b)-min(a,b),min(a,b))
    #return find_gcd(b,a%b)
    """
#Take input
a,b=raw_input().split()
gcd=find_gcd(int(a),int(b))
print gcd
    

def find_gcd(x,y):
    """
    a= max(a,b)
    b=min(a,b)

    if a==b:
        return a
    elif (A!=0 and b!=0)
        return find_gcd(a%b,b)
        """
    while y != 0:
        (x, y) = (y, x % y)
    return x


"""
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
    
"""