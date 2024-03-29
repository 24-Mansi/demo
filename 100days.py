#string
#to access all characters in string we use indexing but formulti line string use for loop
apple = '''He said,
Hi Harry
het I am good
I wan to eat an apple'''
for character in apple:
    print(character)


#strings are immutable
a="!!Harry!! !!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))        #removes the trailing characters
print(a.replace("Harry", "John"))       #replace the existing string with new string
print(a.split(" "))          #makes the string into list

blogheading="introduction to js"
print(blogheading.capitalize())      #it turns first character of string to uppercase rest others to lowercase. No effect if the first character is already uppercase.

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))        #aligns the string to center as per the parameters.
print(a.count("Harry"))   #counts the number of occurence of data.

str1 = "Welcome to the Console!!!"
print(str1.endswith("!!!"))     #checks if string ends with a given value.If yes then return True, else False.
print(str1.endswith("to", 4, 10))        #also check for a value in-between the string by providing start and end index positions.

str1="He's name is Dan. He is an honest man"
print(str1.find("is"))            #searches for first occurence of given value and returns index where it is present.If given value is absent fron string then it will give -1.
print(str1.index("is"))

str1="WelcometotheConsole"
print(str1.isalnum())      #returns True only if the entire the string cosists of A-Z, a-z, 0-9.Else returns false for any other character or punctuations.

str1="Welcome000"
print(str1.isalpha())        #returns True only for entire strin consists A-Z, a-z. Else False.

#isupper()
#islower()
#isprintable()   returns True if all characters in string are printable.
#isspace()      returns True only and only if the string contains white spaces, else False.
#istitle()     returns True only if the first letter of each word of string is capitalized.
#startswith()
#swapcase()       uppercase into lower and vice versa.




#if else elif condition
a= int(input("Enter your age:"))
print("Your age is:", a)
if(a>18):
    print("You can drive")
    print("Yes")
else:
    print("You can not drive")


num = int(input("Enter the value of num="))
if(num<0):
    print("Number is negative.")
elif(num==0):
    print("Number is zero")
elif(num==999):
    print("Number is special")
else:
    print("Number is positive")

print("I am happy now")


#nested if condition
num= 18
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

#for loops----can iterate over a sequence of iterable objects.
name="Mansi"
for i in name:
    print(i)
    if(i=="a"):
        print("Sahil")

colors=["Red","Blue","Black"]
for color in colors:
    print(color)
    if i in color:
        print(i)
        