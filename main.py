from json.decoder import JSONDecodeError
import requests

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print(response.status_code)

# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("не json")

