#python HOME;Intro;get started:
print("Hello, World!")


#python SYNTAX:
if 5 > 2:
  print("Five is greater than two!")
  
#number2 example:
x = 5
y = "Hello, World!"

print(x)
print(y)  


#python Coments:

#print("Hello, World!")
print("Cheers, Mate!") #this is coment.


#python variables:
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#number2 example 
x = str(3)  # x will be '3'
y = int(3)   # y will be 3
z = float(3)   # z will be 3.0

print(x)
print(y)
print(z)

#quotes 
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

#VARIABLE NAMES:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar) 
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)#same answear 

#incorrect names:
#2myvar = "John"
#my-var = "John"
#my var = "John" 


#Many Values to Multiple Variables:
x, y, z = "Orange", "Banana", "Cherry"
print(x) #output:Orange;
print(y) #output:Banana;
print(z) #output:Cherry.

x = y = z = "Orange"
print(x) 
print(y)
print(z) # all values will be orange 

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #apple
print(y) #banana
print(z)#cherry.


#Output  variables:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #output: completed sentence 
#ERROR:
x = 5
y = "John"
print(x + y)
#Correct:
x = 5
y = "John"
print(x, y)

#global variables:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() #output:Python is awesome

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)#output:Python is fantastic

#Python Data Types:
x = 1j
print(x) #lj
#display the data type of x:
print(type(x)) #<class 'complex'>
 
x = ("apple", "banana", "cherry")
print(type(x))   #<class 'tuple'>

x = range(6)
print(x) # range(0, 6)
print(type(x)) #<class 'range'>

#PYTHON NUMBERS:
x = 35e3
y = 12E4
z = -87.7e100
print(type(x)) 
print(type(y))
print(type(z))
#output: FLOAT.

#PYTHON CASTING:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
a= float(1)     # a will be 1.0
b = float(2.8)   # b will be 2.8
c = float("3")   # c will be 3.0
w = float("4.2") # w will be 4.2

#PYTHON STRING:
a = "Hello, World!"
print(a[1]) #output:e
for x in "banana":
  print(x) #output b a n a n a
a = "Hello, World!"
print(len(a))   #13 output
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#  
b = "Hello, World!"
print(b[-5:-2])   #output orl
a = "Hello, World!"
print(a.upper()) #HELLO, WORLD!
print(a.lower()) #hello, world!
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J")) #Jello, World!
print(a.split(",")) # returns ['Hello', ' World!']

age = 36
txt = f"My name is John, I am {age}"
print(txt) #output My name is John, I am 36
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)# The price is 59.00 dollars
txt = "We are the so-called \"Vikings\" from the north."
print(txt) #We are the so-called "Vikings" from the north.