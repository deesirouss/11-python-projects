import random
class Rupees:
  
  def __init__(self, rare = False): #constructor
    
    self.rare = rare
    if self.rare:
      self.value = 1.6
    else:
      self.value = 1.00
  
  def __del__(self):
      print("Coin Spent")
  
  def rust(self):
    self.colour = "greenish"
  
  def clean(self):
    self.colour = "Gold"
  
  def flip(self):
    heads_options = [True, False]
    choice = random.choice(heads_options)
    self.heads = choice
  
    self.colour = "Gold"
    self.num_edges = 1
    self.diameter = 22.5 # mm
    self.thickness = 3.15 # mm
    self.heads = True

coin1 = Rupees()
coin2 = Rupees(rare = True)
print(coin1.value)
del coin1
print(coin2.rare)
print(coin2.value)
print(coin1.value)