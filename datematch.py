
import dateideas
ideas = dateideas.ideaslist()
updatedideas =  {}
print('Welcome to datematch! We will match the perfect date idea for you:')
print()
print('Type "out" for going out, "in" for staying in, or "either" if you have no preference')
print()
firstQ = input('Do you want to go out for your date or stay in?  ')
print()
if firstQ == 'out':
    for idea in ideas.keys():
        if "outside" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif firstQ == "in":
    for idea in ideas.keys():
        if "inside" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif firstQ == "either":
    updatedideas = ideas
else:
    print('Invalid input. Please reload datematch and try again!')
    exit()

ideas = updatedideas
if len(ideas.keys()) == 0:
    print('No possible dates found :(')
    exit()

updatedideas = {}

print('Great! Compiling suitable date ideas . . .:')
print()
print('Type "y" for yes, "n" for no, or "either" if you have no preference')
print()
secondQ = input('Is you or your date hungry?  ')
print()
if secondQ == "y":
    for idea in ideas.keys():
        if "hungry" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif secondQ == "n":
    for idea in ideas.keys():
        if "full" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif secondQ == "either":
    updatedideas = ideas
else:
    print('Invalid input. Please reload datematch and try again!')
    exit()

ideas = updatedideas


if len(ideas.keys()) == 0:
    print('No possible dates found :(')
    exit()

updatedideas = {}

print('Great! Compiling suitable date ideas . . .:')
print()
print('Type "q" for quick (< 2 hours), "l" for long (> 2 hours), or "either" if you have no preference')
print()
thirdQ = input('How much time do you have for your date (< or > 2 hours)?  ')
print()
if thirdQ == "q":
    for idea in ideas.keys():
        if "quick" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif thirdQ == "l":
    for idea in ideas.keys():
        if "long" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif thirdQ == "either":
    updatedideas = ideas
else:
    print('Invalid input. Please reload datematch and try again!')
    exit()

ideas = updatedideas

if len(ideas.keys()) == 0:
    print('No possible dates found :(')
    exit()

updatedideas = {}

print('Great! Compiling suitable date ideas . . .:')
print()
print('Type "a" for active (contains some level of physical activity), "s" for still (no physical activity or movement), or "either" if you have no preference')
print()
fourthQ = input('Do you want a date with some level of physical activity or without any movement?  ')
print()
if fourthQ == "a":
    for idea in ideas.keys():
        if "active" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif fourthQ == "s":
    for idea in ideas.keys():
        if "still" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif fourthQ == "either":
    updatedideas = ideas
else:
    print('Invalid input. Please reload datematch and try again!')
    exit()

ideas = updatedideas

if len(ideas.keys()) == 0:
    print('No possible dates found :(')
    exit()

updatedideas = {}

print('Great! Compiling suitable date ideas . . .:')
print()
print('Type "under" for a budget under $50, "over" for splurging over $50, or "either" if you have no preference')
print()
fifthQ = input('Whats the budget for your date (< or > $50)?  ')
print()
if fifthQ == "under":
    for idea in ideas.keys():
        if "under50" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif fifthQ == "over":
    for idea in ideas.keys():
        if "over50" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif fifthQ == "either":
    updatedideas = ideas
else:
    print('Invalid input. Please reload datematch and try again!')
    exit()

ideas = updatedideas


if len(ideas.keys()) == 0:
    print('No possible dates found :(')
    exit()

updatedideas = {}

print('Great! Compiling suitable date ideas . . .:')
print()
print('Type "first" if this is a first date, "dating" if this not a first/early-stage date, or "either" if you have no preference')
print()
sixthQ = input('Is this a first/early-stage date or are you already dating?  ')
print()
if sixthQ == "first":
    for idea in ideas.keys():
        if "firstdate" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif sixthQ == "dating":
    for idea in ideas.keys():
        if "dating" in ideas[idea]:
            updatedideas[idea] = ideas[idea]
elif sixthQ == "either":
    updatedideas = ideas
else:
    print('Invalid input. Please reload datematch and try again!')
    exit()

ideas = updatedideas

if len(ideas.keys()) == 0:
    print('No possible dates found :(')
    exit()

print('Great! Finding all suitable date ideas now:')
print()


print('Here is a list of compatible date ideas:')
print()
for date in ideas.keys():
    print(date)