#1
print("Hello")
print('Hello')
#2
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#3
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#4
b = "Hello, World!"
print(b[2:5])
#5
b = "Hello, World!"
print(b[:5])
#6
b = "Hello, World!"
print(b[2:])
#7
b = "Hello, World!"
print(b[-5:-2])

#8
a = "Hello, World!"
print(a.upper())
#9
a = "Hello, World!"
print(a.lower())
#10
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#11
a = "Hello"
b = "World"
c = a + b
print(c)
#12
a = "Hello"
b = "World"
c = a + b
print(c)

#13
age = 36
txt = "My name is John, I am " + age
print(txt)
#14
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#15
txt = "We are the so-called \"Vikings\" from the north."
print(txt)