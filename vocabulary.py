import sys
import nltk
import os
from analyzer import Analyzer
 

def main():
     
    # establish the path to the file
    essay = os.path.join(sys.path[0], "essay.txt")
    if not essay:
        sys.exit("Could not find the path")
    # instantiate the object    
    analyzer = Analyzer(essay)
    
    # call the functions
    print 'Number of words: ' , (analyzer.word_count())
    print 'Number of sentences: ' ,analyzer.number_of_sentences()
    #analyzer.tagging()
    print 'Number of complex words: ' , analyzer.complex_words()
    print 'Number of syllables: ', analyzer.syllables()
    print 'Number of characters: ' , analyzer.number_of_characters()
    print 'Number of unique words: ' , analyzer.unique_word_count()
    print 'Characters per word: ' , "{0:.2f}".format(analyzer.number_of_characters()/(analyzer.word_count()*1.0))
    print 'Syllables per word: ', "{0:.2f}".format(analyzer.syllables()/(analyzer.word_count()*1.0))
    print 'Words per sentence: ', "{0:.2f}".format( analyzer.word_count()/ (analyzer.number_of_sentences()*1.0))
    print '              DEEP ANALYSIS(in percent)          '
    analyzer.deep_analysis()
if __name__ == "__main__":
    main()