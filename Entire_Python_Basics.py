# Commenting in Python uses # for a single line, as you can see.
"""
And now you can see that
using 3 apostrophes/half-single-quotes(??) creates a multi line comment.
"""

# importing 'Modules'
import random

# printing something like 'Hello there'
print("Hello there")  # in Python '' and "" are exactly the same.

# variables are used to store values:
name = "Jean-Yves"  # a variable has to start with a letter but after that you can have numbers and/or underscores _
print(name)

# The 5 actual Data Types in Python include:
'''
    Numbers
    Strings
    Lists
    Tuples
    Dictionaries
'''
# The 7 arithmetic operators in Python include:
'''
    + : which adds numbers and joins strings
    - : Subtracts
    / : divides
    * : multiplies
    % : modulus - which returns the remainder of two numbers divided
    **: returns exponential calculations (to the power)
    //: floor division (discards remainder and rounds down regardless of decimal being over 5)
    
'''
# for example
print("The 7 arithmetic operators")
print("9 + 4 =", 9 + 4)  # a comma ',' is used to separate/concatenate the string we wrote to explain what's going on and the answer.
print("9 - 4 =", 9 - 4)
print("9 / 4 =", 9 / 4)
print("9 * 4 =", 9 * 4)
print("9 % 4 =", 9 % 4)
print("9 ** 4 =", 9 ** 4)
print("9 // 4 =", 9 // 4)

# in python or any other language really, BEDMAS is important. It will always determine the order of operation
'''
    BEDMAS is an acronym to help remember an order of operations in algebra basics. 
    When you have math problems that require the use of different operations 
    (multiplication, division, exponents, brackets, subtraction, addition) order is necessary 
    and mathematicians have agreed on the BEDMAS/PEDMAS order.
    
    B - Brackets
    E - Exponents
    D - Division
    M - Multiplication
    A - Addition
    S - Subtraction
'''
print("The importance of BEDMAS in programming")
print("9 + 4 / 2 * 7 =", 9 + 4 / 2 * 7)
print("(9 + 4) / 2 * 7 =", (9 + 4) / 2 * 7)

# singles quotes and double quotes have the same effect, but what if you want to put a quote inside a string?
quote = "\"It's not about how many times you get knocked down, it's about getting back up one more time!\""
print(quote, "\n A backslash \\ or the escape character is all you need to tell the program that the next character can just be printed as is.")
# as seen above, the ' \n ' creates a new line when you print text!

multi_line_quote = '''Always remember that you're 
unique, just like everyone else!'''  # notice how you typically name a variable with multiple words in Python.

print("\n")

# adding two strings
print("The following quote makes no sense but here you go:")
print(quote + multi_line_quote)

print("\n")
# print formatting in Python @7.28min
print("formatting strings using %s:")
print("%s %s %s" % ("My favourite quotes are:", quote, multi_line_quote))

# if you want to get rid of the new line that's added after each print
print("This line ", end='')  # end='' makes sure the next thing printed on the screen will be on the same line.
print("is actually made with two print statements.")

print("\n")
# if we want to print something x number of times
print("Printing something x amount of times.. here where x = 5")
print("\n" * 5)
print(multi_line_quote * 5)

print("\n")
print("----------------------------LISTS--------------------------------")
'''
    Lists allow you to create a container/list of different values that are manipulable.
    These values are accessed by their index/position in the list which by default 
    starts at 0..1..2.. and so on.
'''
# a list example:
zoo_animals = ['Lion', 'Elephant', 'Monkey', 'Tortoise', 'Bear', 'Zebra', 'Giraffe']
# printing the first item is as easy as:
print("The first animal in our list is:", zoo_animals[0])  # remember positions in list start at zero
# you can change the item in any given position
zoo_animals[0] = "Hippo"
print("You swapped a Lion in your list for a:", zoo_animals[0])
# printing multiple values in a list
print("Print animals_lists_in_list from position 0 up to but NOT including 4", zoo_animals[0:4])
# you can include any other data type in you list including other lists!!!
farm_animals = ['Dog', 'Mouse', 'Goat', 'Horse', "Rooster"]
animals_lists_in_list = [farm_animals, zoo_animals]
print("The entire animals_lists_in_list list:", animals_lists_in_list)
# what  if you wanted the 4th item in the second list? Remember that the lists in the animals_lists_in_list lists are also just containers
print("The 4th animal in the second list of the animals_lists_in_list' list of lists is:", animals_lists_in_list[1][5])
# you can add items to an already made list by using append()
farm_animals.append("Duck")
print("After appending Duck to farm_animals: ", animals_lists_in_list)
# you can add items to an already made list into a specific place/index by using insert()
zoo_animals.insert(0, "Lion")
print("After inserting Lion into zoo_animals: ", animals_lists_in_list)
# you can remove items from an already made list by using remove()
zoo_animals.remove("Bear")  # python will look for that object/value
print("After removing Bear from zoo_animals: ", animals_lists_in_list)
# you can sort the list
zoo_animals.sort()
print("Zoo Animals list after normal sorting", zoo_animals)
# you can reverse-sort the list
zoo_animals.reverse()
print("Zoo Animals list after reverse sorting", zoo_animals)
# you can delete something/value in the list using index
del zoo_animals[1]
print("Now the list with one zoo animal [1] deleted:", animals_lists_in_list)
# you can combine lists together@11.59min
animals = zoo_animals + farm_animals
print("All animals combined:", animals)
# you can get the length(number of items) of the list
print("The animals list has a whopping ", len(animals), "animals")
# you can get the highest-ASCII(alphabetically because we are working with strings) valued item in the list
print("The Max animal in the list is", max(animals))
# you can get the lowest-ASCII(alphabetically because we are working with strings) valued item in the list
print("The Min animal in the list is", min(animals))

print("\n")
print("----------------------------TUPLES--------------------------------")
'''
    Tuples are very much like lists. But unlike a list, you're not able to change
    much about it. It's a set list.
'''
# a tuple example:
colours_tuple = ('Red', 'Purple', 'Green', 'fff')
print("Tuple example:", colours_tuple)  # notice how a tuple is sorted by default
# you can create a list out of a tuple
colours_list = list(colours_tuple)
print("Colour tuple turned into List:", colours_list)
# you can turn a list into a tuple
tuple_from_list = tuple(colours_list)
print("Colour list turned back into Tuple:", tuple_from_list)
# you can get the length(amount of items) of the tuple
print("We have", len(colours_tuple), "in the tuple of Colours")
# you can get the Max(Last occurring item) in the tuple
print("The Max of your colours tuple is", max(colours_tuple))
# you can get the Min(first occurring item) in the tuple
print("The Min of your colours tuple is", min(colours_tuple))
# YOU CAN NOT FOR EXAMPLE ADD TWO TUPLES TOGETHER

print("\n")
print("----------------------------DICTIONARIES--------------------------------")
'''
    Dictionaries are also very much like lists. But unlike lists, you're not able to add two dictionaries together
    with a simple + . Dictionaries contain two parts to the data entries. The first, called a 'Key' is a unique
    identifier for its pairing value. The second, like I just mentioned is the 'value' that pairs with the key. 
    This relationships in computing is called a Key Value Pair relationship. 
'''
# a dictionary example @14.35
super_villains = {'Fiddler': 'Issac Bowin', 'Captain Cold': 'Leonard Snart', 'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder', 'Pied Piper': 'Thomas Peterson'}
print("Our villain dictionary looks like so:", end='')
print(super_villains)
# you can print a value if you provide a key
print("Captain Cold's real identity is:", super_villains['Captain Cold'])  # notice how the braces are square braces whenever
# providing a position or key

# if we wanted to delete a character/an entry in our dictionary.
del super_villains['Fiddler']
print(super_villains)
# We can replace a villain's real identity if we find that we got it wrong for example
super_villains['Pied Piper'] = 'Heartley Rathaway'
print("New List of Villains with Pied Piper's real name change:", super_villains)
# Finding out the sum of villains in our dictionary
print("We have", len(super_villains), "in our dictionary")
# Can GET a villain's real name another way
print("Pied Piper's now real name is:", super_villains.get('Pied Piper'))
# you can get a list of all super villain keys
print("Our super villians' code names/keys:", super_villains.keys())
# you can get a list of all super villain values
print("Our super villains' real names/values:", super_villains.values())

print("\n")
print("----------------------------CONDITIONALS--------------------------------")
'''
    IF, ELSE AND ELIF are used to perform actions based on different conditions.
    These conditions come in the following
    ==  : equals
    >   : greater than
    <   : less than
    >=  : greater or equal
    <=  : less or equal
    
'''
# a conditionals example @16.20
# ONCE A CONDITION IS MET, THERE IS NO NEED FOR THE LOOP TO CONTINUE SO IT BREAKS

age = 30
if (age > 16):
    print("You're old enough to drive.")

if (age >= 21):
    print('You\'re old enough to drive a tractor trailer.')
elif (age >= 16):
    print("You are definitely old enough to drive a car.")
else:
    print('You are not old enough to drive.')
# We are able to combine conditions using logical operators. These are 'and', 'or', 'not' @19.40min
if((age >= 1) and (age <= 18)):
    print("You get a birthday party!")
elif((age == 21) or (age >= 65)):
    print('You get a big birthday party!')
elif not(age == 30):
    print("You don't get a birthday party!")
elif(age != 50): #means the same as the above ! means NOT
    print("You don't get a birthday party!")
else:
    print('You get a birthday party! Yaay!!!!')

print("\n")
print("----------------------------LOOPS--------------------------------")
'''
    These constructs allow you to perform an action a set number of times. They can be used to greater
    effect when used in conjunction with conditionals. These include, 'For loop', 'While loop'
'''
# Some loop examples @19.46
print("print a range of numbers 0-10 but doesn't include 10. So it starts from 0 and cycles 10 times which ends at 9!")
for i in range(0, 10):#work up to but not including 10
    print(i, ' ', end='')
print('\n')
# We can cycle through a list
grocery_list = ['Juice','Mangoes', 'Oranges', 'Milk', 'Vegetables']
print("Grocery list printed with a for loop")
for y in grocery_list:
    print(y)
# You can define a list for the for loop to cycle through right in the loop
print("Defining items to cycle through, right in the for loop")
for x in [2,8,26,46,3,4,3]:
    print(x, ' ', end='')
print('\n')
# We can double up for loops to print lists within a list
num_list =[[1,10,15],[6,18,120],[4,9,60]]
print("Printing the list", num_list, "using  a double for loop")
for m in range(0,len(num_list)):
    for n in range(0, 3):
        print(num_list[m][n],' ', end='')
print('\n')

# A while loop is the other looping mechanism in Python. This is used when you don't know how many times a loop will need to be cycled through.

#let's first get a random number for the example's sake
rand_num = random.randrange(0, 50)#generates a random number from 0-99
print("Cycle through getting a random number 0-49 until number = 15")
while rand_num != 15:
    print(rand_num,' ', end='')
    rand_num = random.randrange(0,50)
print('\n')

# using a while loop in a for loop kind of way.
print("Using a while loop similarly to a for loop, we can define a length to iterate to (iterator)")
i = 0 #called your iterator
while(i <= 30):
    # let's print only even numbers
    if((i%2) == 0):
        print(i,' ', end='')
    elif(i == 19):
        break #forces breakage(jumping out) of loop completely
    else:
        i += 1
        continue
    i += 1
print('\n')
print("----------------------------FUNCTIONS--------------------------------")
'''
    Blocks of code that can be used and reused to build bigger code components like lego pieces.
    Functions allow you to write more readable code.
'''
# functions examples @24.55min
def addNumbers(fnum, snum):#def = define (example, example) <== these are called parameters/inputs your function needs to do its job
    sum = fnum + snum
    return sum
#a function has to be defined before it's called.
print("Sum of 13 + 98 =",addNumbers(13, 98)) #can't print sum directly here because it only exists in that function addNumbers()/sum is out of scope

print("\n Getting user input \n")
print("What's your name by the way?")
#name = sys.stdin.readline()
name = 'John Doe'
print("Hello",name)


print('\n')
print("----------------------------STRINGS--------------------------------")
'''
    Characters in a row, and their manipulation
'''
long_string = "I'll Catch You if You Fall - The Floor"
print("Here is our long string:",long_string,"\n")
print("Let's print it up to but not including the 4th index [0:4]:", long_string[0:4])
print("Let's print the last 5 characters [-5:]:", long_string[-5:])
print("Let's print everything but the last 5 characters [:-5]:", long_string[:-5])
print("We can concatenate/join two strings together, or even substrings ([0:4]+\" be there\"):", long_string[0:4]+" be there")#@27.56min
print("The following string is FORMATTED:")
print("%c is my %s letter and my %d number is %.5f" %('D', 'favourite', 12, .659)) #% sign formatting is followed by each type you intent to fill it
#  in with later.
print("Capitalizing the just the first letter of the string  '",long_string,"':",long_string.capitalize())
print("Finding where a substring or character lies within a string", long_string.find('Floor'))#what you're finding is case-sensitive
print("Finding if a string contains only letters", long_string.isalpha())
print("Finding if a string contains only numbers", long_string.isalnum())
print("Finding how many characters make up your string/length", len(long_string))
print("Replacing a specific word with another word, 'Floor:Angel'::",long_string.replace('Floor', 'Angel'))
print("If you wanted to strip whitespace", long_string.strip())#for when there is whitespace or potential for whitespace at end or start of string
print("We can split a string into a list:")
quote_list = long_string.split(" ")#the " " is the means we want to split the string by. if there were commas you could use those too but space
# works here.
print(quote_list)

print('\n')
print("----------------------------I/O (FILE INPUT AND OUTPUT)--------------------------------")
'''
    Allows you to create, write and read from files directly in windows. @30.20min
'''


