# 2+4+6...n
# n is no. of time it is executed not the last term
# a is used as starting variable and for addintion inside the loop
n=4
sum=0
a=2
for i in range(0,n):
    sum=sum+a
    a+=2
    print("Sum of series=",sum)

