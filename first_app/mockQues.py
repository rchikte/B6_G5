
#print lambda function using all types of arguments ?


import pymysql


def func(a,b,c=10,*args,**kwargs):
    return a,b,c,args,kwargs

# print(func(1,2,20,30,n1=5,n2=6))


# def func(a=100,d):
#     return a,d

# print(func(d=200))



res1 =lambda a,b,d,c=10,*args,**kwargs:(a,b,d,c,args,kwargs)
print(res1(1,2,10,d=20,n1=5,n2=6))


# res = lambda a,b,c=10,*args,**kwargs:a+b+c+args[0]+sum(kwargs.values())
# print(res(1,2,20,30,n1=5,n2=6))

class DatabaseManager():
    def __init__(self, databasename):
        self.Databasename = databasename
        print("Database name:- ",self.Databasename)
        
          
    def __enter__(self):
        self.conn = pymysql.connect(host="localhost",user="root",password="1234",database=self.Databasename)
        print("Connection Established")
        return self.conn
      
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("connection closed")
        self.conn.close()
  
# loading a database connection 
with DatabaseManager('world') as c:
    print("in with block")





















