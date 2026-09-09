import pytest
from playwright.sync_api import Page
from pageObjects.web.loginPage import LoginPage
from pageObjects.web.dashboardPage import DashboardPage
from pageObjects.web.cartPage import CartPage


class TestSuite01Scripts:
    """Test Suite 01 Scripts"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture for test initialization"""
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        self.cartPage = CartPage(page)

    def test_suite_01_scripts(self, page: Page):
        """Test case for suite 01 scripts"""
        # Navigate to the login page
        self.loginPage.go_to()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
        
        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()
        
        # Navigate to the cart page
        self.dashboardPage.navigate_to_cart()
        
        # Verify the product is displayed in cart
        self.cartPage.verify_product_is_displayed()
        
        # Click checkout button
        self.cartPage.click_checkout()