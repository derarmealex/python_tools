words = set()
while len(words) < 3:
    word = input("Enter a four character word: ")
    if len(word) == 4 and word not in words:
        words.add(word)
    elif word in words:
        print("Word", word.upper(), "is already entered")
    else:
        print("The word is not four character".upper())
print("Three words are already saved:\n", ", ".join(words))
# or
words = set()
while len(words) < 3:
    word = input("Enter a four character word: ")
    if len(word) == 4 and word not in words: words.add(word)
    elif word in words: print("Word", word.upper(), "is already entered")
    else: print("The word is not four character".upper())
print("Three words are already saved:\n", ", ".join(words))