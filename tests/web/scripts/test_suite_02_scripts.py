import pytest
from playwright.sync_api import Page
from pageObjects.web.loginPage import LoginPage
from pageObjects.web.dashboardPage import DashboardPage


class TestSuite02Scripts:
    """Test Suite 02 Scripts"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture for test initialization"""
        self.page = page
        self.loginPage = LoginPage(self.page)
        self.dashboardPage = DashboardPage(self.page)

    def test_suite_02_scripts(self):
        """Test case for suite 02 scripts"""
        # Navigate to the login page
        self.loginPage.go_to()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
        
        # Assert user profile name is visible in dashboard header
        self.dashboardPage.verify_user_profile_name_visible()
        
        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()
        
        # Navigate to cart page
        self.dashboardPage.navigate_to_cart()
