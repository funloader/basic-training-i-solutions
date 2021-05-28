import random

def generate_random_list(number_of_items):
  random_items = []
  for i in range(number_of_items):
    random_items.append(random.randint(0,100))
  return random_items


for i in range(10):
  random_list = generate_random_list(i)
  print(random_list)
  
