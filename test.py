from random import randint
def tmp():
	print("hello?")

def tmp2():
	print("hello??")

wordFreqs = dict(zip([],[]))

def loadFrequencies() :
	global wordFreqs

	with open ("wordfreqs.txt") as wf :
		words = wf.readlines()
	
	words = [w.strip() for w in words]
	wordFreqs = dict(zip(words, range(0, 10000)))

loadFrequencies()

def getFrequency(word) :
	if (word.lower() in wordFreqs) :
		this_freq = wordFreqs[word.lower()]
	else :
		this_freq = 5000
	return this_freq

def sortFrequency(message) :
	words = message.split(' ')
	return sorted(words, key = lambda k: getFrequency(k), reverse = True)

jokes = ["the weather is good", "haskell?! what is that?"]

shrink = [
	("And how does ", ", in general, make you feel?") ,
	("Why do you think you said ", "?") ,
	("You talk about ", ", do you feel that is important to you?"),
	("What's your opinion on ", "?"),
	("Would you say that you like ", "?"),
	("Tell me more about ", ", please."),
	("What do you mean when you say ", "?")
	]

def findJokeR(message) :
	return findJoke(sortFrequency(message))

def findJoke(words):
    matchedJokes = []
    jokeList = open("jokes.txt", "r")
    jokeList = jokeList.read()
    jokeList = jokeList.split("####")
    
    print(type(jokeList))
    
    for word in words:
        for i in range(len(jokeList)):
            #print(jokeList[i])
            if(word in jokeList[i]):
                matchedJokes.append(i)
        if(len(matchedJokes) != 0):
            break

    #print(matchedJokes)
    #print(randint(0,len(matchedJokes)))
    if(len(matchedJokes) == 0):
        return "Schtopid!"
    return jokeList[matchedJokes[randint(0,len(matchedJokes)-1)]]
    #return matchedJokes[randint(0,len(matchedJokes)-1)]

def main():
    print(findJoke(["horse"]))

if __name__ == "__main__":
    main()
    
def findShrink(message) :
	global shrink
	
	words = sortFrequency(message)
	for word in words :
		if randint(0,1) : 
			a, b = shrink[randint(0, len(shrink) - 1)]
			return a + word + b
	return "Why do you think that is?"
