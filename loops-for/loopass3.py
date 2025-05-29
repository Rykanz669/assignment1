numbers = (1,2,3,4,5,6,7,8,9,10)
for i in range(1,11):
    if i % 3 == 0:
        continue
    print(f"square of {i} is {i**2}")