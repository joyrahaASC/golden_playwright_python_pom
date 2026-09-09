import pytest
from playwright.sync_api import Page
from pageObjects.web.LoginPage import LoginPage
from pageObjects.web.DashboardPage import DashboardPage


class TestSuite07Profile:
    """Test suite for profile verification and cart operations"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup method to initialize page objects"""
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        yield

    def test_profile_and_cart_workflow(self, page: Page):
        """Test to verify user profile and perform cart operations"""
        # Navigate to the login page
        self.loginPage.go_to()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
        
        # Verify user profile name is visible in dashboard header
        self.dashboardPage.verify_user_profile_name_visible()
        
        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()
        
        # Navigate to the cart page
        self.dashboardPage.navigate_to_cart()