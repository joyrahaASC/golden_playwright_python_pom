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

    def verify_profile_name_visible(self):
        """Verify that the dashboard header profile name element is visible.
        
        This method locates the profile name element in the dashboard header,
        waits for it to be visible, and checks its visibility state.
        
        Returns:
            bool: True if the profile name element is visible, False otherwise.
        """
        profile_name_locator = self.page.locator(self.locators["profile_name"])
        profile_name_locator.wait_for(state="visible")
        return profile_name_locator.is_visible()

    def assert_profile_name(self, expected_name):
        """Assert that the dashboard header profile name matches the expected name.
        
        This method locates the profile name element, waits for it to be visible,
        retrieves its text content, and asserts that it matches the expected name.
        
        Args:
            expected_name (str): The expected profile name text to verify against.
        
        Raises:
            AssertionError: If the actual profile name does not match the expected name.
        """
        profile_name_locator = self.page.locator(self.locators["profile_name"])
        profile_name_locator.wait_for(state="visible")
        actual_name = profile_name_locator.inner_text()
        assert actual_name == expected_name, f"Profile name mismatch: expected '{expected_name}', but got '{actual_name}'"
