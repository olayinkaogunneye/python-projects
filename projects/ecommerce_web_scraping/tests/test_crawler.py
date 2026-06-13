import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.crawler import Crawler

def test_crawler_category():
    crawler = Crawler()

    url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    products = crawler.crawl_category(url)

    assert isinstance(products, list)
    assert len(products) > 0
    assert isinstance(products[0], dict)

    print("Crawler test passed — category scraped successfully.")