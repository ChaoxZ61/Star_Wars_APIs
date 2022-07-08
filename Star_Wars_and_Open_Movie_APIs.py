from dataclasses import dataclass, field
import datetime

@dataclass
class StarWarsFilm:
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    characters: list
    plot: str
    RottenTomatoesRating: str
    BoxOfficeGross: str = field(metadata={"units":"U.S.dollars"})

    def __gt__(self, other):
        return self.episode_id > other.episode_id

    def __ge__(self, other):
        return self.episode_id >= other.episode_id

    def __eq__(self, other):
        return self.episode_id == other.episode_id

@dataclass
class Character:
    name: str
    height: int = field(metadata={"units":"centimeters"})
    mass: int = field(metadata={"units":"kilograms"})
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str

    def __str__(self):
        return f"""{self.name}, Height: {self.height}cm, Mass:{self.mass}kg, Hair Color: {self.hair_color},
Skin Color: {self.skin_color}, Eye Color: {self.eye_color}, Birth Year: {self.birth_year}, Gender: {self.gender}"""

@dataclass
class StarWarsLibrary:
    movies: list
    lastUpdated: datetime

    def sort(self):
        sorted(self.movies)

    def searchFilm(self):
        while True:
            searchKey = input("\nChoose the way you want to look for a movie (i: by Episode Id/t: by Title):").lower()
            if searchKey != "i" and searchKey != "t":
                print("\nIn valid option, please try again!")
            else: break

        if searchKey == "i":
            while True:
                episodeID = input("\nPlease the episode ID (1-6):")
                if episodeID.isnumeric() == False:
                    print("\nPlease input an integer.")
                elif int(episodeID) < 1 or int(episodeID) > 6:
                    print("\nID out of range. Please try again.")
                else:
                    for i in range(len(self.movies)):
                        if int(episodeID) == self.movies[i].episode_id:
                            print(self.movies[i])
                    break
        else:
            movieFound = False
            title = input("\nPlease the title of the movie:")
            for i in range(len(self.movies)):
                if title == self.movies[i].title:
                    movieFound = True
                    print(self.movies[i])
            if movieFound == False:
                print("\nTitle not found. Please try again.")

    def searchCharacter(self):
        #a trigger to prevent from printing character info repeatly if it appears in multiple movies.
        infoPrinted = 0
        characterName = input("\nPlease enter the name of the character you want to look for:")
        for i in self.movies:
            for j in i.characters:
                if characterName == j.name:
                    if infoPrinted == 0:
                        print(j)
                        infoPrinted += 1
                    print(i)
        if infoPrinted == 0:
            print("\nThe Character you searched for did not appear in any movies in the library.")
