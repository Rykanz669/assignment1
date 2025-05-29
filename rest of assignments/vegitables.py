total_amount = input("enter purchase amount")

if total_amount > "100":
    print("discount given 10%")
elif total_amount > "50":
    print("discount given 5%")
elif total_amount < "50":
    print("no discount")