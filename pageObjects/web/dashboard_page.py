import json
import os
from playwright.sync_api import expect
from .common_page import CommonPage

def load_locator(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    locator_path = os.path.join(base_dir, "locators", "web", filename)
    with open(locator_path) as f:
        return json.load(f)

class DashboardPage(CommonPage):
    def __init__(self, page, scenario):
        super().__init__(page, scenario)
        self.locators = load_locator("dashboard_page.json")

    def search_product_add_cart(self, product_name):
        product = self.page.locator(self.locators["products"], has_text=product_name).first
        product.wait_for(state="visible")
        add_cart_button = product.locator("button", has_text=" Add To Cart")
        expect(add_cart_button).to_be_visible()
        if add_cart_button.is_visible():
            add_cart_button.click()

    def navigate_to_orders(self):
        self.page.locator(self.locators["orders"]).click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_cart(self):
        self.page.locator(self.locators["cart"]).click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_load_state("domcontentloaded")

    def get_dashboard_header_profile_name(self):
        """Locate and return the profile name element displayed in the dashboard header.
        
        This method waits for the profile name element to be present in the DOM and visible,
        then returns the WebElement object for further assertions or text extraction.
        
        Returns:
            Locator: The located dashboard header profile name element object.
        """
        profile_name_element = self.page.locator(self.locators["dashboard_header_profile_name"])
        profile_name_element.wait_for(state="visible")
        return profile_name_element

    def verify_dashboard_header_profile_name_visible(self):
        """Verify that the dashboard header profile name element is visible on the page.
        
        This method locates the profile name element, waits for it to be visible,
        asserts its visibility state, and returns the visibility status.
        
        Returns:
            bool: True if the profile name element is visible, False otherwise.
        """
        profile_name_element = self.page.locator(self.locators["dashboard_header_profile_name"])
        profile_name_element.wait_for(state="visible")
        expect(profile_name_element).to_be_visible()
        return profile_name_element.is_visible()
