import logging
import time
from automation.locators.locators import MenuPageLocators
from automation.data_strings.datas import TestData


class MenuPage:
    def __init__(self, page):
        self.page = page

    def add_veg_pizza_to_cart_and_validate_subtotal(self):
        """
        Add vegetarian pizzas to the cart and validate subtotal.
        Returns:
            tuple: Subtotal and dictionary of product prices.
        """
        page = self.page

        subtotal = 0
        product_prices = {}

        logging.info("Navigating to Veg Pizza")

        for product, quantity in zip(TestData.product_values, TestData.product_quantity):
            logging.info(f"Adding {product} Pizza to Cart")
            add_cart_button = page.locator(MenuPageLocators.ADD_PRODUCT.format(product))
            add_cart_button.click()
            try:
                # Handle the "Extra Cheese" popup
                no_thanks_element = page.locator(MenuPageLocators.NO_THANKS)
                if no_thanks_element.is_visible():
                    logging.info("Extra Cheese popup is displayed and Clicked No thanks Option")
                    no_thanks_element.click()
            except TimeoutError:
                logging.info("Extra Cheese popup not displayed")

            # Get product price and calculate subtotal
            product_price_element = page.locator(MenuPageLocators.PRICES.format(product))
            product_price = float(product_price_element.inner_text().strip('$'))
            product_prices[product] = product_price
            quantity1 = int(quantity)
            for _ in range(quantity1 - 1):
                increase_button = page.locator(MenuPageLocators.PROD_INCREASE.format(product))
                increase_button.click()
            product_quantity = int(page.locator(MenuPageLocators.QUANTITY.format(product)).inner_text())
            product_subtotal = product_price * product_quantity
            subtotal += product_subtotal

        # Get and validate the cart subtotal
        cart_subtotal_element = page.locator(MenuPageLocators.SUBTOTAL)
        cart_subtotal = float(cart_subtotal_element.inner_text().strip('$'))
        assert subtotal == cart_subtotal, f"Expected subtotal: {subtotal}, Actual subtotal: {cart_subtotal}"

        return subtotal, product_prices

    def add_beverages_to_cart_and_validate_subtotal(self, subtotal):
        """
        Add beverages to the cart and validate subtotal.
        Returns:
            tuple: Updated subtotal and price of the added beverage.
        """
        page = self.page

        logging.info("Navigating to Beverages")
        logging.info(f"Adding {TestData.beverage_product} beverage to Cart")

        # Click the beverage product
        beverage_product_element = page.locator(MenuPageLocators.BEVERAGE_PRODUCTS.format(TestData.beverage_product))
        beverage_product_element.click()
        logging.info(f"{TestData.beverage_product } is clicked")

        # Wait for the product to be added and retrieve its price
        price_element = page.locator(MenuPageLocators.PRICES.format(TestData.beverage_product))
        price = float(price_element.inner_text().strip('$'))
        logging.info(f"price of {TestData.beverage_product}"  f"{ price}")

        # Increase beverage quantity (if needed)
        for _ in range(int(TestData.beverage_quantity)):
            increase_button = page.locator(MenuPageLocators.PROD_INCREASE.format(TestData.beverage_product))
            increase_button.click()

        logging.info(f"increased in {TestData.beverage_product} in {TestData.beverage_quantity} times")
        # Calculate product subtotal and update the cart subtotal
        product_quantity = int(page.locator(MenuPageLocators.QUANTITY.format(TestData.beverage_product)).inner_text())
        product_subtotal = price * product_quantity
        subtotal += product_subtotal

        # Get and validate the updated cart subtotal
        cart_subtotal_element = page.locator(MenuPageLocators.SUBTOTAL)
        cart_subtotal = float(cart_subtotal_element.inner_text().strip('$'))
        assert subtotal == cart_subtotal, f"Expected subtotal: {subtotal}, Actual subtotal: {cart_subtotal}"

        return subtotal, price

    def remove_products(self, subtotal, product_prices, prices):
        """
        Remove products from the cart and update subtotal.
        Returns:
            tuple: Updated cart subtotal and product subtotal.
        """
        page = self.page

        logging.info("Reducing veg pizza quantity")

        # Reduce the quantity of veg pizzas as needed
        for product in TestData.product_values:
            if product == "Margherita":
                logging.info(f"Removing {product} Pizza from cart ")
                decrease_button = page.locator(MenuPageLocators.PROD_DECREASE.format(product))
                decrease_button.click()
                product_price = product_prices[product]
                product_quantity = int(page.locator(MenuPageLocators.QUANTITY.format(product)).inner_text())
                product_subtotal = product_price * product_quantity
                subtotal -= product_subtotal

        logging.info(f"Removing {TestData.beverage_product} from cart")

        # Reduce the quantity of the beverage
        for _ in range(6):  # Adjust the number of iterations based on your requirement
            decrease_button = page.locator(MenuPageLocators.PROD_DECREASE.format(TestData.beverage_product))
            decrease_button.click()

        # Calculate the product subtotal for the beverage and update the cart subtotal
        product_quantity = int(page.locator(MenuPageLocators.QUANTITY.format(TestData.beverage_product)).inner_text())
        product_subtotal = prices * product_quantity
        subtotal -= product_subtotal

        # Get and validate the updated cart subtotal
        cart_subtotal_element = page.locator(MenuPageLocators.SUBTOTAL)
        cart_subtotal = float(cart_subtotal_element.inner_text().strip('$'))
        assert subtotal == cart_subtotal, f"Expected subtotal: {subtotal}, Actual subtotal: {cart_subtotal}"

        return cart_subtotal, product_subtotal
