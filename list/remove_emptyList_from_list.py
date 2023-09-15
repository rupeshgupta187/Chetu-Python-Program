# list=[[],12,23,['rup',"raja","ram"],1,2,3,[]]
# b=[]
# for x in list:
#     if (type(x)==list):
#         continue
#     b.append(x)
    
   
# print(b)

list_of_lists = [[1, 2, 3], [], [4, 5], [], [], [6, 7]]

# Use the filter function to remove blank lists
filtered_list = list(filter(None, list_of_lists))

print(filtered_list)

test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]
 
# printing both lists
print ("The original list 1 : " + str(test_list1))
print ("The original list 2 : " + str(test_list2))
 
# using naive method
# Uncommon elements in List
