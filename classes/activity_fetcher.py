import requests


class ActivityFetcher:
    @staticmethod
    def fetch_activities(username: str) -> list:
        headers = {"Accept": "application/vnd.github+json"}
        payload = {"per_page": 100, "page": 1}

        r = requests.get(f"https://api.github.com/users/{username}/events",
                         headers=headers,
                         params=payload)

        return r.json()
