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
    print 'Number of words: ' ,analyzer.word_count()
    analyzer.number_of_sentences()
    analyzer.tagging()
    
if __name__ == "__main__":
    main()