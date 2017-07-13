
# Raiders of the Lost Ark: Indy and the Cave

from sys import exit

traps= ['wall spikes','pit','idol room','idol']

trap = 0
next_trap = 1

def enter_cave(traps,trap,next_trap):

    while trap >= 0 :
        if traps[trap] == 'wall spikes':
            wall_spikes()
            #print trap,next_trap
            trap = trap + next_trap
            #dead("Ouch! Wall spikes!")

        elif traps[trap] == 'pit':
            #print trap,next_trap
            if next_trap > 0:
                whip = 'Yes'
            else:
                whip = 'No'

            pit(whip)

            trap = trap + next_trap

        elif traps[trap] == 'idol room':

            idol_room()

            trap = trap + next_trap

        else:
            idol()
            next_trap = -1
            trap = trap + next_trap
            print trap,next_trap
            #dead("You should have ran.")
    boulder()

def action(action_msg,hint,fail):
    print action_msg
    choice = raw_input("> ")
    if choice == hint:
        print "Good job"
    else:
        msg = '\n %s  Why didn\'t you %s' % (fail,hint)
        dead(msg)

def plane():
    print 'cue music'

def boulder():
    print "boulder"
    dead("Tripped, you died.")
    plane()

def idol():
    print "Idol"

def idol_room():

    if next_trap > 0:
        msg = """You enter the idol room! \n
Beware of the darts in the walls!"""
    else:
        msg = """Beware of the darts in the walls!"""

    if next_trap > 0:
        hint = "walk on the smooth stones!"
        fail = 'You\'ve been shot by a poison dart!'
    elif next_trap < 0:
        hint = "Run!"
        fail = 'You\'ve been shot by a poison dart!'

    action(msg,hint,fail)


def pit(whip):
    msg = """You come to a bottomless pit"""

    if whip == 'Yes':
        hint = 'use the whip to swing over!'
        fail = 'You fell to your death! '
    else:
        hint = 'jump across!'
        fail = 'You fell to your death! '

    action(msg,hint,fail)
    if whip == 'Yes':
        print "Btw leave the whip."

def wall_spikes():
    msg = """You enter a dark narrow passage
with a beam of light. What should you do? """
    hint = 'stay in the shadows!'
    fail = 'Ouch! Wall spikes!'
    action(msg,hint,fail)

def dead(why):
    print why
    exit(0)

#'Dead body of Forrestal'

#'Dead body of Satipo'

enter_cave(traps,trap,next_trap)
