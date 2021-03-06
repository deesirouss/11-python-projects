import random

class Coin:
  def __init__(self, rare = False, clean = True, heads = True, **kwargs):
    
    for key,value in kwargs.items():
      setattr(self,key,value)
      
    self.is_rare = rare
    self.is_clean = clean
    self.heads = heads
    
    if self.is_rare:
      self.value = self.original_value * 1.25
    else:
      self.value = self.original_value
    
    if self.is_clean:
      self.colour = self.clean_colour
    else:
      self.colour = self.rusty_colour
      
  def rust(self):
    self.colour = self.rusty_colour 

  def clean(self):
    self.colour = self.clean_colour
    
  def flip(self):
    heads_options = [True, False]
    choice = random.choice(heads_options)
    self.heads = choice
    
  def __del__(self):
    print("Coin Spent")
  
  def __str__(self): # print the class value
    if self.original_value >= 1:
        return "Dollar {} Coin".format(int(self.original_value))
    else:
        return "{}p Coin".format(int(self.original_value * 100))
       
class Dollor1(Coin):
  
  def __init__(self): #constructor
    
    data = {
      "original_value": 1.00,
      "clean_colour": "gold",
      "rusty_colour": "greenish",
      "num_edges": 1,
      "diameter": 22.5, # mm
      "thickness": 3.15, # mm
      "mass": 9.5 # pound  
    }
    super().__init__(**data)
    
class Dollor2(Coin):
  
  def __init__(self): #constructor
    
    data = {
      "original_value": 2.00,
      "clean_colour": "bronze", # just for example
      "rusty_colour": "brown",
      "num_edges": 1,
      "diameter": 25.5, # mm
      "thickness": 2.15, # mm
      "mass": 11.5 # pound  
    }
    super().__init__(**data)

class Dollor10(Coin):
  
  def __init__(self): #constructor
    
    data = {
      "original_value": 10.00,
      "clean_colour": "silver", # just for example
      "rusty_colour": None,
      "num_edges": 1,
      "diameter": 25.5, # mm
      "thickness": 4.15, # mm
      "mass": 15.5 # gram  
    }
    super().__init__(**data) 
    
  def rust(self): # polymorphisim
    self.colour = self.clean_colour  
    
  def clean(self): # polymorphisim
    self.colour = self.clean_colour
     
coins = [Dollor1(), Dollor2(), Dollor10()]

for coin in coins:
  arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                          coin.num_edges, coin.mass]

  string = "{} - Colour: {}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
  print(string)