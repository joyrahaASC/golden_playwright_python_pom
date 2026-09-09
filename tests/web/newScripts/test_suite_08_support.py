import pytest
from pageObjects.web.LoginPage import LoginPage
from pageObjects.web.CommonPage import CommonPage


class TestSuite08Support:
    """Test suite for support portal functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Setup method to initialize page objects"""
        self.loginPage = LoginPage(page)
        self.commonPage = CommonPage(page)
        yield

    def test_support_portal_submission(self, page):
        """Test case to verify support portal submission workflow"""
        # Navigate to the application
        self.loginPage.go_to()
        
        # Load test data from JSON file
        self.loginPage.load_test_data()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
        
        # Scroll to footer
        self.commonPage.scroll_to_footer()
        
        # Click Contact Us or Support link
        self.commonPage.click_contact_support_link()
        
        # Assert Support Portal is visible
        self.commonPage.verify_support_portal_visible()
        
        # Input Subject text
        self.commonPage.input_subject()
        
        # Input Message text
        self.commonPage.input_message()
        
        # Click Submit button
        self.commonPage.click_submit_button()
        
        # Locate confirmation message element
        self.commonPage.locate_confirmation_message()
        
        # Wait for confirmation message to be visible
        self.commonPage.wait_for_confirmation_message_visible()
        
        # Assert confirmation message is visible
        self.commonPage.verify_confirmation_message_visible()