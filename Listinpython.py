l=[1,2,3,"Manish",4,5,6,7,True]
print(l)
print(type(l))
print(l[3])
print(l[-3])
if "Manish" in l:
    print("yes")
else:
    print("No")

if "Ma" in "Manish": # same apply for string
    print("yes")

print(l[:])
print(l[0:8])
print(l[0:8:2]) #2-means len(2-1) (step -1)
print(l[-3])

lst=[i for i in range(20)]#on the way list creation
lst2=lst=[i for i in range(20) if i%2==0]
print(lst2)