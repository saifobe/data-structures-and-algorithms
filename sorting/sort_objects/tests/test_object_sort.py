import pytest
from sort_objects.object_sort import sort_movies_by_year, sort_movies_by_title

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

def test_sort_movies_by_year():
    

    # Test sorting by year in descending order
    sorted_movies = sort_movies_by_year(movies)
    assert sorted_movies[0]['title'] == "Interstellar"
    assert sorted_movies[0]['year'] == 2014
    assert sorted_movies[-1]['title'] == "The Godfather"
    assert sorted_movies[-1]['year'] == 1972

    # Test sorting by year for a single movie
    single_movie = [
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Drama", "Crime"]
        }
    ]
    sorted_single_movie = sort_movies_by_year(single_movie)
    assert sorted_single_movie[0]['title'] == "The Shawshank Redemption"
    assert sorted_single_movie[0]['year'] == 1994

    # Test sorting an empty list
    empty_list = []
    sorted_empty_list = sort_movies_by_year(empty_list)
    assert sorted_empty_list == []

def test_sort_movies_by_title():
    expected = [
        {
            "title": "Fight Club",
            "year": 1999,
            "genres": ["Drama"]
        },
        {
            "title": "Inception",
            "year": 2010,
            "genres": ["Action", "Crime", "Drama", "Mystery", "Sci-Fi", "Thriller"]
        },
        {
            "title": "Interstellar",
            "year": 2014,
            "genres": ["Adventure", "Drama", "Sci-Fi"]
        },
        {
            "title": "pulp fiction",
            "year": 1994,
            "genres": ["Crime", "Drama"]
        },
        {
            "title": "Schindler's List",
            "year": 1993,
            "genres": ["Biography", "Drama", "History"]
        },
        {
            "title": "The Dark Knight",
            "year": 2008,
            "genres": ["Action", "Crime", "Drama", "Thriller"]
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
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Drama", "Crime"]
        },
    ]
    actual = sort_movies_by_title(movies)
    assert actual == expected