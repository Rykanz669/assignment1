total = 0
count = 0

while total < 100:
    num = int(input("enter a number: "))
    total += num
    count += 1
    break
print(f"total count reached. number: {count}")