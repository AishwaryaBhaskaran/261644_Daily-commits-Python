#print repeated tuples in python
tup=(1,2,2,3,45,2)
for i in tup:
    if tup.count(i)>1:
        print(i)
        break