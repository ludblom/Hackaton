class Joke:
    jokelist = ["a b c, b c d, c d e, d e f"]

    # separates jokes
    def separatejokes(jokeslist):
        return jokeslist.split("####")
    separatedjokes = []
    for joke in jokelist:
        separatedjokes.append(separatejokes(jokelist))

    # list of all words in all jokes
    wordlist = []
    def createwordlist(jokeslist):
        wordlist = []
        for w in wordlist:
            wordlist.append(wordlist[w])

    # finds frequency of inputted word and returns (word, frequency)
    def freqofword(word, wordlist):
        freqcount = 0
        for string in wordlist:
            if string == word:
                freqcount+=1
        return "word" + freqcount

    wordandwordfreq = []
    for word in wordlist:
        wordandwordfreq.append(freqofword(word, wordlist))

    # finds a specific word in the wordlist and returns the frequency
    def findfreqbyword (word, wordlist):
        for string in wordlist:
            if string == word:
                return string[1]

