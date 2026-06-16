from urllib.parse import urljoin
from pathlib import Path
from typing import List, Dict, Optional

from src.scraper import Scraper
from src.parser import Parser
from src.config import BASE_URL, BRONZE_DATA_DIR


class Crawler:
    """
    Coordinates the scraping process:
    - listing pages
    - product pages
    - pagination
    """

    def __init__(self):
        self.scraper = Scraper()
        self.parser = Parser()
        Path(BRONZE_DATA_DIR).mkdir(parents=True, exist_ok=True)

    def full_url(self, relative: str) -> str:
    # If the relative URL does not contain 'catalogue/', add it
        if "catalogue/" not in relative:
            relative = "catalogue/" + relative.lstrip("./")
        return urljoin(BASE_URL, relative)


    def crawl_listing_page(self, url: str) -> List[str]:
        """Return full product URLs from a category page."""
        html = self.scraper.fetch_page(url)
        if not html:
            return []

        links = self.parser.parse_listing_page(html)
        return [self.full_url(link) for link in links]

    def crawl_product_page(self, url: str) -> Optional[Dict]:
        """Return product details from a product page."""
        html = self.scraper.fetch_page(url)
        if not html:
            return None

        # Pass the URL into the parser
        return self.parser.parse_product_page(html, url)

    def crawl_category(self, url: str) -> List[Dict]:
        """Crawl all pages in a category (handles pagination)."""
        results = []
        current_url = url

        while True:
            html = self.scraper.fetch_page(current_url)
            if not html:
                break

            # Extract product links from this page
            product_links = self.parser.parse_listing_page(html)

            # Visit each product page
            for link in product_links:
                full = self.full_url(link)
                data = self.crawl_product_page(full)
                if data:
                    results.append(data)

            # Check for next page
            soup = self.parser.get_soup(html)
            next_btn = soup.find("li", class_="next")

            if next_btn:
                next_page = next_btn.a["href"]
                current_url = urljoin(current_url, next_page)
            else:
                break

        return results