import httpx
from bs4 import BeautifulSoup

url = "https://www.houseoffraser.co.uk/men/hoodies-and-sweatshirts"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}

def main():
    # 1. Download the page
    response = httpx.get(url, headers=headers, timeout=30.0)
    soup = BeautifulSoup(response.text, "html.parser")

    # 2. Find all product cards
    products = soup.select("div[class^='ProductCard_wrapper']")
    print("Found:", len(products))

    # 3. Extract details from each product
    for product in products:
        brand_tag = product.select_one("p[data-testid='product-card-brand']")
        brand = brand_tag.get_text(strip=True) if brand_tag else None

        name_tag = product.select_one("h2[data-testid='product-card-name-without-brand']")
        name = name_tag.get_text(strip=True) if name_tag else None

# discounted price
        discount_tag = product.select_one("span[class^='Price_isDiscounted']")
        discounted_price = discount_tag.get_text(strip=True) if discount_tag else None

        # original price
        original_tag = product.select_one("span[class^='Price_ticketPrice']")
        original_price = original_tag.get_text(strip=True) if original_tag else None

        print({
            "brand": brand,
            "name": name,
            "discounted_price": discounted_price,
            "original_price": original_price
        })
      

if __name__ == "__main__":
    main()



