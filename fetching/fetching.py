from urllib import request
import json

url = "https://official-joke-api.appspot.com/random_ten"

response = request.urlopen(url)
data = response.read()
jsonData = json.loads(data)

print(f"status code: {response.getcode()}")
print(f"json: {jsonData}")


class Joke:

    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"Set up: {self.setup} (...) Punchline: {self.punchline}"


jokeList = []

for jk in jsonData:
    setup = jk["setup"]
    punchline = jk["punchline"]
    joke = Joke(setup, punchline)
    jokeList.append(joke)

for joke in jokeList:
    print(joke)
