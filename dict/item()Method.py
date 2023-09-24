dict={
    342:"rupesh",
    232:"shivam",
    231:"viresh",
    234: "aditya"
}

for s in dict.keys():
    # print(s,end=" ")
    # print(dict[s],end=" ")
    print(dict.get(s),end=" ")

for x in dict.items():
    print(x)