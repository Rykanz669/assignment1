data = [{
    "name":"prashanth",
    "age": 45,
},

{
    "name":"kareem",
    "age": 49,
}]

def extract_ages(details):
    age_1=details[0]["age"]
    age_2=details[1]["age"]
    return[age_1,age_2]

age=extract_ages(data)
print(age)