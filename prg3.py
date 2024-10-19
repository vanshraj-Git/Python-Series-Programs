#2-6+18-54+.... n
sum=0
a=2
d=-6
n=int(input("no. of times="))
for i in range (1,n+1):
    if i%2!=0:
        sum=sum+a 
        a*=9
        print("sum of series=",sum)     
    elif i%2==0:
        sum=sum+d
        d*=9  
        print("sum of series=",sum)     