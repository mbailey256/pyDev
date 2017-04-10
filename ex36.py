
# Raiders of the Lost Ark: Indy and the Cave

from sys import exit

traps= ['wall spikes','pit','idol room','idol']

trap = 0
next_trap = 1

whip = 'Yes'



def enter_cave(traps,trap,next_trap):

    while trap >= 0 :
        if traps[trap] == 'wall spikes':
            wall_spikes()
            print trap,next_trap
            trap = trap + next_trap
        elif traps[trap] == 'pit':
            pit()
            print trap,next_trap
            trap = trap + next_trap
        elif traps[trap] == 'idol room':
            idol_room()
            print trap,next_trap
            trap = trap + next_trap
        else:
            idol()
            next_trap = -1
            trap = trap + next_trap
            print trap,next_trap

    boulder()



def plane():
    print 'cue music'

def boulder():
    print "boulder"
    plane()

def idol():
    print "Idol"
def idol_room():
    print "Idol Room"
def pit():
    print "Pit"

    #jump
    #if whip = 'Yes'

    #whip = 'No'

def wall_spikes():
    print "Wall Spikes"
    #sunlight
    #shadow

def dead(why):
    print why
    exit(0)

#'Dead body of Forrestal'

#'Dead body of Satipo'

enter_cave(traps,trap,next_trap)
