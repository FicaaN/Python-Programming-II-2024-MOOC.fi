class Series:
    
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.sum_of_ratings = 0
        self.counter = 0

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.sum_of_ratings += rating
            self.counter += 1
        else:
            print("Rating should be between 0 and 5.")

    def average_rating(self):
        if self.counter == 0:
            return 0
        return self.sum_of_ratings / self.counter

    def __str__(self):
        if self.counter == 0:
            return (f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\nno ratings")
        else:
            return (f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n"
                    f"{self.counter} ratings, average {self.average_rating():.1f} points")

def minimum_grade(rating: float, series_list: list):
    min_grade_list = []
    for series in series_list:
        if series.counter > 0 and series.average_rating() >= rating:
            min_grade_list.append(series)
    return min_grade_list

def includes_genre(genre: str, series_list: list):
    genre_list = []
    for series in series_list:
        if genre in series.genres:
            genre_list.append(series)
    return genre_list

# This part is for testing out
if __name__ == '__main__':
    
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)

    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)