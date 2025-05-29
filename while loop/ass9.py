dic = {}
for i in range(3):
    key=input("enter key")
    val=int(input("enter value"))
    dic.update({key:val})
greatest=0
greatest_name=""
for i in dic:
    if dic[i]>greatest:
        greatest+dic[i]
        greatest_name=i
print(greatest_name,greatest)
