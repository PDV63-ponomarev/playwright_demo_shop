import pytest
from playwright.sync_api import Page, BrowserContext


@pytest.fixture(scope="function")
def page(browser):
    """Создаёт новую страницу с гарантированной очисткой."""
    # Создаём новый контекст для КАЖДОГО теста
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080},
        ignore_https_errors=True,
        # Важно: не сохраняем состояние между тестами
        storage_state=None
    )

    page = context.new_page()

    # Устанавливаем короткие таймауты для всех операций
    page.set_default_timeout(15000)

    # Автоматически закрываем все всплывающие окна и диалоги
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.on("popup", lambda popup: popup.close())

    yield page

    # Агрессивная очистка после теста
    try:
        page.close()
    except:
        pass

    try:
        context.close()
    except:
        pass

    # Небольшая пауза между тестами
    import time
    time.sleep(1)