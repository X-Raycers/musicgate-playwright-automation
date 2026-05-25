from pages.common.base_page import BasePage


class FooterLoginPage(BasePage):

    def click_footer_login(self):
        self.page.locator(
            'a#menu-extra-login'
        ).click()