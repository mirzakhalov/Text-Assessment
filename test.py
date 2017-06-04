import sys
import nltk

def main():
    text = nltk.tokenize.word_tokenize("Although I love you, I can live without you")
    vowels = 'aeiouyAEIO'
    dth = 'uioy'
    count = 0
    for word in text:
        for i in range(len(word)):
            if word[i] in vowels:
                count = count + 1
            if word[i] == 'e' and word[i] == word[len(word)-1]:
                count = count - 1
            if word[i] == 'y' and word[i] == word[0]:
                count = count - 1
            if word[i] == 'o' and word[i+1] != word[len(word)]:
                if word[i+1] in dth:
                    count = count - 1
        print(count)
        count = 0
    
    
if __name__ == "__main__":
    main()