from pages.common.base_page import BasePage


class FooterGalleryPage(BasePage):

    def scroll_to_footer(self):
        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight)"
        )

    def footer_is_visible(self):
        return self.page.locator(".site-footer")

    def click_footer_gallery_page(self):
        self.page.locator(
            'a[href="https://musicgate.co.il/%d7%92%d7%9c%d7%a8%d7%99%d7%99%d7%aa-%d7%aa%d7%9e%d7%95%d7%a0%d7%95%d7%aa"]'
        ).click()