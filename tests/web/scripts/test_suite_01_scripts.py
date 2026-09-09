import pytest
from playwright.sync_api import Page, expect
from pageObjects.web.loginPage import LoginPage
from pageObjects.web.dashboardPage import DashboardPage
from pageObjects.web.cartPage import CartPage


class TestSuite01:
    """Test Suite 01 - Product Purchase Flow"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture to initialize page objects"""
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        self.cartPage = CartPage(page)
        yield

    def test_product_purchase_flow(self, page: Page):
        """Test case: Navigate, login, search product, add to cart, and verify checkout"""
        # Navigate to the application
        self.loginPage.go_to()
        
        # Login with valid credentials
        self.loginPage.valid_login()
        
        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()
        
        # Navigate to cart
        self.dashboardPage.navigate_to_cart()
        
        # Verify product is displayed in cart
        self.cartPage.verify_product_is_displayed()
        
        # Click checkout button
        self.cartPage.click_checkout()
        
        # Explicit assertion to verify checkout page or state
        expect(page).to_have_url("**/checkout", timeout=5000)