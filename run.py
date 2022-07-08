from Star_Wars_and_Open_Movie_APIs import StarWarsFilm
from Star_Wars_and_Open_Movie_APIs import Character
from Star_Wars_and_Open_Movie_APIs import StarWarsLibrary
import requests
import datetime

movieList = []
#titleList contains titles for all six episodes
titleList = ["A New Hope", "The Empire Strikes Back", "Return of the Jedi", "The Phantom Menace", "Attack of the Clones","Revenge of the Sith"]
titleEdited = list(map(lambda x: x.replace(" ","+"), titleList))
romeNumList = ["IV", "V", "VI", "I", "II", "III"]
#the API key for OMDB API, change to your own key
key = "9a37732b"

for i in range(len(titleList)):
    detail = requests.get(f"http://swapi.dev/api/films/{i+1}").json()
    characterList = []
    #The fourth episode named differently on imdb, so need to address that.
    if i != 0:
        rate = requests.get(f"http://www.omdbapi.com/?t=Star+Wars%3A+Episode+{romeNumList[i]}+-+{titleEdited[i]}&apikey={key}").json()
    else:
        rate = requests.get(f"http://www.omdbapi.com/?t=Star+Wars&apikey={key}").json()

    for j in detail["characters"]:
        info = requests.get(j).json()
        aCharacter = Character(info["name"],info["height"],info["mass"],info["hair_color"],\
        info["skin_color"],info["eye_color"],info["birth_year"],info["gender"])
        characterList.append(aCharacter)

    movie = StarWarsFilm(detail["title"], detail["episode_id"], detail["opening_crawl"], detail["director"],\
        detail["producer"], detail["release_date"], characterList, rate["Plot"], rate["Ratings"][1]["Value"],rate["BoxOffice"])

    movieList.append(movie)

theLibrary = StarWarsLibrary(movieList, datetime.datetime.now())
#record valid options for main()
actionList = ["f","c","s","e"]

def main():
    while True:
        input1 = input("\nPlease enter your action here: (f: Find Film/c: Find Characters/s: Sort Library/e: Exit)").lower()
        if input1 not in actionList:
            print("\nInvalid Input. Please Try Again.")
            continue
        elif input1 == "f":
            theLibrary.searchFilm()
            continue
        elif input1 == "c":
            theLibrary.searchCharacter()
        elif input1 == "s":
            theLibrary.sort()
            print("\nThe library is sorted by episode id in an ascending order.")
            continue
        else:
            print("\nThank you for using the library, goodbye.")
            break

if __name__ == "__main__":
    main()