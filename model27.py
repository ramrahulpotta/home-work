num = int(input("enter a no:"))
factorial = 1
if num < 0:
   print("doesn't exist")
else:
   for x in range(1,num + 1):
       factorial = factorial*x
   print(factorial)
