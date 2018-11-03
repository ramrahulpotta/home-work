employeename = input("enter name:")
designation = input("designation:")
if designation == "manager":
    salary = int(input("salary:"))
    after_hike = salary+(salary*20)/100
    print(after_hike)
elif designation == "analyst":
        salary = int(input("salary:"))
        after_hike = salary+(salary*10)/100
        print(after_hike)
elif designation == "clerk":
            salary = int(input("salary:"))
            after_hike = salary+(salary*5)/100
            print(after_hike)
else:
    print("no hike")
print("thanks")



