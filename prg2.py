#(x+5^(2))/(1+2)+(x+25^(2))/(2+3)+..... n
sum=0
a=3
d=5
n=int(input("no. of times="))
x=int(input("x value ="))
for i in range(1,n+1):
    c=d**2
    sum=sum+((x+c)/a)
    a+=2
    d*=5
print("sum of the series=",sum)