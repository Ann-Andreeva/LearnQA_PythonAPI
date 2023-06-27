import requests
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response1.json()["token"]

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
if response2.json()["status"] == "Job is NOT ready":
    print("Status is correct (Job is NOT ready)")

time.sleep(15)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
if response3.json()["status"] == "Job is ready":
    print(f'Status is correct (Job is ready), result - {response3.json()["result"]}')