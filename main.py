from random import randint

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
    
