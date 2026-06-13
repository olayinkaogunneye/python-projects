
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scraper import Scraper
from src.config import BASE_URL

def test_scraper_homepage():
    scraper = Scraper()
    html = scraper.fetch_page(BASE_URL)

    assert html is not None
    assert "<html" in html.lower()

    print("Scraper test passed — homepage fetched successfully.")