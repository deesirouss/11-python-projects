number = 1

while number <= 10:
  # for even number
  if number % 2 == 0: #for odd !=
    print(number)
  number = number + 1
  
#==========================

# L = []
# #print(len(L))
# while len(L) < 3:
#   new_name = input("Please add your name: ").strip().capitalize()
#   L.append(new_name)

# print("List is full")
# print(L)

#===============================

for number in range(1,11):
  print(number)

for number in range(1,11,2):
  print(number)

for list1 in [1,2,3]:
  print(list1)
  
for letter in "abcd":
  print(letter)

#===========================

vowels = 0 
consonants = 0

for letter in "Hello World":
  if letter.lower() in "aeiou":
    vowels = vowels + 1
  elif letter == " ":
    pass
  else:
    consonants = consonants +1
print(f"There are {vowels} number of vowels") 
print(f"There are {consonants} number of consonants") 

#=================================================

students = {
  "male":["Tom", "Charlie", "Harry", "Frank"],
  "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
}
for key in students.keys():
  print(key)
  print(students[key])
  for name in students[key]:
    if "a" in name:
      print(name)
      
#================================

#list comprehensives
even_numbers = [x for x in range(50,101) if x % 2 == 0]
odd_numbers = [x for x in range(50,101) if x % 2 != 0]
print(even_numbers, odd_numbers)

words = ["the", "quick", "brown", "fox"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)