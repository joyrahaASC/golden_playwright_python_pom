import pytest
from playwright.sync_api import Page
from pageObjects.web.loginPage import LoginPage
from pageObjects.web.dashboardPage import DashboardPage
from pageObjects.web.cartPage import CartPage


class TestSuite06Checkout:
    """Test suite for checkout functionality"""

    def test_checkout_flow(self, page: Page):
        """Test the complete checkout flow from login to checkout"""
        
        # Initialize page objects
        loginPage = LoginPage(page)
        dashboardPage = DashboardPage(page)
        cartPage = CartPage(page)
        
        # Navigate to the application
        loginPage.go_to()
        
        # Login with valid credentials
        loginPage.valid_login()
        
        # Search for product and add to cart
        dashboardPage.search_product_add_cart()
        
        # Navigate to the cart page
        dashboardPage.navigate_to_cart()
        
        # Verify the product is displayed in cart
        cartPage.verify_product_is_displayed()
        
        # Click checkout button
        cartPage.click_checkout()
