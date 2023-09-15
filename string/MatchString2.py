a="abc"
b="aaabbcc"

for x in a:
    b=b.replace(x,"")
if len(b)==0:
    print("matched")
else:
    print("not matched")

