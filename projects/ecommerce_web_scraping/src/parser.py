from bs4 import BeautifulSoup
from typing import Optional, Dict, List


class Parser:
    """
    Extracts information from BooksToScrape HTML pages.
    """

    def get_soup(self, html: str) -> BeautifulSoup:
        """Turn raw HTML text into a BeautifulSoup object."""
        return BeautifulSoup(html, "html.parser")

    def parse_listing_page(self, html: str) -> List[str]:
        """
        Extract product links from a category listing page.
        Returns a list of relative URLs.
        """
        soup = self.get_soup(html)
        links = []

        for item in soup.find_all("article", class_="product_pod"):
            link = item.h3.a["href"]
            links.append(link)

        return links


    def parse_product_page(self, html: str, product_url: str = None) -> Optional[Dict]:
        soup = self.get_soup(html)

        try:
            title = soup.find("div", class_="product_main").h1.text.strip()
            availability = soup.find("p", class_="instock availability").text.strip()
            rating = soup.find("p", class_="star-rating")["class"][1]
            image = soup.find("div", class_="item active").img["src"]
            category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()

        # Extract description
            desc_tag = soup.find("div", id="product_description")
            description = (
            desc_tag.find_next("p").text.strip()
            if desc_tag else None
            )

        # Clean price
            raw_price = soup.find("p", class_="price_color").text.strip()
            cleaned_price = raw_price.replace("Â", "").replace("£", "").strip()
            price = float(cleaned_price)

            return {
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "image_url": image,
                "category": category,
                "description": description,
                "product_page_url": product_url
            }

        except Exception as e:
            print(f"Error parsing product page: {e}")
            return None
