
# exercise 15 Reading Files

# load argv from sys package
from sys import argv

# capture filename passed by user
script, filename = argv

# use open function to assign FILE OBJECT for the file to a variable
txt = open(filename)

# print filename and contents
print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
# capture filename during execution within an program
file_again = raw_input("> ")

# assign FILE OBJECT for the file to a new variable
txt_again = open(file_again)

# printer contents of variable using the read() method
print txt_again.read()
txt_again.close()
