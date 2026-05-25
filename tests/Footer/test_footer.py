import allure
from playwright.sync_api import Page, expect


@allure.title("Footer logo redirects to homepage")
def test_footer_logo_redirects_to_homepage(page: Page):
    page.goto("https://musicgate.co.il/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-%d7%9e%d7%a2%d7%a5-7-6-fleet-flt-105f")
    expect(page.locator('a[href="https://musicgate.co.il/"] img.site-logo')).to_be_visible()
    page.locator('a[href="https://musicgate.co.il/"] img.site-logo').click()
    expect(page).to_have_url("https://musicgate.co.il/")


@allure.title("Footer login link redirects correctly")
def test_footer_login_link(page: Page):
    page.goto("https://musicgate.co.il/")
    expect(page.locator('a#menu-extra-login')).to_be_visible()
    page.locator('a#menu-extra-login').click()
    expect(page).to_have_url("https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97")


@allure.title("Footer map page redirects correctly")
def test_footer_map_page(page: Page):
    page.goto("https://musicgate.co.il/")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(page.locator(".site-footer")).to_be_visible()
    page.locator('a[href="https://musicgate.co.il/%d7%9e%d7%a4%d7%aa-%d7%94%d7%92%d7%a2%d7%94-%d7%9e%d7%99%d7%95%d7%96%d7%99%d7%a7-%d7%92%d7%99%d7%99%d7%98"]').click()
    expect(page).to_have_url("https://musicgate.co.il/%d7%9e%d7%a4%d7%aa-%d7%94%d7%92%d7%a2%d7%94-%d7%9e%d7%99%d7%95%d7%96%d7%99%d7%a7-%d7%92%d7%99%d7%99%d7%98")


@allure.title("Footer gallery page redirects correctly")
def test_footer_gallery_page(page: Page):
    page.goto("https://musicgate.co.il/")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(page.locator(".site-footer")).to_be_visible()
    page.locator('a[href="https://musicgate.co.il/%d7%92%d7%9c%d7%a8%d7%99%d7%99%d7%aa-%d7%aa%d7%9e%d7%95%d7%a0%d7%95%d7%aa"]').click()
    expect(page).to_have_url("https://musicgate.co.il/%d7%92%d7%9c%d7%a8%d7%99%d7%99%d7%aa-%d7%aa%d7%9e%d7%95%d7%a0%d7%95%d7%aa")


@allure.title("Footer about us page redirects correctly")
def test_footer_about_us_page(page: Page):
    page.goto("https://musicgate.co.il/")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(page.locator(".site-footer")).to_be_visible()
    page.locator('a[href="https://musicgate.co.il/about-us"]').click()
    expect(page).to_have_url("https://musicgate.co.il/about-us")


@allure.title("Footer terms page redirects correctly")
def test_footer_terms_page(page: Page):
    page.goto("https://musicgate.co.il/")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(page.locator(".site-footer")).to_be_visible()
    expect(page.locator('a[rel="privacy-policy"][href="https://musicgate.co.il/%d7%aa%d7%a7%d7%a0%d7%95%d7%9f-%d7%9e%d7%99%d7%95%d7%96%d7%99-%d7%92%d7%99%d7%99%d7%98"]')).to_be_visible()
    page.locator('a[rel="privacy-policy"][href="https://musicgate.co.il/%d7%aa%d7%a7%d7%a0%d7%95%d7%9f-%d7%9e%d7%99%d7%95%d7%96%d7%99-%d7%92%d7%99%d7%99%d7%98"]').click()
    expect(page).to_have_url("https://musicgate.co.il/%d7%aa%d7%a7%d7%a0%d7%95%d7%9f-%d7%9e%d7%99%d7%95%d7%96%d7%99-%d7%92%d7%99%d7%99%d7%98")


@allure.title("Footer Instagram link redirects correctly")
def test_footer_instagram_redirect(page: Page):
    page.goto("https://musicgate.co.il/")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(page.locator(".site-footer")).to_be_visible()
    expect(page.locator('a[href="https://www.instagram.com/musicgate_israel"]')
    ).to_be_visible()
    with page.expect_popup() as popup_info:page.locator('a[href="https://www.instagram.com/musicgate_israel"]').click()
    instagram_page = popup_info.value
    expect(instagram_page).to_have_url(
    "https://www.instagram.com/musicgate_israel/")


@allure.title("Footer Facebook link is visible")
def test_footer_facebook_link(page: Page):
    page.goto("https://musicgate.co.il/")
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    expect(page.locator(".site-footer")).to_be_visible()
    expect(page.locator('a[href="https://www.facebook.com/musicgateisrael"]')).to_be_visible()
    expect(page.locator('i.fa.fa-facebook-f')).to_be_visible()
    expect(page.locator('a[href="https://www.facebook.com/musicgateisrael"]')).to_have_attribute("target","_blank")







