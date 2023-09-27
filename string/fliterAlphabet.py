string="Hey! I am here for# you only??@"

user_input=string.split()
print(string)
b=[]
for x in string:
    if x.isalpha():
        b.append(x)


string1="".join(b)
print(string1)
count=0
for x in string1:
    
     count+=1
print("count is :",count)
