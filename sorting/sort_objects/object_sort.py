movies = [
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Drama", "Crime"]
    },
    {
        "title": "The Godfather",
        "year": 1972,
        "genres": ["Crime", "Drama"]
    },
    {
        "title": "The Godfather: Part II",
        "year": 1974,
        "genres": ["Crime", "Drama"]
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "genres": ["Action", "Crime", "Drama", "Thriller"]
    },
    {
        "title": "pulp fiction",
        "year": 1994,
        "genres": ["Crime", "Drama"]
    },
    {
        "title":"Inception",
        "year": 2010,
        "genres": ["Action", "Crime", "Drama", "Mystery", "Sci-Fi", "Thriller"]
    },
    {
        "title": "Schindler's List",
        "year": 1993,
        "genres": ["Biography", "Drama", "History"]
    },
    {
        "title":"Interstellar",
        "year": 2014,
        "genres": ["Adventure", "Drama", "Sci-Fi"]
    },
    {
        "title": "Fight Club",
        "year": 1999,
        "genres": ["Drama"]
    },
]

def sort_movies_by_year(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie['year'], reverse=True)
    return sorted_movies

def sort_movies_by_title(movies):
    def remove_leading_articles(title):
        articles = ['the ', 'an ', 'a']
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    sorted_movies = sorted(movies, key=lambda movie: remove_leading_articles(movie['title'].lower()))
    return sorted_movies

if __name__ == '__main__':
    sorted_by_year = sort_movies_by_year(movies)
    print('Sorted by year:')
    for movie in sorted_by_year:
        print(movie['title'], movie['year'])

    sorted_by_title = sort_movies_by_title(movies)
    print('\nSorted by title:')
    for movie in sorted_by_title:
        print(movie['title'], movie['year'])


    



