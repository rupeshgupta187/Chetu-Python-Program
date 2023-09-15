# string=["rupesh",2,4,True,"vishal"]
# list=[]
# for x in string:
#     if type(x)==str:
#         x=len(x)
#         list.append(string[x])
# print(list)

def find_string_indices(input_list):
    string_indices = []
    
    for i, element in enumerate(input_list):
        if isinstance(element, str):
            string_indices.append(i)
    
    return string_indices

# Example usage:
input_list = [1, "hello", 3.14, True, "world", False, "Python"]
string_indices = find_string_indices(input_list)

if len(string_indices) > 0:
    print("String indices in the list are:", string_indices)
else:
    print("No string elements found in the list.")