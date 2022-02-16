# Ask user for name
name = input("What is your name?: ")

# Ask user for age
age = input("How old are you?: ")

# Ask user for city
city = input("What city do you live in?: ")

# Ask user what they enjoy
love = input("What do you love doing?: ")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name, age, city, love)

# Print output to screen
print(output)

# optional practice
a = "part one"
b = "part two"
c = a + b
d = c * 3
A = "part"
B = 1
C = A + str(B)
"{}-{}".format(A,B)
D = "{1}-{0}".format(A,B)
#print(D)

# extra exercise string.method()
"hello".count("e")
text = "Happy Birthday"
text.count("a")
text.lower()
text.upper()
text1 = "happy birthday"
text1.capitalize()
text1.title()
text.islower()
text.isupper()
text.istitle()
text.isalpha()
text.isdigit()
text.isalnum()
text.index("birthday")
text.find("birthday")
text2 = "0000happy birthday0000"
text2.strip("0") # lstrip & rstrip
text2.strip()
len(text)

# slice variable[start:end:step]
text[2]
text[-2]
text[0:5:1]
text[:5]
text[5:9:1]
text[5:]
text[5::2]
text[:7]
text[::-1]

# Automated Slices
text[text.index("appy"):text.index("day")]
text[text.index("appy"):]