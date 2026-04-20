# import pytest
# from playwright.sync_api import sync_playwright
#
# @pytest.fixture(scope="function")  # <-- важно: function, не session
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         context = browser.new_context()
#         page = context.new_page()
#         yield page
#         context.close()
#         browser.close()