
# test my answer to result

print '1  True \t', True and True
print '2  False \t', False and True
print '3  False \t',1 == 1 and 2 == 1
print '4  True \t', "test" == "test"
print '5  True \t', 1 == 1 or 2 != 1
print '6  True \t', True and 1 == 1
print '7  False \t', False and 0 != 0
print '8  True \t', True or 1 == 1
print '9  False \t', "test" == "testing"
print '10 False \t', 1 != 0 and 2 == 1
print '11 True \t',   "test" != "testing"
print '12 False \t', "test" == 1
print '13 True \t', not (True and False)
print '14 False \t', not (1 == 1 and 0 != 1)
print '15 False \t', not (10 == 1 or 1000 == 1000)
print '16 False \t', not (1 != 10 or 3 == 4)
print '17 True \t', not ("testing" == "testing" and "Zed" == "Cool Guy")
print '18 True \t', 1 == 1 and (not ("testing" == 1 or 1 == 0))
print '19 False \t', "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print '20 False \t', 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
