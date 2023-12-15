class HomePageLocators:
    ORDER_ONLINE_BUTTON = "//button[text()='ORDER ONLINE NOW']"
    DONT_ALLOW = "//button[@onclick='moeRemoveBanner()']"
    # IFRAME = "//iframe[contains(@id,\"moe-onsite-campaign\")]"
    DELIVERY_ADDRESS = "//input[@placeholder='Enter your delivery address']"
    PINCODE = "//input[@placeholder='Enter Area / Locality']"
    SUGGESTIONS = "//p[text()='Suggestions']/..//ul/li[1]"


    BANNER_CLOSE = "//*[@id=\"close-icon\"]"
    OFFER_BANNER = "//iframe[contains(@id,'moe-onsite-campaign')]"


class MenuPageLocators:
    VEG_PIZZA = "//div[@data-label='Veg Pizza']//child::span[text()='VEG PIZZA']"
    ADD_PRODUCT = "(//div[contains(@data-label,'{}')]//button)[2]/span"
    NO_THANKS = "//span[text()='NO THANKS']"
    PRICES = ("//span[.='{}']//ancestor::div[@class='crt-cnt']//following-sibling::div["
              "@class='crt-cnt-qty-prc']//des        cendant::span[@class='rupee']")
    # PROD_INCREASE = ("(//span[.='{}']//ancestor::div[@class='crt-cnt']//following-sibling::div[\"@class='crt-cnt-qty-prc']//child::div//descendant::div)[4]")
    PROD_INCREASE = "//div[@class='crt-itms']//span[text()='{}']/../../..//div[@data-label='increase']"
    QUANTITY = ("//span[.='{}']//ancestor::div[@class='crt-cnt']//following-sibling::div["
                "@class='crt-cnt-qty-prc']//child::div//descendant::div[1]//span")
    SUBTOTAL = "//span[@data-label='total-minicart']"
    MENU_BEVERAGES = "//span[.='BEVERAGES']"
    BEVERAGE_PRODUCTS = "(//div[@data-label='Beverages'])[2]//div[@data-label='{}']//button/span"
    PROD_DECREASE = ("(//span[.='{}']//ancestor::div[@class='crt-cnt']//following-sibling::div["
                     "@class='crt-cnt-qty-prc']//child::div//descendant::div)[2]")


class CartPageLocator:
    CHECK_OUT = "//button[@data-label=\"miniCartCheckout\"]"
    SUBTOTAL_PLACE_ORDER = "//span[.='Sub Total']/../span/span"
