my_list=[1,2]
new_dict=current={}
for num in my_list:
    current[num]={ }
    current=current[num]
print(new_dict)
