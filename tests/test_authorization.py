from os import name

from playwright.sync_api import Page, expect

email = 'Bob2@mail.ru'
password = 'some_pass'

def test_register(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    page.locator(".ico-register").click()

    page.locator('#gender-male').click()
    page.locator('#FirstName').click()
    page.locator('#FirstName').fill('Bob')
    page.locator('#LastName').click()
    page.locator('#LastName').fill('Stivenson')
    page.locator('#Email').click()
    page.locator('#Email').fill(email)
    page.locator('#Password').click()
    page.locator('#Password').fill(password)
    page.locator('#ConfirmPassword').click()
    page.locator('#ConfirmPassword').fill(password)

    page.locator('#register-button').click()


def test_login(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    page.locator(".ico-login").click()

    page.locator(".email").click()
    page.locator(".email").fill(email)
    page.locator(".password").click()
    page.locator(".password").fill(password)

    page.locator(".login-button").click()

    expect(page.locator("body")).to_contain_text(email)

def test_login_fail(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    page.locator(".ico-login").click()

    page.locator(".email").click()
    page.locator(".email").fill("Some@mail.ru")
    page.locator(".password").click()
    page.locator(".password").fill("1111")

    page.locator(".login-button").click()

    expect(page.locator("body")).to_contain_text("Login was unsuccessful.")

def test_forgot_password(page: Page) -> None:
    pass

def test_remember_login(page: Page) -> None:
    pass

def test_logout(page: Page) -> None:
    pass