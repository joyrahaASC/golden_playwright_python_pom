import pytest
from playwright.sync_api import Page
from pageObjects.web.LoginPage import LoginPage
from pageObjects.web.DashboardPage import DashboardPage


class TestSuite07BProfile:
    """Test suite for profile and cart operations"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture to initialize page objects"""
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        yield

    def test_profile_and_cart_workflow(self, page: Page):
        """Test profile name retrieval and cart operations"""
        # Navigate to the login page
        self.loginPage.go_to()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
        
        # Get dashboard header profile name
        self.dashboardPage.get_header_profile_name()
        
        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()
        
        # Navigate to the cart page
        self.dashboardPage.navigate_to_cart()
