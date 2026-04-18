import pytest
from playwright.sync_api import Browser, BrowserContext, Page

@pytest.fixture
def context(browser: Browser) -> BrowserContext:
    """НОВЫЙ контекст для КАЖДОГО теста"""
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        ignore_https_errors=True
    )
    yield context
    # Важно: закрываем контекст ПОСЛЕ теста
    context.close()
