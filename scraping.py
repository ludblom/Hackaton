from bs4 import BeautifulSoup
import requests


def startScraping():
    counter = 1
    url = "http://www.jokes2go.net/joke/"
    page = requests.get(url)
    
    with open("jokes.txt", "a") as fileName:
        while True:
            # Setup string
            urlJoke = url + str(counter)
            page = requests.get(urlJoke)
            soup = BeautifulSoup(page.text, 'html.parser')

            # Have we reached end?
            if(page.status_code != 200):
                break
            if(counter % 50 == 0):
                print("%d" % counter)
            joke = soup.find_all(class_='joke')
            fileName.write(joke[0].find("p").getText())
            counter += 1
            fileName.write("\n####\n")

startScraping()
