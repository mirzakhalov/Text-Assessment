import sys, nltk, os, string
from nltk.tokenize import TweetTokenizer

# these classes should be in the same folder
from analyzer import Analyzer
from dict import Dictionary
import xlsxwriter as xl

def main():

    # Our program uses Victoria University of Wellington's range software vocabulary list
    # For further information on that, please visit and download it at http://www.victoria.ac.nz/lals/resources/range
    # establish the paths for the dictionaries
    dict1 = os.path.join("/Users/mirzakhalov/Documents/PersonalProjects/Text-Assessment/dicts", "gsl_1st.txt")
    dict2 = os.path.join("/Users/mirzakhalov/Documents/PersonalProjects/Text-Assessment/dicts", "gsl_2nd.txt")
    dict3 = os.path.join("/Users/mirzakhalov/Documents/PersonalProjects/Text-Assessment/dicts", "gsl_3rd.txt")
    if not dict1 or not dict2 or not dict3:
        sys.exit("Could not find the path")
    
    # instantiate the object
    dictionary = Dictionary()
    loaded = dictionary.load(dict1, dict2, dict3)
    if not loaded:
       sys.exit("Could not load the dictionaries")
    
    # make the counters for each dictionary
    count1, count2, count3 = 0, 0, 0
    path = '/Users/mirzakhalov/Documents/PersonalProjects/Text-Assessment/samples'
    #print 'File ID' + '\t\t\t' + 'Easy' + '\t' + 'Medium' + '\t' + 'Advanced'
    workbook = xl.Workbook('results.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'FILE ID')
    worksheet.write('B1', 'EASY')
    worksheet.write('C1', 'MEDIUM')
    worksheet.write('D1', 'ADVANCED')
    worksheet.write('E1', 'NUMBER OF WORDS')
    worksheet.write('F1', 'NUMBER OF SENTENCES')
    worksheet.write('G1', 'NUMBER OF COMPLEX WORDS')
    worksheet.write('H1', 'NUMBER OF UNIQUE WORDS')
    
    # get each file from the folder and analyze
    i = 1
    
    for filename in os.listdir(path):
        print("here")
        essay = os.path.join("/Users/mirzakhalov/Documents/PersonalProjects/Text-Assessment/samples", filename)
        # initialize the object
        analyzer = Analyzer(essay)
        # get the whole text in the form of token put into the list
        tokens = analyzer.return_tokens(essay)
        twd = 0
        count1, count2, count3 = 0, 0, 0
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
        
        worksheet.write(i, 0, filename)
        worksheet.write(i,1, float("{0:.2f}".format(count1*100.0/(twd+1))))
        worksheet.write(i,2, float("{0:.2f}".format(count2*100.0/(twd+1))))
        worksheet.write(i,3, float("{0:.2f}".format(count3*100.0/(twd+1))))
        worksheet.write(i,4, analyzer.word_count())
        worksheet.write(i,5, analyzer.number_of_sentences())
        worksheet.write(i,6, analyzer.complex_words())
        worksheet.write(i,7, analyzer.unique_word_count())
        i += 1
        # print the result in so that it aligns like a table
        #print (filename + "\t\t" + "{0:.2f}".format(count1*100.0/twd) + "%" + "\t" + 
        #"{0:.2f}".format(count2*100.0/twd) + "%" + "\t" + "{0:.2f}".format(count3*100.0/twd) + "%")
    workbook.close()
if __name__ == "__main__":
    main()
