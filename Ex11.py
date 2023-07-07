import requests

class TestCookie:
    def test_length(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookies = dict(response.cookies) #.get("auth_cookie")
        print(cookies)
        assert "HomeWork" in cookies, "Key 'HomeWork' not in cookies"

        cookie = cookies["HomeWork"]
        assert cookie == 'hw_value', "Cookie is not correct"
