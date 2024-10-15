# 1+2+3+4+5...n
# n is no. of time it is executed not the last term
# a is used as starting variable and for addintion inside the loop
n=10
sum=0
a=1
for i in range(0,n):
    sum=sum+a
    a+=1
    print("Sum of series=",sum)
