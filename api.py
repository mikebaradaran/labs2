import requests
# Hello
url="http://www.omdbapi.com/?apikey=ef5e4257&s=star"

data = requests.get(url)
data = data.json()
print(data["Search"])
print(data["Search"][0])
print(data["Search"][0]["Poster"])
