bad=["bad","worst","ugly","disgusting","poor","so mean"]
good=["good","beatiful","fantastic","instresting","superb"]
user_input=input("enter your rating :").split()

for x in user_input:
    for y in bad:
        if x==y:
            print("bad rating ")

    for z in good:
        if x==z:
            print("Good rating")
new=[]
for c,t in zip(bad,good):
    if bad(c)==user_input:
        print("bad rating")
    elif good[t]==user_input:
        print("good rating")        
    