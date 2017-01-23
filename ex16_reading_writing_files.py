# exercise 16 Reading and Writing Files

# package
from sys import argv

# arguement
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# keystroke
raw_input("?")


print "Opening the file..."
# open file for 'w'riting
target = open(filename, 'w')


print "Truncating the file.  Goodbye!"
# set size of file to near zero; NOT ACTUALLY NEEDED AS open(<filename>,'w')
# truncates the target file
# target.truncate()

print "Now I'm going to ask you for three lines."

# assign user input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to a file."

# write out file line by line using initial method
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# write out file using only one target.write

strg = "%s\n%s\n%s" % (line1,line2,line3)
target.write(strg)



print "And finally, we close it."

# close file object
target.close()
