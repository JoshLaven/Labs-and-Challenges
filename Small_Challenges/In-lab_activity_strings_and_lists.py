
'''
Optional Activity:
task: use a list to create a string or a few strings

If you don't have an idea: 
Alter the example below so that instead of 4 sentences, you only print 2:
print "I've lived in CA, NM, and MO. Now I live in IL" 
'''

#note this is how str.format() works:
my_string = "Stuff {} and more stuff {}. Other stuff {}"
#my_string.format(what goes in the first{}, on the second{}, third{}, etc)
my_string.format('that I say', 'that I want to say', 'that should not be said')

#e.g.
states = ['CA', 'NM', 'MO', 'IL']
current = 'IL'

for state in states: #we will cover for loops later
    if state is current: 
        print("Now I live in "+ state)
    else:
        print("I've lived in "+ state)

#or do the same thing a little differently
states = ['CA', 'NM', 'MO', 'IL']
current = 'IL'

for state in states:
    if state is current:
        print("Now I live in {}".format(state))
    else:
        print("I've lived in {}".format(state))

#also the same!
for i in range(len(states)):
    if states[i] is current: 
        print("Now I live in "+ states[i])
    else:
        print("I've lived in "+ states[i])

