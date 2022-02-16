films = {
  "Finding Dory": [3,5],
  "Bourne": [18,5],
  "Tarzan": [15,5],
  "Ghost Busters": [12,5]
}

while True:
  choice = input("Which film do you want to watch?: ").strip().title()
  
  if choice in films:
    age = int(input("How old are you ?: ").strip())
    
    # check user's age
    if age >= films[choice][0]:
      
      # check enough tickets
      if films[choice][1] > 0:
        print(f"Enjoy the film {choice}")
        films[choice][1] = films[choice][1] - 1
        
      else:
        print(f"No ticket left for film {choice}")  
      
    else:
      print("You are too young to watch this film !")
         
  else:
    print("Sorry, We don't have that film")