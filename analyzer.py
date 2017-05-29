import nltk
from nltk.tokenize import TweetTokenizer
import string

class Analyzer():
  
       
    def __init__(self, essay):
        tokenizer = nltk.tokenize.TweetTokenizer() # initialize the tokenizer object
        with open(essay, 'r') as text: 
            self.essay = text.read().replace('/n', '') # save the file as string into "self.essay"
        tokens = tokenizer.tokenize(self.essay) # divide the string into words(tokens) and save as a "list"git 
    
    def word_count(self): # basically counts the number of tokens except the punctuation symbols
        count = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(self.essay)
        for token in tokens:
            if token not in string.punctuation:
                count = count + 1
        return count  # so far the number is one more than the actual one. Dunno why??
        
    def number_of_sentences(self):          # exactly determines the number of sentences in the text
        count = 0                           # exception cases include the sentences starting with numbers or symbols
        switch = 0
        for character in self.essay:
            if character == '.':
                switch = 1
            if character[0].isupper() and switch == 1:
                count = count + 1
                switch = 0
        print "Number of sentences: ", count
    
    
    def tagging(self):
        text = nltk.tokenize.word_tokenize(self.essay)
        printed = nltk.pos_tag(text)        # this is the most powerful function of my whole code. It analyzes the sentence into grammatical parts.
        adjective_count = 0
        noun_count = 0
        verb_count = 0
        
        for i in range(self.word_count()):
            if printed[i][1] == "JJ":
                adjective_count = adjective_count + 1
            if printed[i][1] == "VBN" or printed[i][1] == "VB":
                verb_count = verb_count + 1
            if printed[i][1] == "NN" or printed[i][1] == "NNS" or printed[i][1] == "NNP" :
                noun_count = noun_count + 1
        #print(printed)
        print "Number of adjectives: ", adjective_count 
        print "Number of nouns: ", noun_count
        print "Number of verbs: ", verb_count
        
        