import random
import math

health = 50
difficulty = 1 # could be 1-easy, 2-medium, 3-difficult
potion_health = int(random.randint(25,50) / difficulty)
health = health + potion_health
print(health)

# extra Practices
round(1.5)
math.floor(1.5)
math.ceil(2.1)
math.pi
math.e
math.floor(math.sin(math.pi))
math.asin(0)
math.hypot(3,4)
math.pow(2,3)
2 ** 3
math.exp(2)
math.log(math.e)
math.log10(1000)
math.log2(8)