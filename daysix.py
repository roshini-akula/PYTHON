print(type(d))
for k in d.values():
    print(k)
for k in d.values():
    print(k,end=" ")
for k in d.items():
    print(k)
for a,b in d.items():
    print(a," ",b)
print("enter something")
a=int(input())
d={}
for i in range(5):
    k=input("enter key")
    v=input("enter the value")
    d.update({k:v})
    print(d)
m=[1014,2089,5098,5678]
n=["shub","rohan","jay","krish"]
mydata=dict(zip(m,n))
print(mydata)
print(zip(m,n))

    
    
