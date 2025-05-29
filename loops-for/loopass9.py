names = ("sam","john","bob","alice")
for i in names:
    i==int(i)
    if i >= 0:
        print(f"{names[i]}".upper)
    else:
         print(f"{names[i]}".capitalize)
print(names)