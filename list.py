#Find out second smallest number in list
my_list=[3,7,1,2,0,2,3]
final_list=[]
for i in my_list:
    if i not in final_list:
        final_list.append(i)
final_list.sort()
print(final_list[1])