write_again = True
word_collection = str("TRUE WEALTH\n\n\nOnce upon a time, there lived a very rich and wealthy man in a big "
                      "town. \nHe "
                      "led a "
                      "luxurious "
                      "life. ""He always boasted about his wealth to his friends and relatives. \n\n"
                      ""
                      "His son was studying ""in a distant city and he ""returned home for vacation. "
                      "The rich \nman wanted to show off to his son how rich he was. But his son wasn’t "
                      "fond of any \nluxurious lifestyle. However, the rich man wanted to make his \nson realize that his lifestyle was "
                      "extremely rich and that poor people suffered a lot. He planned a day’s \nvisit to the entire town to show him "
                      "the life of the poor people. \n\n"
                      ""
                      "The father and the son took a chariot and visited the entire town. They returned \n"
                      "home after two days. The father was happy that his son was very quiet after seeing \nthe poor people honouring "
                      "the rich man and after witnessing the \nsufferings of the poor due to lack of facilities. \n\nThe rich man asked his "
                      "son, “Dear boy, how was the trip? \nHave you enjoyed it?” “Yes my dad, it was a great trip with you,"
                      "” the son replied.\n\n“So, what did you learn from the trip?” the father asked. The son was silent. \n\n“Finally you "
                      "have realized how the poor suffer and how they actually live,” said the father. \n\n“No father,” replied the son. "
                      "He added, “We have only two dogs, they have 10 dogs. We have a big pool in our garden, but they \nhave a massive "
                      "bay without any end! We have luxurious and expensive lights imported from various countries, but they have \n"
                      "countless stars lighting their nights. We have a house on a small piece of land, but they have abundant fields"
                      " that go beyond \nthe horizon. We are protected by huge and strong walls around our property, but they bond with "
                      "each other and surround \nthemselves with their fellow beings. We have to buy food from them, but they are so rich "
                      "that they can cultivate their own \nfood.” \n\nThe rich father was stunned and speechless, on hearing his son’s words. \n\n"
                      "Finally the son added, “Dad, thank you so much for showing me who is rich and who is poor. Thank you for letting "
                      "me \nunderstand how poor we really are!” \n\nTRUE WEALTH IS NOT MEASURED BY MONEY AND PROPERTY! TRUE WEALTH IS "
                      "CREATED ""IN GOOD FRIENDSHIPS AND COMPASSIONATE RELATIONSHIPS.")

true = str(input("Give me an adjective..."))
TRUE = str(input("ANOTHER ADJECTIVE IN CAPS..."))
# word_collection.replace("TRUE", true)
son = str("daughter")
# word_collection.replace("son", son)
rich = str(input("What's an adjective that perfectly sums up your current living situation?..."))
# word_collection.replace("rich", rich)
poor = str(input("What's an adjective that sums up a life you don't want to be in?..."))
# word_collection.replace("poor", poor)
wealth = str(input("Give me an adjective..."))
WEALTH = str(input("ANOTHER ADJECTIVE IN CAPS..."))
# word_collection.replace("WEALTH", true)
luxurious = str(input("One word to describe how you're used to living!..."))
# word_collection.replace("luxurious", luxurious)
people = str(input("What's another word for 'People'?..."))
# word_collection.replace("people", people)
town = str(input("What town do you live in?..."))
# word_collection.replace("town", town)
father = str("daddy")

words_to_replace = ("true", "TRUE", "son", "rich", "poor", "wealth", "WEALTH" "luxurious", "people", "town", "father")
replacement_words = (true, TRUE, son, rich, poor, wealth, WEALTH, luxurious, people, town, father)

while write_again:
    for x in range(0, len(words_to_replace)):
        word_collection = word_collection.replace(words_to_replace[x], replacement_words[x])
    print(word_collection)
    write_again = str(input("Write another story? Y or N"))
    if write_again == "Y" or write_again == "y" or write_again == "":
        write_again = True
    else:
        write_again = False
        break
