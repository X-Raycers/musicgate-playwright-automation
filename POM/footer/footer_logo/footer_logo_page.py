from pages.common.base_page import BasePage


class FooterLogoPage(BasePage):

    def click_footer_logo(self):
        self.page.locator(
            'a[href="https://musicgate.co.il/"] img.site-logo'
        ).click()