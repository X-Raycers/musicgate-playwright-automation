import allure
from playwright.sync_api import Page, expect


@allure.title("Homepage loads successfully")
def test_homepage_loads(page: Page):
    page.goto("https://musicgate.co.il/")
    expect(page).to_have_url("https://musicgate.co.il/")