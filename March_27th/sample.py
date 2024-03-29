n=int(input("enter number:"))
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
if c>0:
    print("Not Prime")
else:
    print("Prime")
