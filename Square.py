#x^(1)+x^(2)+x^(3)+.... +n
sum=0
a=1
n=int(input("nth term of the series"))
x=int(input("x value ="))
for i in range (1,n+1):
    sum=sum+x**a
    a+=1
print("Sum of series=",sum)
