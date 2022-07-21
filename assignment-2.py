group_of_words = str(input("Enter any sentence \n"))
words = [word.lower() for word in group_of_words.split()]
words.sort()
print("The sorted words are:")
for word in words:
    print(word)
