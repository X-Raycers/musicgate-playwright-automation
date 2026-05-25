import allure
from playwright.sync_api import Page, expect

@allure.title("Open search")
def test_open_search(page: Page):
    page.goto("https://musicgate.co.il/")
    page.get_by_role("textbox").fill("גיטרה")
    page.get_by_role("button", name="חיפוש").click()
    expect(page.locator("body")).to_contain_text("גיטרה")


@allure.title("Search existing product")
def test_search_existing_product(page: Page):
    page.goto("https://musicgate.co.il/")
    page.get_by_role("textbox").fill("CUENCA")
    page.keyboard.press("Enter")
    (expect( page.locator("h2.mf-catalog-title"))
    .to_contain_text("תוצאות חיפוש עבור"))
    expect(page.locator("body")).to_contain_text("CUENCA")


@allure.title("Search invalid product")
def test_search_invalid_product(page: Page):
    page.goto("https://musicgate.co.il/")
    page.get_by_role("textbox").fill("abcdefxyz123")
    page.keyboard.press("Enter")
    (expect( page.locator("h2.mf-catalog-title"))
    .to_contain_text("תוצאות חיפוש עבור"))
    expect(page.locator("body")).to_contain_text("abcdefxyz123")


@allure.title("Empty search")
def test_empty_search(page: Page):
    page.goto("https://musicgate.co.il/")
    page.get_by_role("textbox").fill("")
    page.keyboard.press("Enter")
    expect(page.locator("h1.mf-catalog-title")
    ).to_contain_text("תוצאות חיפוש")


@allure.title("Search with special characters")
def test_search_special_characters(page: Page):
    page.goto("https://musicgate.co.il/")
    page.get_by_role("textbox").fill("@#$%^&*!")
    page.keyboard.press("Enter")
    (expect(page.locator("h2.mf-catalog-title"))
    .to_contain_text("תוצאות חיפוש עבור"))
    expect(page.locator("body")).to_contain_text("@#$%^&*!")


@allure.title("Navigate from search result")
def test_navigate_from_search(page: Page):
    page.goto("https://musicgate.co.il/")
    page.get_by_role("textbox").fill("גיטרה")
    page.keyboard.press("Enter")
    page.get_by_role( "link",name="למיין לפי המעודכן ביותר").click()
    expect(page).to_have_url(("https://musicgate.co.il/%D7%97%D7%A0%D7%95%D7%AA-%D7%9B%D7%9C%D7%99-%D7%A0%D7%92%D7%99%D7%A0%D7%94-%D7%94%D7%9E%D7%A9%D7%AA%D7%9C%D7%9E%D7%AA-%D7%91%D7%99%D7%A9%D7%A8%D7%90%D7%9C?orderby=date&s=%D7%92%D7%99%D7%98%D7%A8%D7%94&post_type=product"))
    expect(page.locator("body")).to_contain_text("גיטרה")