from urllib.parse import urljoin
from src.scraper import Scraper
from src.parser import Parser
from src.config import BASE_URL


class CategoryDiscovery:
    """
    Fetches the homepage and extracts all category names + URLs.
    """

    def __init__(self):
        self.scraper = Scraper()
        self.parser = Parser()

    def discover(self) -> dict:
        """Return a dictionary of {category_name: full_url}."""
        html = self.scraper.fetch_page(BASE_URL)
        if not html:
            print("Could not load homepage.")
            return {}

        soup = self.parser.get_soup(html)

        # The category list is inside <ul class="nav nav-list">
        nav = soup.find("ul", class_="nav nav-list")
        if not nav:
            print("Could not find category list.")
            return {}

        categories = {}

        # All categories are inside the second <ul> inside nav
        items = nav.find_all("a")

        for tag in items:
            name = tag.text.strip()
            href = tag.get("href")

            # Skip the root "Books" category
            if name.lower() == "books":
                continue

            full_url = urljoin(BASE_URL, href)
            categories[name] = full_url

        return categories