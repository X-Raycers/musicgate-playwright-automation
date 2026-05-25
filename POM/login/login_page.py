from pages.common.base_page import BasePage


class LoginPage(BasePage):

    def open_login_page(self):
        self.page.goto(
            "https://musicgate.co.il/%d7%94%d7%a8%d7%a9%d7%9e%d7%aa%d7%9c%d7%a7%d7%95%d7%97"
        )

    def click_login_button(self):
        self.page.locator(
            "#menu-extra-login"
        ).click()

    def fill_email(self, email):
        self.page.locator(
            "#username"
        ).fill(email)

    def fill_password(self, password):
        self.page.locator(
            "#password"
        ).fill(password)

    def submit_login(self):
        self.page.locator(
            'button[name="login"]'
        ).click()

    def click_remember_me_checkbox(self):
        self.page.locator(
            "label.woocommerce-form-login__rememberme"
        ).click()

    def click_show_password_button(self):
        self.page.locator(
            'button.show-password-input[aria-describedby="password"]'
        ).click()

    def username_field(self):
        return self.page.locator("#username")

    def password_field(self):
        return self.page.locator("#password")

    def login_text(self):
        return self.page.locator(".login-text")

    def remember_me_checkbox(self):
        return self.page.locator("#rememberme")