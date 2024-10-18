#x+2/10+x+4/30+x+6/90+ ..........n
sum=0
a=2
d=10
n=int(input("no. of times="))
x=int(input("x value ="))
for i in range(1,n+1):
    sum=sum+((x+a)/d)
    a+=2
    d*=3
    print("Sum of series=",sum)
