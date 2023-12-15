import logging
from automation.locators.locators import HomePageLocators
from automation.data_strings.datas import TestData


class HomePage:
    def __init__(self, page):
        self.page = page

    def choose_location(self):
        """
        Perform actions to choose the delivery location.
        """
        page = self.page
        logging.info("Clicking online order button")
        order_online = page.locator('xpath=' + HomePageLocators.ORDER_ONLINE_BUTTON)
        order_online.click()

        # Enter the pincode
        delivery_address_input = page.locator(HomePageLocators.DELIVERY_ADDRESS)
        delivery_address_input.click()
        logging.info("Entering Pincode")
        page.locator(HomePageLocators.PINCODE).type(TestData.pincode)
        page.locator(HomePageLocators.SUGGESTIONS).click()

        try:
            with page.expect_popup() as popup_info:
                with page.frame(name=HomePageLocators.OFFER_BANNER):
                    banner_close = page.locator('xpath=' + HomePageLocators.BANNER_CLOSE)
                    banner_close.click()
                    logging.info("Closing Banner")

                popup_info.value.close()
        except Exception as e:
            logging.info("Banner not displayed")

        # Click the "Don't Allow" button if present (for location access)
        try:
            dont_allow_button = page.locator(HomePageLocators.DONT_ALLOW)
            dont_allow_button.click()
        except TimeoutError:
            logging.info("Location access not required")

        # Click the suggestions element (if available)
        suggestions_element = page.locator(HomePageLocators.SUGGESTIONS)
        if suggestions_element.is_visible():
            suggestions_element.click()
