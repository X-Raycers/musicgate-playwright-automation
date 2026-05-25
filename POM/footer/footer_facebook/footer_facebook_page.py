from pages.common.base_page import BasePage


class FooterFacebookPage(BasePage):

    def scroll_to_footer(self):
        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def footer_is_visible(self):
        return self.page.locator(".site-footer")

    def facebook_link(self):
        return self.page.locator(
            'a[href="https://www.facebook.com/musicgateisrael"]'
        )

    def facebook_icon(self):
        return self.page.locator(
            'i.fa.fa-facebook-f'
        )