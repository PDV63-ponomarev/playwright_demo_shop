from playwright.sync_api import Page, expect

shop = "https://demowebshop.tricentis.com/"

def test_give_item_in_cart_simple(page: Page) -> None:
    page.goto(shop + 'books')
    expect(page.locator("#topcartlink")).to_contain_text("(0)")
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.get_by_role("paragraph")).to_contain_text("The product has been added to your shopping cart")
    expect(page.locator("#topcartlink")).to_contain_text("(1)")

def test_give_item_in_cart(page: Page) -> None:
    page.goto(shop + 'desktops')
    expect(page.locator("#topcartlink")).to_contain_text("(0)")
    page.get_by_role("button", name="Add to cart").first.click()
    page.get_by_role("radio", name="Fast [+100.00]").check()
    page.get_by_role("radio", name="GB [+60.00]").check()
    page.get_by_role("radio", name="GB [+100.00]").check()
    page.get_by_role("checkbox", name="Image Viever [+5.00]").check()
    page.get_by_role("textbox", name="Qty:").fill("10")
    page.locator("#add-to-cart-button-72").click()
    expect(page.get_by_role("paragraph")).to_contain_text("The product has been added to your shopping cart")
    expect(page.locator("#topcartlink")).to_contain_text("(10)")

def test_change_item_in_cart(page: Page) -> None:
    page.goto(shop + '141-inch-laptop')
    expect(page.locator("#topcartlink")).to_contain_text("(0)")

    price = page.locator("#product-details-form").text_content()
    page.locator("#add-to-cart-button-31").click()
    expect(page.locator("#topcartlink")).to_contain_text("(1)")

    page.locator('.cart-label').first.click()
    expect(page.locator(".qty-input")).to_have_value("1")
    expect(page.locator('.product-subtotal')).to_contain_text('1590.00')
    page.locator(".qty-input").dblclick()
    page.locator(".qty-input").fill('2')
    page.locator(".qty-input").press("Enter")
    expect(page.locator('.product-subtotal')).to_contain_text('3180.00')


def test_delete_item_in_cart(page: Page) -> None:
    page.goto(shop + 'books')
    page.get_by_role("button", name="Add to cart").first.click()
    expect(page.locator("#topcartlink")).to_contain_text("(1)")
    page.locator('.cart-label').first.click()

    page.locator("input[name=\"removefromcart\"]").check()
    page.get_by_role("button", name="Update shopping cart").click()
    expect(page.locator("body")).to_contain_text("Your Shopping Cart is empty!")


def test_summ_price_in_cart(page: Page) -> None:
    pass

def test_making_order(page: Page) -> None:
    pass
