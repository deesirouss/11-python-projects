# get sentence from user
original = input("Please Enter a Sentence: ").strip().lower()

# split sentence into words
words = original.split()

# loop through words and convert to pig latin
new_words = []

# if starts with vowel, just add "yay"
for word in words:
  if word[0] in "aeiou":
    new_word = word + "yay"
    new_words.append(new_word)
  
  #Otherwise move the first constant cluster to end and add "ay"
  else:
    vowel_pos = 0
    for letter in word:
      if letter not in "aeiou":
        vowel_pos = vowel_pos + 1
      else:
        break # not continue
    cons = word[:vowel_pos]
    new_word = word[vowel_pos:] + cons + "ay"
    new_words.append(new_word)

# stick words back together
output = " ".join(new_words).capitalize()

#output the sentence
print(output)