import sys
import nltk

def main():
    text = nltk.tokenize.word_tokenize("I love you")
    printed = nltk.pos_tag(text)
    print(printed)
    print(printed[0][1])
    
if __name__ == "__main__":
    main()