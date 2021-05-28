your_name = "Jamie"

# Lines 4-5 are a function called 'say_hello'
def say_hello(name):
  print("Hey there, {}".format(name))
  
# Now we can call the function and substitute any variable as the 'name' parameter!
say_hello(your_name)
say_hello("Sam")


def multiply_two_numbers(x, y):
  print(x*y)
  
multiply_two_numbers(10,5)
