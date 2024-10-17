#1^(3)/x+3^(3)/x+5^(3)/x+....N
sum=0
a=1
n=int(input('No. of times='))
x=int(input('give me x='))
for i in range (1,n+1):
    sum=sum+a**3/x
    a+=2
print("sum of the series",sum)
