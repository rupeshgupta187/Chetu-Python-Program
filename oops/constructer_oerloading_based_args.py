class Sample:
    def __init__(self,*args):
        if len(args)>1:
            self.ans=0
            for i in args:
                self.ans+=i
        elif isinstance(args[0],int):
            self.ans=args[0]*args[0]
        
        #if args is string print with hello "
        elif isinstance(args[0],str):
            self.ans="Hello " +args[0]
s1=Sample(12,34,5,56,76)
print("sum of list is :",s1.ans)
s2=Sample(5)
print("Squre is ",s2.ans)
s3=Sample("GeeksforGeeks")
print("String :",s3.ans)
