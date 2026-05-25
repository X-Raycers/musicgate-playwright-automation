from pages.common.base_page import BasePage


class FooterInstagramPage(BasePage):

    def scroll_to_footer(self):
        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def footer_is_visible(self):
        return self.page.locator(".site-footer")

    def click_instagram_link(self):
        self.page.locator(
            'a[href="https://www.instagram.com/musicgate_israel"]'
        ).click()