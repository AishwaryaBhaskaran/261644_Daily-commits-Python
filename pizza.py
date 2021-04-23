#Write Python code that asks a user how many pizza slices they want.The pizzeria charges Rs 123.00 a slice. if user order even number of slices, price per slice is Rs 120.00. Print the total price depending on how many slices user orders.
x=int(input())
sum=0
if x%2==0:
    sum=120.00*x
else:
    sum=123.00*x
print(sum)
