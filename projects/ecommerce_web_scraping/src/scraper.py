import time
import random
import requests
from pathlib import Path
from typing import Optional
from .config import BASE_URL, RAW_DATA_DIR, HEADERS


class Scraper:
    """
    Simple helper class for downloading pages and saving the raw HTML.
    Handles retries and basic waiting between requests.
    """

    def __init__(self, base_url: str = BASE_URL, headers: dict = HEADERS):
        self.base_url = base_url
        self.headers = headers

        # Make sure the raw data folder exists
        Path(RAW_DATA_DIR).mkdir(parents=True, exist_ok=True)

    def _wait(self):
        """Pause briefly between requests."""
        time.sleep(random.uniform(1.0, 2.0))

    def fetch_page(self, url: str) -> Optional[str]:
        """
        Download a single page. Returns the HTML text or None if it fails.
        """
        attempts = 3

        for i in range(attempts):
            try:
                response = requests.get(url, headers=self.headers, timeout=10)

                if response.status_code == 200:
                    return response.text

                print(f"Attempt {i+1}: status code {response.status_code}")

            except requests.exceptions.RequestException as err:
                print(f"Attempt {i+1}: error fetching {url}: {err}")

            self._wait()

        print(f"Could not fetch {url} after {attempts} attempts.")
        return None

    def save_raw(self, html: str, filename: str):
        """Write the raw HTML to the raw/ folder."""
        path = Path(RAW_DATA_DIR) / filename
        path.write_text(html, encoding="utf-8")
        print(f"Saved: {path}")

    def fetch_and_save(self, url: str, filename: str):
        """Convenience method: download a page and save it."""
        html = self.fetch_page(url)
        if html:
            self.save_raw(html, filename)
        return html
