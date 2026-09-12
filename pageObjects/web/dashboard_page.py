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
        waits for it to be visible, and returns its text value.
        
        Returns:
            str: The displayed username or profile name text.
        """
        user_profile_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_element.wait_for(state="visible")
        return user_profile_element.inner_text()

    def verify_user_profile_name_visible(self, expected_name):
        """Assert user profile name is visible in dashboard header.
        
        Verifies that the user profile name element is visible in the dashboard
        header and asserts that it matches the expected name.
        
        Args:
            expected_name (str): The expected username or profile name to verify.
        
        Returns:
            bool: True if all assertions pass.
        
        Raises:
            AssertionError: If the element is not visible or the name doesn't match.
        """
        user_profile_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_element.wait_for(state="visible")
        expect(user_profile_element).to_be_visible()
        actual_name = user_profile_element.inner_text()
        assert actual_name == expected_name, f"Expected profile name '{expected_name}', but got '{actual_name}'"
        return True

    def scroll_to_footer_support_link(self):
        """Scroll to Contact Us or Support link in footer.
        
        Scrolls down to the footer section of the dashboard page and ensures
        the Contact Us or Support link is visible in the viewport.
        """
        footer_support_link_element = self.page.locator(self.locators["footer_support_link"])
        footer_support_link_element.scroll_into_view_if_needed()
        footer_support_link_element.wait_for(state="visible")
        expect(footer_support_link_element).to_be_visible()

    def click_footer_support_link(self):
        """Click Contact Us or Support link in footer.
        
        Locates and clicks the Contact Us or Support link in the footer section
        of the dashboard page. This should navigate to the support portal.
        """
        footer_support_link_element = self.page.locator(self.locators["footer_support_link"])
        footer_support_link_element.wait_for(state="visible")
        expect(footer_support_link_element).to_be_visible()
        footer_support_link_element.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_load_state("domcontentloaded")
