
# exercise 16 Study Drill request

# package
from sys import argv

# filename
script, filename = argv

# assign file object to variable
txt = open(filename)

# read and print contents
print txt.read()

# close file object 
txt.close()
