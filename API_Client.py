import requests


class APIClient:
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout

    def fetch_data(self):
        try:
            response = requests.get(
                self.url,
                timeout=self.timeout
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as error:
            print(error)
            return []
