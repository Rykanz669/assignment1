numbers = [1,2,3,4,5]
for i in range(5):
    numbers.append(int(input(f"enter number{i+1}: ")))

for num in numbers:
    if num == i:
        print("found")
        break
else:
    print("not found")
   



