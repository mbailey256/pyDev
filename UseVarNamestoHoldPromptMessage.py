
# can you use varname for prompt?


fname = 'First Name'
lname = 'Last Name'
#fname = raw_input(prompt) % 'First Name'

def getvars(vars):
    prompt = '%s > ' % vars
    var = raw_input(prompt)
    return var

fname = getvars(fname)
lname = getvars(lname)

print '%s %s' % (fname,lname)
