import re

#creating a regex pattern that matches a phone number string
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#now PhoneNumRegex variable contains a Regex object

#a regex's search() method searches the string for matches to the regex
#here we use mo to signify matching objects
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: '+ mo.group())

#this method is much shorter than the isPhoneNumber.py program
#adding paratheses to the regex will create groups
#then you can use group() to grab each set of parentheses 
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)
mo.group(2)
mo.group(0)
mo.group()
mo.groups()
#you can assign string values to the groups here:
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)
#you can use the \ key to include the raw string passed to re.compile function like parantheses \(
#.  ^  $  *  +  ?  {  }  [  ]  \  |  (  ) all have special meanings that you need to backslash to pass to compile

#the | character is called a pipe, you can use it to match one of many expressions
#r'Batman|Tina Fey' will match either batman or tina fey
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()
print(mo2.group())

#you can also use the pipe to match one of several patterns as a part of your regex
#for example:
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
print(mo.group())
mo.group(1)
print(mo.group(1))


#using the earlier phone number example, you can make a regex to look for numbers that don't have an area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()
print(mo2.group())

#you can think of the ? as saying "match zero or one of the group preceding this question mark"
#the * means "match zero or more" the group that precedes the star can occur any number of times in the text
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
print(mo1.group)

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
print(mo3.group())

#WHile star means match zero or more, the + symbol means match one or more.
#this means the group preceding a plus must appear at least once
batRegex = re.compiler(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

#The regex bat(wo)+man will not match the string 'The Adventures of Batman' because at least one wo is required by the plus sign
#If you have a group that you want to repeat a specific number of times follow the group in your regex with a number in braces.
#for example the regex (Ha){3} will match 'HaHaHa' but not "HaHa" since the latter has only 2 repeats
#You can specify a range by writing a minumum, a comma and a maximum between the braces
#For example, the regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', 'HaHaHaHaHa'
#You can leave out the left or right number to leave minumum or maximum unbounded
#For example (Ha){3,} or (Ha){,5}
#Braces serve to shorten similar expressions like so:
(Ha){3}
(Ha)(Ha)(Ha)

(Ha){3,5}
((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

mo2 = haRegex.search('Ha')
mo2 == None

#Python's regular expressiosn are greedy by default in ambiguous situations they will match the longest string possible
#the non-greedy version of braces matches the shortest string possible
#this has the closing brace followed by a question mark
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

#In addition to the search() method, Regex objects also have the findall() method
#findall() will return the strings of every match in a searched string
#search() returns a match object of the first matched text in searched string
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()

#findall() will return a list of strings, as long as there are no groups in the regular expression
#each string in the list is a piece of the searched text that matched the regular expression
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#If there are groups in the regular expression, then findall() will return a list of tuples
#Each tuple represents a found match and its items are the matched strings for each group into the regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#Earlier you learned \d is shorthand for the regular expression (0|1|2|3|4|5|6|7|8|9)
#\d can stand for any digit. there are many shorthand character classes
#\D = any character that is a not a numeric digit from 0-9
#\w Any letter, numeric digit or underscore character
#\W Any character that is not a letter, numeric digit, or underscore character
#\s any space, tab, or newline character
#\S Any character that is not a space, tab, or newline
#The character class [0-5] will match only numbers 0 to 5
#There is no shorthand character class that matches only letters
#You can use [a-zA-Z]
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers. 10 lords, 9 ladies, 8 maids, 7 swans. 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

#the regular expression \d+\s\w+ will match text that has one or more numeric digits (\d+)
#followed by a whitespace character (\s), followed by one or more letter/digit/underscore characters (\w+)
#findall() returns all matching strings of the regex pattern
#You can define your own character class using square brackets. [aeiouAEIOU] will match any vowel
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')

#You can include ranges of letters and numbers using a hyphen
#Inside the square brackets, the normal regular expression symbols are not interpreted as such
#by using the ^ character just after the character class's opening bracket
#you can make a negative character class that will match all the characters that are not in the character class
consonantRegex = re.compile(r'[aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

#You can also use the ^ symbol at the start of a regex to indicate that a match must occur at the beginning of the searched text 
#You can use a $ at the end of the regex to indicate the string must end with this regex
#You can use the ^ and $ together to indicate the entire string must match the regex.
#Meaning its not enough for a match to be made on some subset of the string
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
beginsWithHello.search('He said hello.') == None
#the r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('Your number is forty two.') == None
#the r'^\d+$' regular expression string matches strings that both begin and end with one ore more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.search('12345xyz67890') == None
wholeStringIsNum.search('12 34567890') == None
#the . character in a regular expression is called a wildcard and will match any character excpet a newline
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat')
#Matching everything with Dot-Star: .* stands in for that everything
#Remember that dot means any single character except newline
#* means zero or more of the preceding character
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
mo.group(2)
#to match any and all text in a non-greedy fashion, use (.*?)
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

#The .* will match everything except a newline
#by using re.DOTALL you can make the dot character match all characters including the newline
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust. \nProtect the innocent.\nUphold the law.').group()

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust. \nProtect the innocent.\nUphold the law.').group()

#regular expressions match text with other exact casing you specify. 
#the following match completely different strings
regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 =re.compile('rob0cop')
regex4 = re.compile('Roboc0p')
#if you want to make your regex case insensitive, you use re.IGNORECASE or re.I
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()

robocop.search('ROBOCOP protects the innocent.').group()

robocop.search('Al, why does your programming book talk about robocop so much?').group()

#The sub method passes two arguments. First argument is a string to replace any matches, the second is the string for the regular expression
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob.')

#Sometimes ou need to use matched text itself as part of substitution.
#In the first argument to sub(), you can type \1, \2, \3, to mean "enter the text of group 1, 2, 3," and so on 
#Lets say you want to censor their names, besides the first letter
#You can use Regex agent (\w)\w* and pass r'\1****' as the first argument to sub()
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

