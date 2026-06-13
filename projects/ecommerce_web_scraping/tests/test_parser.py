from src.scraper import Scraper
from src.parser import Parser

def test_parser_product_page():
    scraper = Scraper()
    parser = Parser()

    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    html = scraper.fetch_page(url)

    data = parser.parse_product_page(html)

    assert isinstance(data, dict)
    assert "title" in data
    assert "price" in data

    print("Parser test passed — product page parsed successfully.")