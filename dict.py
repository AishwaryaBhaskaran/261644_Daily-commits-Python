#Merge two dictionaries
def Merge(dict1,dict2):
  return dict1.update(dict2)

dict1={'1':1}
dict2={'2':2}

print(Merge(dict1, dict2))

print(dict1)
