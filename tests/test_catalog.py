from playwright.sync_api import Page, expect

shop = "https://demowebshop.tricentis.com/"

def test_cards_books(page: Page) -> None:
    page.goto(shop + 'books')
    for item in page.locator('.item-box').all():
        # expect(page.locator("body")).to_contain_text(email)
        pass

def test_pages_catalog(page: Page) -> None:
    pass

def test_sort(page: Page) -> None:
    pass

def test_filters(page: Page) -> None:
    pass

def test_product_card(page: Page) -> None:
    pass
