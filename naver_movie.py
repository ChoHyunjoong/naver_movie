import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

movie = []
for a in soup.select("dt.tit a"):
    diction = {}
    diction['title'] = a.get_text()
    diction['code'] = a['href'].split('code=')[1]
    movie.append(diction)
print(movie)
        
    