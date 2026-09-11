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
        """Get user profile name from dashboard header.
        
        Locates the user profile name element in the dashboard header,
        waits for it to be visible, and extracts the text content.
        
        Returns:
            str: The text content of the user profile name element.
        """
        user_profile_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_element.wait_for(state="visible")
        return user_profile_element.inner_text()

    def verify_user_profile_name_displayed(self, expected_name):
        """Assert user profile name matches expected value.
        
        Locates the user profile name element in the dashboard header,
        waits for it to be visible, retrieves the displayed text, and
        asserts that it matches the expected_name parameter.
        
        Args:
            expected_name (str): The expected user profile name to verify.
        
        Raises:
            AssertionError: If the displayed name does not match expected_name
                          or if the element is not visible.
        """
        user_profile_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_element.wait_for(state="visible")
        expect(user_profile_element).to_be_visible()
        expect(user_profile_element).to_have_text(expected_name)
