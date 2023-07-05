import requests

class TestCookie:
    def test_length(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers = dict(response.headers)
        print(headers)

        assert "Date" in headers, "Header 'Date' not in headers"
        assert "Content-Type" in headers, "Header 'Content-Type' not in headers"
        assert "Content-Length" in headers, "Header 'Content-Length' not in headers"
        assert "Connection" in headers, "Header 'Connection' not in headers"
        assert "Keep-Alive" in headers, "Header 'Keep-Alive' not in headers"
        assert "Server" in headers, "Header 'Server' not in headers"
        assert "x-secret-homework-header" in headers, "Header 'x-secret-homework-header' not in headers"
        assert "Cache-Control" in headers, "Header 'Cache-Control' not in headers"
        assert "Expires" in headers, "Header 'Expires' not in headers"
