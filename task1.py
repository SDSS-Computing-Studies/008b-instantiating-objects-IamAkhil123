#!python3

class veterinarian:1. 

def __init__(self):
   self.animal = input("What is your animal")
   self.breed = input("What breed is your animal")
   self.name = input("What is your animals name")
   self.owner = int(input("What is the owners name?:"))
   self.birthdate = int(input("What is your pets birthdate"))
 
def display(self):  
   output = str(self.name) + " " + self.breed + " " + self.owner
   outputLength = len(output) 
   print( outputLength * "=")
   print( output)
   print( outputLength * "=")

def newpet():
   animal = input("What is your animal")
   breed = input("What breed is your animal")
   name = int(input("What is your animals name"))
   owner = int( input("What is the owners name?:"))
   birthdate = int(input("What is your pets birthdate"))

def exit():
     exit()

def retrieve():
      u = input("Which pet?")



x = input("1. Enter a new pet""\n""2. Retrieve a pet""\n""3. Exit")
if x == 1:
  newpet()
if x == 2:
  retrieve()
if x == 3:
  exit()

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""