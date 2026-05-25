import allure
from playwright.sync_api import Page, expect


@allure.title("Add product to cart")
def test_add_product_to_cart(page: Page):
    page.goto("https://musicgate.co.il/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-%d7%9e%d7%a2%d7%a5-7-6-fleet-flt-105f")
    expect(page.locator("h1.product_title.entry-title")).to_contain_text('בונגוס מעץ "7 + "6 FLEET FLT-105F')
    page.locator('form.cart button[name="add-to-cart"][value="57380"]').click()
    page.reload()
    page.goto("https://musicgate.co.il/cart")


@allure.title("Remove product from cart")
def test_remove_product_from_cart(page: Page):
    page.goto("https://musicgate.co.il/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-%d7%9e%d7%a2%d7%a5-7-6-fleet-flt-105f")
    expect(page.locator("h1.product_title.entry-title")).to_contain_text('בונגוס מעץ "7 + "6 FLEET FLT-105F')
    page.locator('form.cart button[name="add-to-cart"][value="57380"]').click()
    page.goto("https://musicgate.co.il/cart")
    page.locator('td.product-remove a[href*="remove_item"]').click()


@allure.title("Increase product quantity")
def test_increase_product_quantity(page: Page):
    page.goto("https://musicgate.co.il/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-%d7%9e%d7%a2%d7%a5-7-6-fleet-flt-105f")
    expect(page.locator("h1.product_title.entry-title")).to_contain_text('בונגוס מעץ "7 + "6 FLEET FLT-105F')
    page.locator('form.cart button[name="add-to-cart"][value="57380"]').click()
    page.goto("https://musicgate.co.il/cart")
    page.locator('div.qty-box span.increase.icon_plus').click()
    expect(page.locator('input.input-text.qty.text')).to_have_value("2")


@allure.title("Decrease product quantity")
def test_decrease_product_quantity(page: Page):
    page.goto("https://musicgate.co.il/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-%d7%9e%d7%a2%d7%a5-7-6-fleet-flt-105f")
    expect(page.locator("h1.product_title.entry-title")).to_contain_text('בונגוס מעץ "7 + "6 FLEET FLT-105F')
    page.locator('form.cart button[name="add-to-cart"][value="57380"]').click()
    page.goto("https://musicgate.co.il/cart")
    page.locator('div.qty-box span.increase.icon_plus').click()
    expect(page.locator('input.input-text.qty.text[value="2"]')).to_have_value("2")
    page.locator('div.qty-box span.decrease.icon_minus-06').click()
    expect(page.locator('input.input-text.qty.text')).to_have_value("1")


@allure.title("Multiple products in cart")
def test_multiple_products_in_cart(page: Page):
    page.goto("https://musicgate.co.il/product/%d7%91%d7%95%d7%a0%d7%92%d7%95%d7%a1-%d7%9e%d7%a2%d7%a5-7-6-fleet-flt-105f")
    expect(page.locator("h1.product_title.entry-title")).to_contain_text('בונגוס מעץ "7 + "6 FLEET FLT-105F')
    page.locator('form.cart button[name="add-to-cart"][value="57380"]').click()
    page.goto("https://musicgate.co.il/product/%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%97%d7%a9%d7%9e%d7%9c%d7%99%d7%aa-%d7%90%d7%93%d7%95%d7%9e%d7%94-cort-x-200-crd-hsh")
    expect(page.locator("h1.product_title.entry-title")).to_contain_text('גיטרה חשמלית אדומה CORT X-200 CRD HSH')
    page.locator('form.cart button[name="add-to-cart"][value="93977"]').click()
    page.goto("https://musicgate.co.il/cart")
    expect(page.locator('a#icon-cart-contents span.mini-item-counter.mf-background-primary')).to_have_text("2")


