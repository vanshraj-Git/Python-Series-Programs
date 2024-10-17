#9!/x +13!/x +17!/x +21!/x + .......N
import math as m
sum=0
a=9
n=int(input('no. of times you want to add='))
x=int(input('provide me x='))
for i in range (1,n+1):
    sum=sum+((m.factorial(a))/x)
    a+=4
print("Sum of series=",sum)