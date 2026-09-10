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
        waits for it to be visible, and returns its text content.
        
        Returns:
            str: The text content of the user profile name element.
        """
        user_profile_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_element.wait_for(state="visible")
        return user_profile_element.inner_text()

    def assert_user_profile_name_visible(self):
        """Assert user profile name is visible in dashboard header.
        
        Verifies that the user profile name element is displayed in the
        dashboard header by waiting for visibility and asserting its state.
        Raises an assertion error if the element is not visible.
        """
        user_profile_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_element.wait_for(state="visible")
        expect(user_profile_element).to_be_visible()

    def wait_for_success_message(self):
        """Wait for confirmation message to be visible.
        
        Waits for the success/confirmation message element to become visible
        on the dashboard after login using explicit wait with appropriate timeout.
        """
        success_message_element = self.page.locator(self.locators["success_message"])
        success_message_element.wait_for(state="visible")

    def assert_success_message_visible(self):
        """Assert confirmation message is visible.
        
        Asserts that the success/confirmation message element is visible on the page.
        Waits for the element to be visible and then performs an assertion.
        Raises an assertion error if the element is not visible.
        """
        success_message_element = self.page.locator(self.locators["success_message"])
        success_message_element.wait_for(state="visible")
        expect(success_message_element).to_be_visible()
