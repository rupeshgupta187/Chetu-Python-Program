from multipledispatch import dispatch

class Product:
    @dispatch(int,int)
    def product(first,second):
        result=first*second
        print(result)
    @dispatch(int,int,int)
    def product(first,second,third):
        result=first*second*third
        print(result)
    @dispatch(float,float)
    def product(first,second):
        result=first*second
    @dispatch(str,str)
    def product(first,second):
        print(first+second)
ob=Product()
ob.product(23,45)
ob.product(23,45,45)
ob.product(23.4,45.5)
ob.product("rupesh ","Aman")