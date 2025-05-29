username = "goku"
password = "kakarot"

write_username = input("enter username: ")
write_password = input("enter password: ")

if username == write_username and password == write_password:
    print("login sucessful")
else:
    print("login failed")