import pytest
from pageObjects.web.LoginPage import LoginPage
from pageObjects.web.Support import Support


class TestSuite03Scripts:
    """Test Suite 03 Scripts"""

    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Setup fixture for test initialization"""
        self.loginPage = LoginPage(page)
        self.support = Support(page)
        yield

    def test_contact_support_submission(self, page):
        """Test contact support submission workflow"""
        # Navigate to the login page
        self.loginPage.go_to()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
        
        # Scroll to footer
        self.support.scroll_to_footer()
        
        # Click Contact Us or Support link
        self.support.click_contact_us_link()
        
        # Assert support portal is visible
        self.support.assert_support_portal_visible()
        
        # Input subject text
        self.support.input_subject()
        
        # Input message text
        self.support.input_message()
        
        # Click Submit button
        self.support.click_submit_button()
        
        # Locate success confirmation message element
        self.support.locate_success_message()
        
        # Wait for success confirmation message to be visible
        self.support.wait_for_success_message()
        
        # Assert success confirmation message is visible
        self.support.assert_success_message_visible()