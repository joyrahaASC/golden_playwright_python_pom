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

    def verify_user_profile_name_visible(self, expected_name):
        """Verify user profile name is visible in dashboard header.
        
        Waits for the dashboard header to load, locates the user profile name element,
        verifies it is visible, and validates that the displayed name matches the expected name.
        
        Args:
            expected_name (str): The expected user profile name to validate against.
            
        Returns:
            bool: True if the user profile name is visible and matches the expected name.
            
        Raises:
            AssertionError: If the user profile name is not visible or does not match expected_name.
        """
        self.page.locator(self.locators["dashboard_header"]).wait_for(state="visible")
        user_profile_name_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_name_element.wait_for(state="visible")
        expect(user_profile_name_element).to_be_visible()
        actual_name = user_profile_name_element.inner_text()
        assert actual_name == expected_name, f"Expected name '{expected_name}' but got '{actual_name}'"
        return True
