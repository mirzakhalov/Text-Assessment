import sys, nltk, os, string
from nltk.tokenize import TweetTokenizer
from analyzer import Analyzer
from dict import Dictionary

def main():

    # establish the path to the file
    essay = os.path.join("/home/ubuntu/workspace/text_assessment/samples", "essay.txt")
    if not essay:
        sys.exit("Could not find the path")
    # instantiate the object
    analyzer = Analyzer(essay)

    # Our program uses Victoria University of Wellington's range software vocabulary list
    # For further information on that, please visit and download it at http://www.victoria.ac.nz/lals/resources/range
    # establish the paths for the dictionaries
    dict1 = os.path.join("/home/ubuntu/workspace/text_assessment/dicts", "gsl_1st.txt")
    dict2 = os.path.join("/home/ubuntu/workspace/text_assessment/dicts", "gsl_2nd.txt")
    dict3 = os.path.join("/home/ubuntu/workspace/text_assessment/dicts", "gsl_3rd.txt")
    if not dict1 or not dict2 or not dict3:
        sys.exit("Could not find the path")
    # instantiate the object
    dictionary = Dictionary()
    loaded = dictionary.load(dict1, dict2, dict3)
    if not loaded:
       sys.exit("Could not load the dictionaries")
    # make the counters for each dictionary
    count1, count2, count3 = 0, 0, 0
    tokens = analyzer.return_tokens(essay)
    for token in tokens:
       if token not in string.punctuation:
           if dictionary.check(token) == 1:
               count1 = count1 + 1
           if dictionary.check(token) == 2:
               count2 += 1
           if dictionary.check(token) == 3:
               count3 += 1
           else:
               continue
    # twd stands for "total words detected"
    twd = count1 + count2 + count3

    # call the functions
    print 'Number of words analyzed: ' , twd
    print 'Vocabulary level: \n' + "\tEasy: " + "{0:.2f}".format(count1*100.0/twd) + '%'
    print '\tIntermediate: ' + "{0:.2f}".format(count2*100.0/twd) + '%'
    print '\tAdvanced: ' + "{0:.2f}".format(count3*100.0/twd) + '%'
    print 'Number of words: ' , (analyzer.word_count())
    print 'Number of sentences: ' ,analyzer.number_of_sentences()
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
