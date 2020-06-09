import webbrowser
import requests


def search_google(query):
    query = query.replace(' ', '+')
    url = f"https://google.com/search?q={query}"

    # desktop user-agent
    resp = requests.get(url)
    if resp.status_code == 200:
        url = resp.url
        webbrowser.MacOSX('default').open(url)
    else:
        return None


def search_imdb():
    url = "https://imdb8.p.rapidapi.com/title/get-overview-details"

    querystring = {"currentCountry": "US", "tconst": "tt0944947"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "91aab86f57msh8f51ad9512d613cp1d292cjsn5179a1286f1d"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.text)


search_imdb()
