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
        self.locators = load_locator("dashboard_locators.json")

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

    def verify_user_profile_name_visible(self):
        user_profile_name_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_name_element.wait_for(state="visible")
        expect(user_profile_name_element).to_be_visible()
        if user_profile_name_element.is_visible():
            return True
        else:
            raise AssertionError("User profile name element is not visible in dashboard header")

    def assert_user_profile_name_visible(self):
        user_profile_name_element = self.page.locator(self.locators["user_profile_name"])
        user_profile_name_element.wait_for(state="visible")
        expect(user_profile_name_element).to_be_visible()

    def get_profile_name_element(self):
        """Locate and return the profile name element in the dashboard header.
        
        This method retrieves the profile name element using the 'profile_name' locator key
        from the locators dictionary and returns the element object for further interactions.
        
        Returns:
            Locator: The profile name element locator object.
        """
        profile_name_locator = self.locators["profile_name"]
        return self.page.locator(profile_name_locator)

    def wait_for_profile_name_visible(self, timeout=10):
        """Wait for the profile name element to become visible with a configurable timeout.
        
        This method implements an explicit wait for the profile name element to be displayed
        in the dashboard header. It uses Playwright's wait_for() method with a visible state.
        
        Args:
            timeout (int): Maximum time to wait in seconds (default: 10).
        
        Returns:
            bool: True if the element becomes visible within the timeout, False otherwise.
        """
        try:
            profile_name_locator = self.locators["profile_name"]
            profile_name_element = self.page.locator(profile_name_locator)
            profile_name_element.wait_for(state="visible", timeout=timeout*1000)
            return True
        except TimeoutError:
            return False

    def verify_profile_name(self, expected_name):
        """Verify that the profile name text matches the expected value.
        
        This method retrieves the text content from the profile name element and asserts
        that it equals the expected name parameter. Raises an AssertionError with a
        descriptive message if the values do not match.
        
        Args:
            expected_name (str): The expected profile name text to verify against.
        
        Raises:
            AssertionError: If the actual profile name does not match the expected name.
        """
        profile_name_locator = self.locators["profile_name"]
        profile_name_element = self.page.locator(profile_name_locator)
        profile_name_element.wait_for(state="visible")
        actual_name = profile_name_element.inner_text().strip()
        assert actual_name == expected_name, f"Profile name mismatch: expected '{expected_name}', but got '{actual_name}'"

    def get_header_profile_name(self):
        """Get the profile name text from the dashboard header.
        
        This method locates the header profile name element, waits for it to be visible,
        and retrieves its text content. The method returns the profile name as a string.
        
        Returns:
            str: The profile name text displayed in the dashboard header.
        """
        header_profile_name_element = self.page.locator(self.locators["header_profile_name"])
        header_profile_name_element.wait_for(state="visible")
        profile_name_text = header_profile_name_element.inner_text()
        return profile_name_text

    def verify_header_profile_name_visible(self):
        """Verify that the header profile name element is visible in the dashboard.
        
        This method locates the header profile name element, waits for it to become visible,
        and asserts its visibility using Playwright's expect assertion. Returns True if the
        element is visible, otherwise raises an AssertionError.
        
        Returns:
            bool: True if the header profile name element is visible.
        
        Raises:
            AssertionError: If the header profile name element is not visible.
        """
        header_profile_name_element = self.page.locator(self.locators["header_profile_name"])
        header_profile_name_element.wait_for(state="visible")
        expect(header_profile_name_element).to_be_visible()
        if header_profile_name_element.is_visible():
            return True
        else:
            raise AssertionError("Header profile name element is not visible in dashboard header")
