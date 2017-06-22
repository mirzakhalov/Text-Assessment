import sys, nltk, os, string
from nltk.tokenize import TweetTokenizer
from analyzer import Analyzer
from dict import Dictionary

def main():

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
    path = '/home/ubuntu/workspace/text_assessment/samples'
    print 'File ID' + '\t\t\t' + 'Easy' + '\t' + 'Medium' + '\t' + 'Advanced'
    
    # get each file from the folder and analyze 
    for filename in os.listdir(path):
        essay = os.path.join("/home/ubuntu/workspace/text_assessment/samples", filename)
        # initialize the object
        analyzer = Analyzer(essay)
        # get the whole text in the form of token put into the list
        tokens = analyzer.return_tokens(essay)
        for token in tokens:
           if token not in string.punctuation:
               if dictionary.check(token) == 1: # function returns 1 if the word is in the 'easy' list
                   count1 = count1 + 1
               if dictionary.check(token) == 2: # returns 2 if in the 'medium' list
                   count2 += 1
               if dictionary.check(token) == 3: # returns 3 if in the 'advanced' list
                   count3 += 1
               else:
                   continue
        
        # twd stands for "total words detected"
        twd = count1 + count2 + count3
        # print the result in so that it aligns like a table
        print (filename + "\t\t" + "{0:.2f}".format(count1*100.0/twd) + "%" + "\t" + 
        "{0:.2f}".format(count2*100.0/twd) + "%" + "\t" + "{0:.2f}".format(count3*100.0/twd) + "%")

if __name__ == "__main__":
    main()
