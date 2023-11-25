"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, filepath): 
        self.filepath = filepath
        self.array_of_words = []
        self.number_of_words = ''
        self.wordlist = ''
        self.numwords()
        # call function for file len
    def numwords(self):
        file = open(self.filepath)
        for line in file:
            word = line.strip()
            self.array_of_words.append(word)
        print(self.array_of_words)
        number_of_words = len(self.array_of_words)
        self.number_of_words = number_of_words
        print(f"{self.number_of_words} words read.")

    def __repr__(self):
        return f"{self.number_of_words}"
    
    # def listOfWords(self):
    #     wordlist = []
    #     file = open(self.filepath)
    #     readInto = file.read()
    #     for word in readInto:
    #         wordlist.append(word)
    #     self.wordlist = wordlist
    #     # print(self.wordlist)
    #     return self.wordlist

    def random(self): #only need to pass in self, not wordlist as well
        random_words = random.sample(self.array_of_words, 1)[0]
        return random_words
    



wordFinder = WordFinder('words.txt') # wordFinder = class WordFinder('words.txt') 
print(wordFinder)



print(wordFinder.random())
print(wordFinder.random())
    