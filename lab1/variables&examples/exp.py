#Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Variables
#1
x = 5
y = "John"
print(x)
print(y)

#2
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#3
x = 5
y = "John"
print(type(x))
print(type(y))

#4
x = "John"
# is the same as
x = 'John'

#5
a = 4
A = "Sally"
#A will not overwrite a


#global
#1
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()
#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


myfunc()

print("Python is " + x)
#4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#multiple-values
#1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#2
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output
#1
x = "Python is awesome"
print(x)
#2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#4
x = 5
y = 10
print(x + y)
#5
x = 5
y = "John"
print(x + y)
#6
x = 5
y = "John"
print(x, y)