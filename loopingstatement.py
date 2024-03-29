#while loop
# n= int(input('enter the value='))
# i=1
# while i<=n:
#     print("hello world")
#     i=i+1

#wap to print numbers from 1-10
# i=0
# while i<=10:
#     print(i)
#     i=i+1
# i=0
# whilei<=10:
# print(i)
# i-i+1


#wap to print even numbers
# n=int(input('enter the value='))
# i=0
# while i<=n:
#     if i%2==0:
#         print(i)
#     i=i+1

# n=int(input('enter the value='))
# i=0
# while i<=n:
#       print(i)
#       i=i+2

#wap to print odd numbers
# n=int(input('enter the value='))
# i=0
# while i<=n:
#         if i%2!=0:
#             print(i)
#         i=i+1

# n=int(input('enter the value='))
# i=1
# while i<=n:
#     print(i)
#     i=i+2


#wap to extract lowercase alphabet from str
#s="HeLLo WorLD"
#o/p='eoor'
# s=input('enter the string=')
# i=0
# out='' 
# while i<len(s):
#     if 'a'<=s[i]<='z':
#         print(s[i])
#         out+=s[i]
#     i=i+1
# print(out)


#wap to print lowercase character from str
# s=input('enter the string=')
# i=0
# while i<len(s):
#     if 'a'<=s[i]<='z':
#         print(s[i])
#     i+=1


#wap to extract numeric character from the str
# s='h12gt34 %gsy'
# #o/p='1234'
# i=0
# res=''
# while i<len(s):
#     if '0'<=s[i]<='9':
#         res=res+s[i]
#     i+=1
# print(res)





####for loop------
# s='HEllo World'
# out=''
# for i in s:
#     if 'a' <=i<='z':
#         out+=1
# print(out)


# for i in 'hello':
#     print(i)
# for i in [1,2,3,4]:
#     print(i)
# for i in {1:2,2:3,3:4}:
#     print(i)
# for i in True:
#     print(i)


# #wap to extarct vowels from the str
# s='hello wolrd'
# out=''
# for i in s:
#     if i in 'aeiouAEIOU':
#         out=out+i
# print(out)

#wap to extarct consonants from the str
# s='hello wolrd'
# out=''
# for i in s:
#     if i not in 'aeiouAEIOU':
#         out=out+i
# print(out)


#wap to extract all the integers values from the list
# l=[10,20,30,"hello",4.3,[1,2]]
# #o/p=[10,20,30]
# out=[]
# for i in l:
#     if type(i)==int:
#         out=out+[i]
# print(out)


#wap to print all the str from the tuple
# t=(10,20,'hoo',8.9,'hello','python')
# out=''
# for i in t:
#     if type(i)==str:
#         out=out+(i)
# print(out)


#wapto extract all the individual datatypes from the list
# l=[10,'hello',9.7,[1,2],7j,23,{1,2},True]
# #o/p=[10,9.7,7j,23,True]
# out=[]
# for i in l:
#     if type(i)==int:
#         out=out+[i]
#     if type(i)==float:
#         out=out+[i]
#     if type(i)==complex:
#         out=out+[i]
#     if type(i)==bool:
#         out=out+[i]
# print(out)


#wap to extarct all the single value data from list
# l=[10,20,3.34,"hello",[1,2],{12,23},7j]
# #o/p=[10,20,3.34,7j]
# out=[]
# for i in l:
#     if type(i)==int:
#         out=out+[i]
#     if type(i)==float:
#         out=out+[i]
#     if type(i)==complex:
#         out=out+[i]
# print(out)
# #other way
# res=[]
# for i in l:
#     if type(i) in (int,float,complex):
#         res+=[i]
# print(res)


#wap to extract all the special characters from string
# s='he#21$Hi'
# #o/p='#$'
# out=''
# for i in s:
#     if not ('a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9'):
#         out=out+i
#     print(out)



###adding the length of the collection-----
# s='hai 251 bye hii 8 hello 64 how'
# #o/p=26 (for addition we use 0)
# num=0
# for i in s:
#     if '0'<=i<='9':
#         num=num+int(i)
# print(num) 

# s='hai 251 bye hii 8 hello 64 how'
# #o/p=1920 (for multiplication we use 1)
# num=1
# for i in s:
#     if '0'<=i<='9':
#         num=num*int(i)
# print(num) 


# t={9865,'hai',7j,'star',7.34,(1,2,3),False}
# #o/p=10
# length=0
# for i in t:
#     if type(i) in (str,list,tuple,set,dict):
#         length=length+len(i)
# print(length)


# t=[3,4,6,7,5,2,8]
# #o/p=20


# l=['shahid','sajad','anmol','mansi','sahil','zubair']
# #o/p=[2,2,2,2,2,3]
# out=[]   #[2]
# for i in l:    #i='sajad'
#     count=0
#     for char in i:     #char='a'
#             if char in 'aeiouAEIOU':
#                 count=count+1    #count=0+1
#     out=out+[count]    #out=[]+[2]
# print(out)


# d=['kriti','rana','raju','mallesh','shaan']
# #o/p=[2,2,2,2]
# out=[]
# for i in d:
#     count=0
#     for j in i:
#         if i.count(j)==2:
#             count+=1
#         out+=[count]
#     print(out)


# s='aabbcccdde'
# #o/p={'a':2,'b':2,'c':3,'d':2'e':1}
# out={}
# for i in s:
#     if i not in out:
#         out[i]=s.count(i)
# print(out)


# t=['amir','sajad','sahil','vivek','akash']
# #o/p=[]


# data={90:'apple','hii':'orange',3j:'grapes','b':'pineapple'}
# #o/p={90:'elppa',3j:'grapes'}
# out={}
# for i in data:
#     if type(i) in (int,float,complex,bool):
#         if i not in out:
#             if len(data[i])%2==1:
#                 out[i]=data[i] [::-1]
#             else:
#                 out[i]=data[i]
# print(out)


# a='ge#42^9jf5(%'
# #o/p='gejf4295#^(%'
# alpha,num,spcl='','',''
# for i in a:
#     if 'a'<=i<='z' or 'A'<=i<='Z':
#         alpha+=1
#     elif '0'<=i<='9':
#         num+=1
#     else:
#         spcl+=1
# print(alpha+num+spcl)


# d=[10,0,'hii','',0j,[1,2],{},0.0]
# #o/p=[0,'',0j,{}]
# out=[]
# for i in d:
#     if bool(i)==False:
#         out=out+[i]
# print(out)


#wap to delete duplicate values from the list without using typecasting and builtin
# l=[1,2,3,1,4,5,4,6,6]
# #o/p=[1,2,3,4,5,6]
# out=[]
# for i in l:
#     if i not in out:
#         out=out+[i]
# print(out)


# s='hai'
# #o/p='hhaaii'
# out=''
# for i in s:
#     if 'a'<=i<='z':
#         out=out+i
#     if 'a'<=i<='z':
#         out=out+i
# print(out)

# s='hai'
# res=''
# for i in s:
#     if 'a'<=i<='z':
#         res=res+ i*2
# print(res)






