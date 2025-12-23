from locust import HttpUser, task, between
import random

class N11SearchUser(HttpUser):
    host = "https://www.n11.com"
    wait_time = between(2, 5)

    search_keywords = ["iphone", "laptop", "shoes", "mobile", "tv"]

    def on_start(self):
        self.client.headers.update({
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.n11.com/",
        })


    @task(1)
    def open_homepage(self):
        with self.client.get("/", name="Open Homepage", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Homepage failed with status code {response.status_code}")

    @task(3)
    def search_products(self):
        keyword = random.choice(self.search_keywords)

        with self.client.get(f"/arama?q={keyword}", name="Search Product", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Search failed for '{keyword}' with status code {response.status_code}")
            if response.elapsed.total_seconds() > 2:
                response.failure("Response time exceeded 2 seconds")