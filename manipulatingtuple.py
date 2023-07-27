#convert the tuple in the list and do changes

tup=(1,2,3,4,5,6,7)
lst=list(tup)
print(lst)
lst.insert(0,220)
print(lst)
tup=tuple(lst)
print(tup)
r=tup.index(1)
print(r)