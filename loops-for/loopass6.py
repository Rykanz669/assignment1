dic = {
    "apple":2,
    "banana":3,
    "apricot":4,
    "berry":5,
}
total_value=1
for i in dic:
    if i[0]=="a":
        total_value*=dic[i]
print(total_value)

