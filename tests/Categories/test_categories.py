import allure
from playwright.sync_api import Page, expect


@allure.title("Verify guitars category page title")
def test_verify_guitars_category_page_title(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa"]').click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa")
    expect(page).to_have_title("גיטרות")
    page.wait_for_timeout(5000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(5000)


@allure.title("Navigate to acoustic guitars category")
def test_navigate_to_acoustic_guitars_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa"] span.mega-indicator').click()
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%95%d7%aa"]').click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to electric guitars category")
def test_navigate_to_electric_guitars_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa"] span.mega-indicator').click()
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%97%d7%a9%d7%9e%d7%9c%d7%99%d7%95%d7%aa"]').click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%97%d7%a9%d7%9e%d7%9c%d7%99%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to classical guitars category")
def test_navigate_to_classical_guitars_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa"] span.mega-indicator').click()
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%a7%d7%9c%d7%90%d7%a1%d7%99%d7%95%d7%aa"]').click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa/%d7%92%d7%99%d7%98%d7%a8%d7%95%d7%aa-%d7%a7%d7%9c%d7%90%d7%a1%d7%99%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to amplifiers main category")
def test_navigate_to_amplifiers_main_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d"]').click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d")
    page.wait_for_timeout(5000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(5000)


@allure.title("Navigate to electric guitar amplifiers category")
def test_navigate_to_electric_guitar_amplifiers_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d"] span.mega-indicator').click()
    page.locator("#mega-menu-item-87454").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d/shoes")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to acoustic guitar amplifiers category")
def test_navigate_to_acoustic_guitar_amplifiers_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d"] span.mega-indicator').click()
    page.locator("#mega-menu-item-87452").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d-%d7%9c%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to amplifier accessories category")
def test_navigate_to_amplifier_accessories_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('a.mega-menu-link[href="https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d"] span.mega-indicator').click()
    page.locator("#mega-menu-item-87451").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9e%d7%92%d7%91%d7%a8%d7%99%d7%9d/%D7%90%D7%91%D7%99%D7%96%D7%A8%D7%99%D7%9D-%D7%9C%D7%9E%D7%92%D7%91%D7%A8%D7%99%D7%9D")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to keyboards main category")
def test_navigate_to_keyboards_main_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator("#mega-menu-item-87457").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%90%d7%95%d7%a8%d7%92%d7%a0%d7%99%d7%95%d7%aa-%d7%95%d7%a4%d7%a1%d7%a0%d7%aa%d7%a8%d7%99%d7%9d")
    page.wait_for_timeout(5000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(5000)


@allure.title("Navigate to keyboards category")
def test_navigate_to_keyboards_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator("#mega-menu-item-87457").click()
    page.locator("#mega-menu-item-87458").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%90%d7%95%d7%a8%d7%92%d7%a0%d7%99%d7%95%d7%aa-%d7%95%d7%a4%d7%a1%d7%a0%d7%aa%d7%a8%d7%99%d7%9d/%d7%90%d7%95%d7%a8%d7%92%d7%a0%d7%99%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to electric pianos category")
def test_navigate_to_electric_pianos_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87457 span.mega-indicator').click()
    page.locator("#mega-menu-item-87462").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%90%d7%95%d7%a8%d7%92%d7%a0%d7%99%d7%95%d7%aa-%d7%95%d7%a4%d7%a1%d7%a0%d7%aa%d7%a8%d7%99%d7%9d/%d7%a4%d7%a1%d7%a0%d7%aa%d7%a8-%d7%97%d7%a9%d7%9e%d7%9c%d7%99")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to sheet music stands category")
def test_navigate_to_sheet_music_stands_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87457 span.mega-indicator').click()
    page.locator("#mega-menu-item-87468").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d-%d7%9c%d7%92%d7%99%d7%98%d7%a8%d7%94/%D7%A2%D7%9E%D7%95%D7%93%D7%99-%D7%AA%D7%95%D7%99%D7%9D")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to percussion instruments main category")
def test_navigate_to_percussion_main_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator("#mega-menu-item-87484").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 1500)
    page.wait_for_timeout(2000)


@allure.title("Navigate to darbukas category")
def test_navigate_to_darbukas_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87484 span.mega-indicator').click()
    page.locator("#mega-menu-item-87488").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94-%d7%93%d7%a8%d7%91%d7%95%d7%a7%d7%94")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to bongos category")
def test_navigate_to_bongos_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87484 span.mega-indicator').click()
    page.locator("#mega-menu-item-88211").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to xylophones category")
def test_navigate_to_xylophones_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87484 span.mega-indicator').click()
    page.locator("#mega-menu-item-88216").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%aa%d7%95%d7%a4%d7%99%d7%9d-%d7%95%d7%90%d7%91%d7%99%d7%96%d7%a8%d7%99%d7%9d/%d7%9b%d7%9c%d7%99-%d7%94%d7%a7%d7%a9%d7%94/%d7%a7%d7%a1%d7%99%d7%9c%d7%95%d7%a4%d7%95%d7%a0%d7%99%d7%9d")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to wind instruments main category")
def test_navigate_to_wind_instruments_main_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator("#mega-menu-item-87506").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)



@allure.title("Navigate to harmonicas category")
def test_navigate_to_harmonicas_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87506 span.mega-indicator').click()
    page.locator("#mega-menu-item-87514").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94/%d7%9e%d7%a4%d7%95%d7%97%d7%99%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to melodicas category")
def test_navigate_to_melodicas_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87506 span.mega-indicator').click()
    page.locator("#mega-menu-item-87513").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94/%d7%9e%d7%9c%d7%95%d7%93%d7%99%d7%a7%d7%95%d7%aa")
    page.wait_for_timeout(1000)
    page.mouse.wheel(0, 700)
    page.wait_for_timeout(2000)


@allure.title("Navigate to kazoo category")
def test_navigate_to_kazoo_category(page: Page):
    page.goto("https://musicgate.co.il/")
    page.locator('#mega-menu-item-87506 span.mega-indicator').click()
    page.locator("#mega-menu-item-87516").click()
    expect(page).to_have_url("https://musicgate.co.il/product-category/%d7%9b%d7%9c%d7%99-%d7%a0%d7%a9%d7%99%d7%a4%d7%94/%d7%a7%d7%90%d7%96%d7%95")
    page.wait_for_timeout(2000)
    page.mouse.wheel(0, 3000)
    page.wait_for_timeout(3000)