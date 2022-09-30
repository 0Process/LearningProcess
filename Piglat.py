#English to pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

#The above lines of code ask the user to enter English text to translate to Pig Latin. We also create a constant that hold every lowecase
#vowel letter (and y) as a tuple of strings to be used later in the program.

#Next, we create the pigLatin variable to store the words as we translate them into pigLatin
piglatin = [] # A list of the words in Pig Latin
for word in message.split():
    #Seperate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetter += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
#We need each word to be its own string so we call message.split() to get a list of words as seperate strings
#The string "I am Nick." would cause split to return ['I', 'am', 'Nick.']

#We need to remove any non-letters from the start and end of each word so that a string like 'Nick' returns 'Nickyay' instead of 'Nick.yay
#We'll save these non-letters to a variable named prefixNonLetters.
    
    #Seperate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

#a loop that calls isalpha() on the first character in the word will determine if we should remove a character from a word and
#concatenate it to the end of prefixNonLetters. If the entire word is made of non-letter characters, like '4000', we can simply
#append it to the pigLatin list and continue to the next word to translate. We also need to save the non-letters at the end of the
#word string. THis code is similar to the previous loop

#Next, we make sure the program remembers if the word was in uppercase or titlecase so we can restore it after translating to piglatin

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() #Make the word lowercase for translation.

#for the rest of the code in the for loop we'll work on a lowercase version of word
#To convert a word like "sweigart" to "eigart-sway" we need to remove all the consonants from the beginning of word:

    # Seperate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

#We use a loop similar to the loop that removed non-letters from the start of word, except now we are pulling off consonants and storing them
#in a variable named prefixConsonants. If there were any consonants at the start of the word they are now in prefixConsonants and
#we should concatenate that variable and the string 'ay' to the end of word. Otherwise, we can assume word begins with a vowel and we
#only need to concatenate 'yay':
    
    #Add the pig Latin ending to the word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
#Recall that we set word to its lowercase version with word = word.lower(). If word was originally in uppercase or title case, this
#code will convert word back to its original case
    #Set the word back to uppercase or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

#At the end of the for loop, we append the word, along with any non-letter prefix or suffix it originally had, to the pigLatin list
    #Add the non letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

#Join all the words back together into a single string
print(' '.join(pigLatin))

#After the loop finishes we combine the list of strings into a single string by calling the join() method. This single string is passed to
#print() to display our Pig Latin on the screen. 