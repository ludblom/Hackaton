def replace():
    jokes = open("jokes.txt", "r")
    jokes = jokes.read()
    jokes = jokes.split("####")
    newJokes = [jok for jok in jokes if len(jok.split(" ")) <= 30]
    with open("newJokes.txt", "a") as newJoke:
        for joke in newJokes:
            newJoke.write(joke)
            newJoke.write("\n####\n")
        

replace()
