import requests
from bs4 import BeautifulSoup
import webbrowser

def random_wikipedia_article():
    """Gets random title of wikipedia article and asks user if they want to read it.
    Args: None
    Results: Shows random generated article or ends with None.
    Raises: AnyError: if anything bad happens."""
    url = 'https://en.wikipedia.org/wiki/Special:Random'
    response = requests.get(url, allow_redirects=False)

    new_url = response.headers['Location']
    response = requests.get(new_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    print(title.string)
    
    answer = ""
   
    print("Do you want to read this article?(yes/no)")
    answer = str(input().lower())
    if answer == "yes":
        webbrowser.open_new(new_url)
    else:
        print("Do you want to get another article? (yes/no)")
        answer = str(input().lower())
        if answer == "yes":
            random_wikipedia_article()