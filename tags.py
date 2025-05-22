tags = {"python","fastapi","backend"}
new_tag = input("enter new tag: ").strip().lower()
if new_tag in tags:
    print("tag already exists")
else:
    tags.add(new_tag)
    print("updated tags",tags)
