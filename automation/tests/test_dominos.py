import logging

from automation.modules.cart_page import CartPage
from automation.modules.home_page import HomePage
from automation.modules.menu_page import MenuPage


def test_dominos_order(launch_browser):
    page = launch_browser
    home_page = HomePage(page)
    menu_page = MenuPage(page)
    cart_page = CartPage(page)

    logging.info("Choosing the location...")
    home_page.choose_location()
    
    logging.info("Adding veg pizza to cart and validating subtotal...")
    subtotal, product_prices = menu_page.add_veg_pizza_to_cart_and_validate_subtotal()

    logging.info("Adding beverages to cart and validating subtotal...")
    subtotals, prices = menu_page.add_beverages_to_cart_and_validate_subtotal(subtotal)

    logging.info("Removing products from the cart...")
    cart_subtotal, beverage_subtotal = menu_page.remove_products(subtotals, product_prices, prices)

    logging.info("Proceeding to checkout...")
    cart_page.checkout(cart_subtotal, beverage_subtotal)
    logging.info("Test completed successfully.")
