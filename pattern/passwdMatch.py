# passwd=[123]
# user=input('enter password :').split()
# result=0
# if(passwd==user):
#     print("pasword are matched :")
# else:
#     for i in range(len(user)):
#         if(passwd[i]==user[i]):
#             result='1'
#         else:
#             result='0'
# print(result)


inp1=eval(input("enter first  number :"))
inp2=eval(input("enter  second number "))
# if(type(inp1)==int and type(inp2)==int):
print('sum of inp1 and inp2 is :',inp1+inp2)

if(type(inp1)==str and type(inp2)==str):
    print('sum of inp1 and inp2 is :',inp1+inp2)

if(type(inp1)==float and type(inp2)==int):
    print('sum of inp1 and inp2 is :',inp1+inp2)

if(type(inp1)==int and type(inp2)==float):
    print('sum of inp1 and inp2 is :',inp1+inp2)

if(type(inp1)==str and type(inp2)==int):
    print('sum of inp1 and inp2 is :',int(inp1)+inp2)   

if(type(inp1)==int and type(inp2)==str):
    print('sum of inp1 and inp2 is :',inp1+int(inp2)) 

    #########################################################################

