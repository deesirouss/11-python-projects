known_users = ['Bibek', 'Mahesh', 'Amit', 'Sparsha']
#print(len(known_users))
# 'bibek' in known_users

while True:
  print("Hi! my name is Travis")
  name = input("What is your name?: ").strip().capitalize()
  
  if name in known_users:
    print(f"""Hello {name} :) !""")
    
    remove = input("Do you like to removed from this system? (y/n)").lower()
    if remove == "y":
      known_users.remove(name) # one time only i.e one name
    elif remove == 'n':
      print("No Problem, I didn't want to leave anyway !")
      # examples
      # del known_users[0]
      # del known_users[0:2]
      
      
  else:
    print(f"Hmmm ! I don't think I have meet you yet {name}")
    add_me = input("Would you like to be added in this system ? (y/n): ").strip().lower()
    if add_me == 'y':
      print(known_users)
      known_users.append(name)
    elif add_me == 'n':
      print("No Worries, See you arround !")