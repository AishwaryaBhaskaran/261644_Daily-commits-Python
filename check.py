#Write a python program to check if the input number is-real number-float numner-string-complex number-Zero (0
def check(num):
 if type(num)==int:
    print("Integer")
 elif type(num)==complex:
    print("complex")
 elif type(num)==float:
    print("float")
 elif type(num)==str:
     print("string")
 else:
    print("zero")

a=10
b="Hai"
c=0
d=2.44
mynum=check(a)
print(mynum)
mynum=check(b)
print(mynum)
mynum=check(c)
print(mynum)
mynum=check(d)
print(mynum)