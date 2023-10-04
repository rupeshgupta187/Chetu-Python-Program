file=open("text3.txt","w")
list=[]
for x in range(5):
    name=input("enter a name of candidate : ")
    list.append(name)
file.writelines(list)
file.writelines("\n")
file.close()