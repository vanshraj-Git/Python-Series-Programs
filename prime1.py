prime=29
flag=0
for i in range(2,(prime//2)+1):
    if(prime %i==0):
        flag=1
        print(f"{i} is a factor of {prime}")
if(flag==0):
    print(f"{prime} is a prime no.")