# days=[
#     ("Monday","Mon",1),
#     ("Tuesday","Tue",2),
#     ("Wednesday","Wed",3),
#     ("Thursady","Thu",4),
#     ("Friday","Fri",5),
#     ("Saturday","Sat",6),
#     ("Sunday","Sun",7),
# ]
# input_days=input("enter days of weeks :")
# flag=False
# for full_day, abbrev, number in days:
#     if input_days.capitalize()=="abbrev" or number:
#         print(f'{full_day}')
#         flag=True
#         break
# if not flag:
#     print("enter valid abbre or number to get the present days of weeks ")


days_list = [
    ("Monday", "Mon", 1),
    ("Tuesday", "Tue", 2),
    ("Wednesday", "Wed", 3),
    ("Thursday", "Thu", 4),
    ("Friday", "Fri", 5),
    ("Saturday", "Sat", 6),
    ("Sunday", "Sun", 7)
]

# Input the day of the week
day_input = input("Enter the day of the week: ")

# Check if the input is valid
found = False
for full_day, abbrev, number in days_list:
    if day_input.capitalize() == abbrev or number :
        print(f"{full_day} ")
        found = True
        

if not found:
    print("Invalid input. Please enter a valid day of the week.")