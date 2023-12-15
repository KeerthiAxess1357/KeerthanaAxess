import logging

from automation.locators.locators import CartPageLocator


class CartPage:
    def __init__(self, page):
        self.page = page

    def checkout(self, cart_subtotal, beverage_price_total):
        """
        Perform checkout and validate the total amount.

        Raises:
            AssertionError: If the menu_page total doesn't match the cart_page total.
        """
        page = self.page

        # Navigate to the cart page or use the appropriate URL

        # Perform the checkout action
        checkout_button = page.locator(CartPageLocator.CHECK_OUT)
        checkout_button.click()

        logging.info("validating subtotal")

        # Retrieve and process the subtotal amount
        subtotal_element = page.locator(CartPageLocator.SUBTOTAL_PLACE_ORDER)
        subtotal_text = subtotal_element.inner_text().replace("$", "")
        sub_total_price = round(float(subtotal_text), 1)

        # Calculate the expected beverage price
        discount_beverage_price = beverage_price_total * 0.0477
        actual_beverage_price = round(cart_subtotal - discount_beverage_price, 1)

        # Assert that the actual and expected prices match
        assert actual_beverage_price == sub_total_price
