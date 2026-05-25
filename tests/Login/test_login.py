import allure
from playwright.sync_api import Page, expect

@allure.title("Open login page")
def test_open_login_page(page: Page):
    page.goto("https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97")
    page.locator("#menu-extra-login").click()
    expect(page.locator(".login-text")).to_contain_text("התחברות")
    expect( page.locator("#username")).to_be_visible()


@allure.title("Login with empty fields")
def test_login_empty_fields(page: Page):
    page.goto("https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97")
    page.locator("#menu-extra-login").click()
    page.locator('button[name="login"]').click()
    expect(page.locator("#username")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()


@allure.title("Invalid password login test")
def test_invalid_password(page: Page):
    page.goto("https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97")
    page.locator("#menu-extra-login").click()
    page.locator("#password").fill("wrongpassword")
    page.locator('button[name="login"]').click()
    expect( page.locator("#password")).to_be_visible()


@allure.title("Invalid email login test")
def test_invalid_email(page: Page):
    page.goto("https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97")
    page.locator("#menu-extra-login").click()
    page.locator("#username").fill("wrongemail@gmail.com")
    page.locator('button[name="login"]').click()
    expect(page.locator("#username")).to_be_visible()


@allure.title("Remember me checkbox test")
def test_remember_me_checkbox(page: Page):
    page.goto("https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97")
    page.locator("#menu-extra-login").click()
    page.locator("label.woocommerce-form-login__rememberme").click()
    expect(page.locator("#rememberme")).to_be_checked()


@allure.title("Show password button test")
def test_show_password_button(page: Page):
    page.goto("https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97")
    page.locator("#menu-extra-login").click()
    page.locator("#password").fill("fakepassword123")
    page.locator('button.show-password-input[aria-describedby="password"]').click()
    expect( page.locator("#password")).to_have_attribute("type", "text")