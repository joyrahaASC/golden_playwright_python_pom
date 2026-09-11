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

    def get_user_profile_name(self):
        """Locate and return the user profile name from the dashboard header.
        
        This method waits for the user profile name element to be visible,
        locates it using the configured locator, and returns its text content
        for assertion purposes.
        
        Returns:
            str: The text content of the user profile name element.
        """
        self.page.locator(self.locators["user_profile_name"]).wait_for(state="visible")
        profile_element = self.page.locator(self.locators["user_profile_name"])
        return profile_element.inner_text()

    def verify_user_profile_visible(self, expected_username):
        """Verify that the user profile name is visible and matches the expected username.
        
        This method waits for the user profile name element to be visible in the
        dashboard header top right section, asserts its visibility, retrieves its
        text content, and validates it against the expected username parameter.
        
        Args:
            expected_username (str): The expected username to validate against.
        
        Returns:
            bool: True if the element is visible and text matches expected_username,
                  False otherwise.
        """
        self.page.locator(self.locators["user_profile_name"]).wait_for(state="visible")
        profile_element = self.page.locator(self.locators["user_profile_name"])
        expect(profile_element).to_be_visible()
        actual_username = profile_element.inner_text()
        return actual_username == expected_username
