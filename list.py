"""
n = input("n: ")
name= []
no = []
for i in range(n):
    #obj=raw_input()
    name.append(raw_input("Name "))
    no.append(input("No "))

print name
print no
for i in range(n):
    flag=0
    na  = raw_input("key ")
    for j in range(n):
        print j
        print name[j]
        if name[j]==na:
            flag=1
            #index=j
            print "index"+str(j)
            print na+"="+str(no[j])
            break

    if flag==0:
        #print na+"="+str(no[j])
        print "Not found"

"""
n = input()
name= []
no = []
for i in range(n):    
    name.append(raw_input())
    no.append(input())
    
for i in range(n):
    flag=0
    na  = raw_input()
    for j in range(n):    
        if name[j]==na:
            flag=1
            #index=j            
            break

    if flag==1:
        print na+"="+str(no[j])
    else:
        print "Not found"
