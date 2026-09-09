import pytest
from playwright.sync_api import Page
from pageObjects.web.dashboardPage import DashboardPage
from pageObjects.web.loginPage import LoginPage


class TestSuite02Scripts:
    """Test Suite 02 Scripts"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture for test initialization"""
        self.page = page
        self.dashboardPage = DashboardPage(page)
        self.loginPage = LoginPage(page)

    def test_suite_02_scripts(self):
        """Test case for suite 02 scripts"""
        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()
        
        # Navigate to cart
        self.dashboardPage.navigate_to_cart()
        
        # Locate profile name element in dashboard header
        self.dashboardPage.get_profile_name_element()
        
        # Wait for profile name to be visible
        self.dashboardPage.wait_for_profile_name_visible()
        
        # Assert displayed profile name matches expected user name
        self.dashboardPage.verify_profile_name()
        
        # Navigate to the login page
        self.loginPage.go_to()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
