import nltk
from nltk.tokenize import TweetTokenizer
import string


class Analyzer():

   
    def __init__(self, essay):
        tokenizer = nltk.tokenize.TweetTokenizer() # initialize the tokenizer object
        works_cited_start = False
        self.paper = ""
        with open(essay, 'r') as text:
            self.essay = text.read().replace('/n', '') # save the file as string into "self.essay"
        for i in range(len(self.essay)):
            if self.essay[i] == "W" or self.essay[i] == "w":
                if self.essay[i+1] == "o" and self.essay[i+2] == "r" and self.essay[i+3] == "k":
                    if (self.essay[i+4] == "s" and self.essay[i+5] == " ") or self.essay[i+4] == " ":
                        if (self.essay[i+5] == "c" or "C") or self.essay[i+6] == "c" or "C":
                            if (self.essay[i+6] == "i" and self.essay[i+7] == "t" and self.essay[i+8] == "e" and self.essay[i+9] == "d") or (self.essay[i+7] == "i" and self.essay[i+8] == "t" and self.essay[i+9] == "e" and self.essay[i+10] == "d"):
                                self.paper = self.essay[0:i-1]
                                break
        tokens = tokenizer.tokenize(self.paper) # divide the string into words(tokens) and save as a "list"git

    def word_count(self): # basically counts the number of tokens except the punctuation symbols
        count = 0
        works_cited_start = False
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(self.paper)
        for token in tokens:
           if token not in string.punctuation:
                count = count + 1
        return count  # so far the number is one more than the actual one. Dunno why??

    def return_tokens(self, essay):
        tokenizer = nltk.tokenize.TweetTokenizer() # initialize the tokenizer object
        tokens = tokenizer.tokenize(self.paper) # divide the string into words(tokens) and save as a "list"git
        return tokens

    def number_of_sentences(self):          # exactly determines the number of sentences in the text
        count = 0                           # exception cases include the sentences starting with numbers or symbols
        switch = 0
        for character in self.paper:
            if character == '.':
                switch = 1
            if character[0].isupper() and switch == 1:
                count = count + 1
                switch = 0
        return count

    def complex_words(self):
        count = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(self.paper)

        for token in tokens:        # as pointed out in many algorithms of readability, complex word is a word consisting of more than 2 letters
            if len(token) > 2:
                count = count + 1
        return count

    def syllables(self):
        text = nltk.tokenize.word_tokenize(self.paper)
        vowels = 'aeiouyAEIO'               # Apparently, counting the syllables is not only about counting the vowels
        dth = 'uioy'                        # Additionally, we have to take into consideration sequential vowels, silent vowels
        count = 0
        total_count = 0
        max_count = 0
        for word in text:
            for i in range(len(word)):
                if word[i] in vowels:
                    count = count + 1
                if word[i] == 'e' and word[i] == word[len(word)-1]:
                    count = count - 1
                if word[i] == 'y' and word[i] == word[0]:
                    count = count - 1
                if word[i] == 'o' and i < (len(word)-1):
                    if word[i+1] in dth:
                        count = count - 1
            total_count += count
            if count > max_count:
                string = word
                max_count = count
            count = 0
        #print(string)  if uncommented this line will print the word with the most syllables
        return total_count

    def number_of_characters(self):
        text = nltk.tokenize.word_tokenize(self.paper)
        count = 0
        for word in text:
            for symbol in word:
                if symbol not in string.punctuation:
                    count += 1
        return count

    def unique_word_count(self): #calculating the number of unique words
        text = nltk.tokenize.word_tokenize(self.paper)
        count = 0
        array = []
        for word in text:
            if word in string.punctuation:  # making sure words are not punctuation marks
                continue
            else:
                if word not in array:   # making sure they are not repeated
                    array.append(word)
                    count = count + 1
        return count

    def deep_analysis(self):
        text = nltk.tokenize.word_tokenize(self.paper)          # Not sure what they mean?
        tagged = nltk.pos_tag(text)                             # Please read NLTK POS tagging documentation here: http://www.nltk.org/book/ch05.html
        adjectives = ('JJ', 'JJR', 'JJS')
        adverbs = ('RB', 'RBR', 'RBS', 'WHB')
        verbs = ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')
        nouns = ('NN', 'NNS', 'NNP', 'NNPS')
        pronouns = ('PRP', 'PRP$', 'WP', 'WP$')
        determiners = ('DT', 'PDT', 'WDT')
        conjunctions = ('CC')
        interjections = ('UH')
        qualifiers = ('CD', 'EX','POS')
        prepositions = ('IN', 'TO')
        adjective, adverb, verb, noun, pronoun, determiner, conjuction, interjection, qualifier, preposition, unrecognized = 0,0,0,0,0,0,0,0,0,0,0
        total_words = self.word_count() * 1.0
        for i in range(self.word_count()):
            if tagged[i][1] in string.punctuation:
                continue
            elif tagged[i][1] in adjectives:
                adjective += 1
            elif tagged[i][1] in nouns:
                noun += 1
            elif tagged[i][1] in adverbs:
                adverb += 1
            elif tagged[i][1] in verbs:
                verb += 1
            elif tagged[i][1] in pronouns:
                pronoun += 1
            elif tagged[i][1] in determiners:
                determiner += 1
            elif tagged[i][1] in conjunctions:
                conjuction += 1
            elif tagged[i][1] in interjections:
                interjection += 1
            elif tagged[i][1] in prepositions:
                preposition += 1
            elif tagged[i][1] in qualifiers:
                qualifier += 1
            else:
                unrecognized += 1
        print ('Adjectives: ', "{0:.2f}".format((adjective/total_words)*100.0), '%')
        print ('Adverbs: ', "{0:.2f}".format((adverb/total_words)*100.0), '%')
        print ('Nouns: ', "{0:.2f}".format((noun/total_words)*100.0), '%')
        print ('Verbs: ', "{0:.2f}".format((verb/total_words)*100.0), '%')
        print ('Pronouns: ', "{0:.2f}".format((pronoun/total_words)*100.0), '%')
        print ('Conjunctions: ', "{0:.2f}".format((conjuction/total_words)*100.0), '%')
        print ('Determiners: ', "{0:.2f}".format((determiner/total_words)*100.0), '%')
        print ('Prepositions: ', "{0:.2f}".format((preposition/total_words)*100.0), '%')
        print ('Qualifiers: ', "{0:.2f}".format((qualifier/total_words)*100.0), '%')
        print ('Interjections: ', "{0:.2f}".format((interjection/total_words)*100.0), '%')
        print ('Unrecognized: ', "{0:.2f}".format((unrecognized/total_words)*100.0), '%')

class Dictionary():

    def __init__(self):
        self.words1 = set()
        self.words2 = set()
        self.words3 = set()

    def load(self, dict1, dict2, dict3):
        file1 = open(dict1, "r")
        file2 = open(dict2, "r")
        file3 = open(dict3, "r")
        # load the first dictionary
        for word in file1:
            self.words1.adds(line.rstrip("\n"))
        file.close()
        # load the second dictionary
        for word in file1:
            self.words1.adds(line.rstrip("\n"))
        file.close()
        # load the third dictionary
        for word in file1:
            self.words1.adds(line.rstrip("\n"))
        file.close()
        return True

    def check(self, word):
        if word.lower() in self.words1:
            return 1
        elif word.lower() in self.words2:
            return 2
        elif word.lower() in self.words3:
            return 3
        else:
            return 4
