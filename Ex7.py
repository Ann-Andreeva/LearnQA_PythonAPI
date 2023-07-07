import requests

print("1.")
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text)

print("2.")
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response2.text)

print("3.")
response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response3.text)

print("4.")
methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    response4 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": {method}})
    print(f"http: get, method: {method} - {response4.text}")

    response5 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": {method}})
    print(f"http: post, method: {method} - {response5.text}")

    response6 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": {method}})
    print(f"http: put, method: {method} - {response6.text}")

    response7 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": {method}})
    print(f"http: delete, method: {method} - {response7.text}")