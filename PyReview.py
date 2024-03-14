# Had to change filenames in .replit to run this - will change back to main.py when I start on the API itself and this will just be for reference

def multiply(*args):  #undefined number of arguments become a tuple
                      #use ** to pack/unpack dictionary keyword=value args
  print(args)
  total = 1
  for arg in args:
    total *= arg

  return total

print(multiply(10,3,5))

name_list = ["Alice", "Bob", "Julie", "Jenny", "Jessica"]  #can add/remove elements
name_tuple = ("Alice", "Bob", "Julie") #can't add/remove elements
name_set = {"Alice", "Bob", "Julie"}   #can add/remove but no duplicates, doesn't keep order, can't use the subscript notation
name_dict = {"Alice": "A", "Bob": "B", "Julie": "J"}  #key:value pairs, can add/remove elements, can't have duplicates, can use the subscript notation
# comparison operators != == < > <= >= is (items are the same) in (a key exists in a dictionary)

jnames = []
lc_jnames = [name for name in name_list if name.startswith("J")]  #Transmute list using list comprehension!
for name in name_list:  #traditional method of transmuting a list
  if name.startswith("J"):
    jnames.append(name)

print(jnames)
print(lc_jnames)

print(name_list[2])
print(name_tuple[2])

variable = input(f"What is your name? ")

if variable == "Julie" : 
  print(variable)
elif variable == "Matt" :
  print(variable)
else :
  print("You are not Julie")
  

# Dictionary comprehensions

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

# This makes the list of users into a dictionary with the name as the key and the full tuple as the value
username_mapping = {user[1]: user for user in users}
print(username_mapping)