
# exercise 5

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s. " % name
print "He's %d inches or %d centimenters tall." % (height, height * 2.54)

print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usaully %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d i get %F." % ( \
    age, height, weight, round(age + height + weight,2))
