import webbrowser
import requests
from bs4 import BeautifulSoup
from imdb import IMDb


def search_google(query: str):
    """Search in google

    Args:
        query (str): What to search for
    """
    query = query.replace(' ', '+')
    url = f"https://google.com/search?q={query}"

    # desktop user-agent
    resp = requests.get(url)
    if resp.status_code == 200:
        url = resp.url
        webbrowser.MacOSX('default').open(url)
    else:
        return None


def search_imdb(genre: str):
    """Search for movies in IMDB

    Args:
        genre (str): The genre of the movies

    Returns:
        list: list of top 5 newest movies
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
        "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "DNT": "1", "Connection": "close",
    }

    genres = {
        'action': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=action&sort=release_date,desc',
        'adventure': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=adventure&sort=release_date,desc',
        'animation': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=animation&sort=release_date,desc',
        'biography': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=biography&sort=release_date,desc',
        'comdey': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=comedy&sort=release_date,desc',
        'crime': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=crime&sort=release_date,desc',
        'drama': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=drama&sort=release_date,desc',
        'family': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=family&sort=release_date,desc',
        'fantasy': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=fantasy&sort=release_date,desc',
        'history': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=history&sort=release_date,desc',
        'horror': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=horror&sort=release_date,desc',
        'music': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=music&sort=release_date,desc',
        'musical': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=musical&sort=release_date,desc',
        'mystery': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=mystery&sort=release_date,desc',
        'romance': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=romance&sort=release_date,desc',
        'sci-fi': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sci-fi&sort=release_date,desc',
        'sport': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=sport&sort=release_date,desc',
        'thriller': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=thriller&sort=release_date,desc',
        'war': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=war&sort=release_date,desc',
        'western': 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=western&sort=release_date,desc'
    }

    page = requests.get(genres[genre], headers=headers)

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        movies = BeautifulSoup(
            str(soup.find_all("h3", class_="lister-item-header")), 'html.parser')

        movies = movies.find_all(href=True)

        movies_list = []
        movies = str(movies).split(',')[:5]

        for a in movies:
            movies_list.append(a.split('>')[1][:-3])

        return movies_list


def search_movie(movie_name: str):
    """Get details about movie

    Args:
        movie_name (str): The name of the movie

    Returns:
        dict: dictionary with details about the movie
    """
    ia = IMDb()
    movie = ia.get_movie(ia.search_movie(movie_name)[0].getID())
    runtime = int(movie.get('runtimes')[0])
    if 60 < runtime:
        runtime = f"{runtime // 60} hours and {runtime % 60} minutes"

    return {'runtime': runtime, 'rating': movie.get(
        'rating'), 'director': movie.get('director')[0], 'year': movie.get('year'), 'plot': movie.get('plot')[0].split(':')[0]}
