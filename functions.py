# set of instructions which will get executed when someomne calls the function.
# these are of two types:
# 1. inbuilt functions
# 2. userdefined functions

# inbuilt functions: the functions which are predefined by the developer, as a user we can call those functions for 'n'
# number of times, it is not possible to modify the functions.

# userdefined functions: the functions which are defined by the user are called as userdefined.


#syntax to create a function
#def functionname(args):
#    S.B
#    return/print

# syntax used to call a function
# functionname(args)


# def uppercase():
#     s=input('enter the string=')
#     out=''
#     for i in s:
#         if 'A'<=i<='Z':
#             out+=i
#     # print(out)
# # uppercase()
#     return out
# print(uppercase())


# def greet():
#     print("hello world")

# def greeting(name):
#     print(f'hello {name}')

# def add(a,b):
#     print(a+b)

# def sub(c,d,e):
#     print(c-d-e)

# greet()
# greeting('sajad')
# # greeting('umar','sajad')
# add(3,2)
# sub(4,5,6)


#wa function to extract all the integers from the list
# def sample():
#     l=eval(input('enter the list='))
#     out=[]
#     for i in l:
#         if type(i)==int:
#             out=out+[i]
#     print(out)
# sample()


# l=[1,2,'hii','hello',6j,4.5]
# def sample(l):   #l is just a argument name we can pass anything here
#     out=[]
#     for i in l:
#         if type(i)==int:
#             out+=[i]
#     print(out)
# sample(l)


# #wa function to extract all the even length strings from the tuple
# t=('hello','hiii','good','great','mornings')
# #o/p=('hii','good','mornings')
# def sample(a):
#     out=()
#     for i in t:
#         if len(i)%2==0:
#             out+=(i,)
#     print(out)
# sample(t)


# #wa function to extract all duplicate values from the tuple without using typecasting or builtin
# t=('hii',8,3,7.7,'hii',[1,2],[1,2],5j,7.7)
# #o/p=('hii',7.7,[1,2])
# def sample(a):
#     out=()
#     for i in a:
#         if a.count(i)>1:
#             if i not in out:
#                 out=out+(i,)
#     print(out)
# sample(t)


# #wa function to check whether the char is uppercase lowercase spcl character or number
# s='aV#2'
# #o/p='a' is lowercase
# #'V' is uppercse
# #'#' is spcl character
# #'2' is number
# def sample(a):
#     out=''
#     for i in a:
#         if 'a'<=i<='z':
#             print(i,'is lowercase')
#         elif 'A'<=i<='Z':
#             print(i,'is uppercase')
#         elif '0'<=i<='9':
#             print(i,'is number')
#         else:
#             print(i,'spcl character')
#         print(out)
# sample(s)


# #wa function to check the sum of all the integer numbers
# a=6543
# #o/p=18
# def sum(a):
#     count=0
#     for i in str(a):
#         count=count+int(i)
#     print(count)
# sum(a)


#wa function to delete all the duplicate values from the list
l=eval(input('enter the list='))
def delete(a):
    for i in l:
        if i not in a:
            
