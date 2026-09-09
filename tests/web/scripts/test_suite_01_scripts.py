import pytest
from playwright.sync_api import Page
from pageObjects.web.loginPage import LoginPage
from pageObjects.web.dashboardPage import DashboardPage
from pageObjects.web.cartPage import CartPage


class TestSuite01:
    """Test Suite 01 - E2E Shopping Flow"""

    def test_shopping_flow(self, page: Page):
        """Test case for complete shopping flow from login to checkout"""
        
        # Initialize page objects
        loginPage = LoginPage(page)
        dashboardPage = DashboardPage(page)
        cartPage = CartPage(page)
        
        # Navigate to the application
        loginPage.go_to()
        
        # Perform valid login with username and password
        loginPage.valid_login()
        
        # Search for product and add to cart
        dashboardPage.search_product_add_cart()
        
        # Navigate to cart
        dashboardPage.navigate_to_cart()
        
        # Verify product is displayed in cart
        cartPage.verify_product_is_displayed()
        
        # Click checkout button
        cartPage.click_checkout()
