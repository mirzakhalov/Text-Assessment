class Dictionary:

    # initialize three sets for dictionaries
    def __init__(self):
        self.words1 = set()
        self.words2 = set()
        self.words3 = set()

    # load the words into the sets
    def load(self, dict1, dict2, dict3):
        file1 = open(dict1, "r")
        file2 = open(dict2, "r")
        file3 = open(dict3, "r")
        # load the first dictionary
        for word in file1:
            self.words1.add(word.rstrip("\r\n"))
        file.close(file1)
        # load the second dictionary
        for word in file2:
            self.words2.add(word.rstrip("\r\n"))
        file.close(file1)
        # load the third dictionary
        for word in file3:
            self.words3.add(word.rstrip("\r\n"))
        file.close(file3)
        return True

    # check if the word is in the sets
    def check(self, token):
        if token.upper() in self.words1:
            return 1
        elif token.upper() in self.words2:
            return 2
        elif token.upper() in self.words3:
            return 3
        else:
            return 4
