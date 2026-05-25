from pages.common.base_page import BasePage


class CartPage(BasePage):

    def open_bongos_product_page(self):
        self.page.goto(
            "https://musicgate.co.il/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-%d7%9e%d7%a2%d7%a5-7-6-fleet-flt-105f"
        )

    def open_guitar_product_page(self):
        self.page.goto(
            "https://musicgate.co.il/product/%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%97%d7%a9%d7%9e%d7%9c%d7%99%d7%aa-%d7%90%d7%93%d7%95%d7%9e%d7%94-cort-x-200-crd-hsh"
        )

    def bongos_product_title(self):
        return self.page.locator(
            "h1.product_title.entry-title"
        )

    def add_bongos_to_cart(self):
        self.page.locator(
            'form.cart button[name="add-to-cart"][value="57380"]'
        ).click()

    def add_guitar_to_cart(self):
        self.page.locator(
            'form.cart button[name="add-to-cart"][value="93977"]'
        ).click()

    def open_cart(self):
        self.page.goto(
            "https://musicgate.co.il/cart"
        )

    def reload_page(self):
        self.page.reload()

    def remove_product_from_cart(self):
        self.page.locator(
            'td.product-remove a[href*="remove_item"]'
        ).click()

    def increase_quantity(self):
        self.page.locator(
            'div.qty-box span.increase.icon_plus'
        ).click()

    def decrease_quantity(self):
        self.page.locator(
            'div.qty-box span.decrease.icon_minus-06'
        ).click()

    def quantity_input(self):
        return self.page.locator(
            'input.input-text.qty.text'
        )

    def cart_counter(self):
        return self.page.locator(
            'a#icon-cart-contents span.mini-item-counter.mf-background-primary'
        )