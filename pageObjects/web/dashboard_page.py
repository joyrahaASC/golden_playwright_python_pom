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

    def get_profile_name_element(self):
        """Locate and return the profile name element in the dashboard header.
        
        This method waits for the profile name element to be visible and returns
        the element object for further operations like reading text or assertions.
        
        Returns:
            Locator: The Playwright locator object for the profile name element.
        """
        profile_name_locator = self.page.locator(self.locators["profile_name"])
        profile_name_locator.wait_for(state="visible")
        return profile_name_locator

    def get_profile_name_text(self):
        """Retrieve and return the text content of the profile name element.
        
        This method waits for the profile name element to be visible in the
        dashboard header, extracts the text content, and returns it as a string.
        
        Returns:
            str: The text content of the profile name element.
        """
        profile_name_locator = self.page.locator(self.locators["profile_name"])
        profile_name_locator.wait_for(state="visible")
        return profile_name_locator.inner_text()

    def verify_profile_name(self, expected_name):
        """Verify that the displayed profile name matches the expected value.
        
        This method locates the profile name element in the dashboard header,
        extracts its text content, and asserts that it matches the expected_name
        parameter. Optionally captures a screenshot for documentation.
        
        Args:
            expected_name (str): The expected profile name to verify against.
        
        Raises:
            AssertionError: If the displayed profile name does not match the expected value.
        """
        profile_name_locator = self.page.locator(self.locators["profile_name"])
        profile_name_locator.wait_for(state="visible")
        expect(profile_name_locator).to_have_text(expected_name)
        self.page.screenshot(path=f"screenshots/profile_name_verification_{expected_name}.png")
