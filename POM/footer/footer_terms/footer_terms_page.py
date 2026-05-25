from pages.common.base_page import BasePage


class FooterTermsPage(BasePage):

    def scroll_to_footer(self):
        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def footer_is_visible(self):
        return self.page.locator(".site-footer")

    def click_footer_terms_page(self):
        self.page.locator(
            'a[rel="privacy-policy"][href="https://musicgate.co.il/%d7%aa%d7%a7%d7%a0%d7%95%d7%9f-%d7%9e%d7%99%d7%95%d7%96%d7%99-%d7%92%d7%99%d7%99%d7%98"]'
        ).click()