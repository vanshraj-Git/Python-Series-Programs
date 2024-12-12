sum=0
for i in range(2,101):
    flag=0
    for j in range(2,int(i//2)+1):
        if (i%j==0):
            flag=1
            break
    if flag==0:
        sum=sum+1
        print(i)
print("total no. of prime no.'s from 0 to 1000 = ",sum)


