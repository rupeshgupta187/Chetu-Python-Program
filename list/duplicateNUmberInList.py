# unique=[]
# duplicate=set()
# list=[12,12,34,56,67,46,45,45,45,22,22,44,44,44,]
# count=0
# for x in list:
    
#     if x in unique:
#         duplicate.add(x)
#         count+=1
#     else:
#         unique.append(x)

# print("duplicate values is :",duplicate,"count of duplicate is :",count)
# print("unique value is :",unique)

# print("*"*20)

def repeate(x):
    size=len(x)
    repeated=[]
    uni=[]
    for i in range(size):
        for j in range(1,size):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
            if x[j] in range(size):
                uni.append(x[j] ) 
            return uni
            
    return repeated
list1=[10,20,30,34,23,23,33,33,22,24,24,22,22]
print(repeate(list1))

