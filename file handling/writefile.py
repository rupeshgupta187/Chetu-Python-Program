file=open("text2.txt","w")
for x in range(5):
    name=input("enter times name : ")
    file.write(name)
    file.write('\n')
file.close()