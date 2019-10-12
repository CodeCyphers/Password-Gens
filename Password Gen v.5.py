 #Importing the random module and the string module, used for the actual randomization
import random
import string

# Defines the function for all ascii random and allows an argument to be passed to it
def random_ascii(stringLength=1000):

  #Specifies characters that will be randomized in the string
  characters = string.ascii_letters + string.digits + '&*-#$!^_=+@~'

  #Stores the randomized string in a variable to be saved to a txt file.
  final = ''.join(random.choice(characters) for i in range (stringLength))

  #prints the random string to the screen
  print(final)

  #Creates the txt file if not already created
  f = open('random_pw.txt', 'w')

  #Writes the randomly generated string to the txt file (will overwrite any prior data)
  f.write(final)

  #Closes the instance of the txt file
  f.close()

#Asks the user how many chars to include
how_many = int(input("How many characters?: "))

#Takes the users inputted amount and starts the function with the argument how_many
random_ascii(how_many)