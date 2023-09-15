string=input("enter a string : ")
s=string.split()[::-1]
l=[]
for x in s:
    l.append(x)
print(" ".join(l))

#####################################################

# def find_unmatched_characters(str1, str2):
#     unmatched_characters = []

#     for char1 in str1:
#         found = False
#         for char2 in str2:
#             if char1 == char2:
#                 found = True
#                 break

#         if not found:
#             unmatched_characters.append(char1)

#     return unmatched_characters

# # Input two strings
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# unmatched_chars = find_unmatched_characters(string1, string2)

# if unmatched_chars:
#     print("Unmatched characters:", unmatched_chars)
# else:
#      print("No unmatched characters found.")