num=int(input("enter the value:"))
i=1
count=0
for i in range(i,num+1):
    if(num%i==0):
        count=count+1
if(count==2):
    print("Prime number")
else:
    print("Not a prime number")
