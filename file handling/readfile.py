file=open("text.txt","r")
str=""
while str:
    str=file.readlines()
    print(str,end="")

