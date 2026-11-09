# SpongeBob dumbtext formatter

# prompt user for phrase
print("Enter a phrase you'd like to make dumb: ")
phrase = input()

# create an empty list to hold characters of phrase string
phraseList = []

# this variable alternates between 0 and 1 to tell program to use upper or lower
upDown = 0

# create a list from the phrase with alternating lower/upper chars

for i in phrase:
    if upDown == 0:
        phraseList.append(i.lower())
        upDown = 1
    elif upDown:
        phraseList.append(i.upper())
        upDown = 0

# make the list of converted chars back into a string

dumbPhrase = ''.join(phraseList) # use '' to indicate no spaces between items

print(dumbPhrase)



