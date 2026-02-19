#travesing in arrays
numbers=[10,25,30,45,50,65,70,85,90,105]
even=[]
odd=[]
for i in range(0,len(numbers),2):
    odd.append(numbers[i])
for i in range(1,len(numbers),2):
    even.append(numbers[i])
print(even)
print(odd)

numbers=[10,25,30,45,50,65,70,85,90,105]
even=[]
odd=[]
for i in range(len(numbers)):
    if i % 2 == 0:
        even.append(numbers[i])
    else:
       odd.append(numbers[i])
print(even)
print(odd)

#searching in arrays
numbers=[11,2,3,40,44,55,66,77,88]
l= len(numbers)
for i in range(l):
    if numbers[i]==2:
       print("found at :",i)
        break
else:
    print("not found")
