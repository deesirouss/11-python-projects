from re import A


def add(x,y):
  return x+y #there is difference btn print & return
  
z = add(5,10)
print(z)

#=============

def rev(text):
  return text[::-1]
reverse = rev("Hello")
print(reverse)
reverse_list = rev([1,2,3])
print(reverse_list)
reverse_tuple= rev((1,2,3))
print(reverse_tuple)

#=============
# global and local
# fuction create local scope whereas loops and if statement don't
a = 100 # global scope
def f1():
  b = 10 + a # using global value
  print(b)

def f2():
  a = 2 # local scope
  print(a) 

f1()
f2()
print(a)

#=========================
# modifying global value a
def f3():
  global a
  a = 2 # modified global value of a
  print(a)
def f4():
  a = 20 # local scope
  print(a)

f3()
f4()
print(a)

# for list and dictionaries without specifying global we can chage the value through indexing and key

# keyword arguments
def about(name, age, likes = "footbal"):
  return (f"Meet {name}! He is {age} years old and like {likes}")

print(about(name = "Bibek", likes = "Python", age = 23)) # keyword arguments

dictonary = {"name": "Bibek", "age": 23, "likes": "game"}
print(about(**dictonary)) # unpacking dictonary which has key value pairs called **kwargs
print(about(age = 23,name = "Bibek"))

# *args 
# we use *args when we don't know how many arguments we are operationg on
def sum(*numbers):
  total = 0
  for number in numbers:
    total = total + number
  return total

print(sum(1,2,3,4,4))

def foo(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} is key & {value} is its value")

foo(name="bibek", likes="python")