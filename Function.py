# *arg
def my_function(*college):
    print("Hello "+ college[0])
my_function("MLRIT", "MLRITM")

#**kwargs
def my_function(**college):
    print("Warm Welcome "+ college['c'])
my_function(a="MLRIT",c="MLRIT")

#If we call the function without argument, it uses the default value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("INDIA")
my_function()
my_function()
my_function("Brazil")

#recursion
def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
recursion(6)


#returning a value in function
def my_function(x):
  return 5 * x
print("Multiples are: ")
print(my_function(3))
print(my_function(5))
print(my_function(9))