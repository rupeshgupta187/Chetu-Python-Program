def update(a, user):
    a=a[:-len(user)]
    a+=user
    return a
user=input("enter a number ")
a="C000000"
value=update(a, user)
print(value)
