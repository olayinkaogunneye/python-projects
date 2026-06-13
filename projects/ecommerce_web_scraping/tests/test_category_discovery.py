from src.category_discovery import CategoryDiscovery

def test_category_discovery():
    cd = CategoryDiscovery()
    categories = cd.discover()

    assert isinstance(categories, dict)
    assert len(categories) > 0
    assert "Travel" in categories

    print("Category discovery test passed — categories extracted successfully.")