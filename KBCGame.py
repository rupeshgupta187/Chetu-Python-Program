questions=[
    [
        "Which was languaged used to create the Facebook",
        "Python","JavaScript","Java","C#",4 
    ],
    [
        "which one is the next prime minister of india ?","Narendra Modi","Rahul Gandhi","Ashok Gahlot","Sachin Pailet",1
    ],
    [
       " In which year G-20 held ","2023","2022","2018","2020",1
    ],
    [
        "Which country organised G-20 Submission ?","India","Amerika","Rusia","China",1
    ]


]

levels=[1000,2000,4000,10000,20000,100000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for the {levels[i]}")
    print(f"{question[0]}")

    print(f" a. {question[1]}                       b. {question[2]}")
    print(f" c. {question[3]}                       d. {question[4]}")
    ans=int(input("Enter your answer answer betweet 1 to 4 : "))
    if ans==0:
        money=levels[i-1]
        break
    elif ans==question[-1]:
        print(f"congratulation!! You have won the {levels[i]}\n")
        if i==4:
            money=1000
        elif i==13:
            money=5000000
        elif i==9:
            money=100000
        elif i==14:
            money=10000000

    else:
        print("Your answer is wrong sorry!!")
