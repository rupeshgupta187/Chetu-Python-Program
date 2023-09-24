dict={
    342:"rupesh",
    232:"shivam",
    231:"viresh",
    234: "aditya"
}

for x in dict.keys():
    print(x,end=" ")
print()

for x in dict.values():
    print(x,end=" ")

for x,y in dict.items():
    print(f"keys is : {x} -->{y}")