#2+6+18+... n
sum=0
a=2
n=int(input('no. of times you want to add='))
for i in range(1,n+1):
    sum=sum+a
    a*=3
    print("Sum of series=",sum) 