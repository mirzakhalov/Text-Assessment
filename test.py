import sys
import nltk
import grammar_check

def main():
    tool = grammar_check.LanguageTool('en-GB')
    text = 'I is working.'
    matches = tool.check(text)
    print(grammar_check.correct(text, matches))
    
if __name__ == "__main__":
    main()