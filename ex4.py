
# setting variable cars
cars = 100
# setting variable seats in car
space_in_a_car = 4.0
# number of drivers
drivers = 30
# number of passengars
passengers = 90
# spare cars
cars_not_driven = cars - drivers
# cars with drivers
cars_driven = drivers
# capacity
carpool_capacity = cars_driven * space_in_a_car
# stats on carpool_capacity
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport ", carpool_capacity, "people today."
print "We have ", passengers, "to carpool today."
print "We need to put about ", average_passengers_per_car, "in each car."
