lower=int(input("enter start no"))
upper=int(input("enter upper no:"))

for x in range(lower,upper + 1):
   if x > 1:
       for i in range(2,x):
           if (x % i) == 0:
               break
       else:
           print(x)