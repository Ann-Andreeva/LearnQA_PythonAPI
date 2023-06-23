import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

n = len(response.history) - 1
print(n)
print(response.history[n].url)