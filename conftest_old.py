import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.fixture(scope="module")  # Один контекст на все тесты в модуле
def context_module(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context_module: BrowserContext):
    page = context_module.new_page()
    yield page
    page.close()