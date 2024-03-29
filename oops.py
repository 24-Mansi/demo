# oops- the language which is based on object and class are called oops.
#python is object oriented language.

# class- is the blue print which consists of all the properties and functionality state or behaviour.
# or class will tell the user how to store the data and how to uiloize the stored data.

# object- it is the instance (example) of class.


# syntax to define class
# class classname:
#     properties/functionalities/variables
#     state/behaviour/methods


#syntax to create object
# objectname = classname(arg)

# class A:
#     pass   pass is a keyword used to make empty class and shows thst class needs a development for now and will pass all the values.
# onj=A()    in this case no need to use object but used when need to make class member.


#classmemeber------properties which remain same for all the objects.


#objectmember------properties which differs from object to object.


#__init__  -magic method used to save the data and initialize the data in object.
#it is compulsory to pass self as 1st argument, rest can be any objectmember.
#no need to pass the self because it is default passed in classname.(self takes the address of any object member)

#school.__dict__ - it will show all the methods of classname / details of the class we have created.
#st1.__dict__  - it will show all the object instances / details.


# methods---- functions written inside the class 
# 1. class method
# 2. object method
# 3. static method

# calling the object methods using class name
# classname.methodname(self,args)



# class school:
#     schoolname='abc'
#     principal='adnan'
#     schoolsadd='ropar'
#     def __init__(self,stname,rollno,stadd):
#         self.stname=stname
#         self.rollno=rollno
#         self.stadd=stadd
#     def ch_rollno(self,new):
#         self.rollno=new

#     def display(self):
#         print(self.stname,self.rollno,self.stadd)


#     @classmethod
#     def ch_principal(cls,new):
#         cls.principal=new                      #school.principal


#     @classmethod
#     def ch_schooladd(cls,newadd):
#         cls.schooladd=newadd


# st1= school('ameer',23,'kashmir')
# st2= school('irshad',1,'kashmir')

# school.ch_princi('arsalan')
# school.ch_schooladd('punjab')
# st1.ch_schooladd('chandigarh')       #change with object members

# st1.display()

# print(st1.__dict__)
# st1.ch_rollno(5)
# print(st1.__dict__)

# print(school.__dict__)
# print(st1.__dict__)


#not possible to display object name/member using classs name  (when to do so we have to pass the argument as self)
#possible to display class member using object name
# print(school.schoolname)
# print(school.schoolname,school.principal)
# print(st1.schoolname)
# print(st2.schoolname)
# print(school.stname)

# print(schoolname.st1)



class family:
    famhead='father'
    homeadd='jogindernagar'
    homedist='mandi'
    def __init__(self,memname,memage,memheight):
        self.memname=memname
        self.memage=memage
        self.memheight=memheight

    
    @classmethod
    def ch_homeadd(cls,newadd):
        cls.homeadd=newadd
    
mem1= family('mehar',57,5.8)
mem2= family('archana',47,5.2)
mem3= family('koshika',23,5.5)
mem4= family('mansi',21,5.4)
mem5= family('sahil',19,5.11)

family.ch_homeadd('punjab') 
print(family.homeadd)
mem1.ch_homeadd('punjab')

print(family.ch_homeadd('chandigarh'))
print(family.homeadd)

# print(family.__dict__)
# print(mem1.__dict__)






