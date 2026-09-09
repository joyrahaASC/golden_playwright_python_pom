import pytest
from pageObjects.web.loginPage import LoginPage
from pageObjects.web.dashboardPage import DashboardPage
from pageObjects.web.cartPage import CartPage


class TestSuite01:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        self.cartPage = CartPage(page)
    
    def test_case_c100(self, page):
        """Test case for C100: Navigate, login, search product, add to cart, and verify"""
        
        # Navigate to the application
        self.loginPage.go_to()
        
        # Perform valid login with username and password
        self.loginPage.valid_login()
        
        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()
        
        # Navigate to cart
        self.dashboardPage.navigate_to_cart()
        
        # Verify product is displayed in cart
        self.cartPage.verify_product_is_displayed()
        
        # Click checkout button
        self.cartPage.click_checkout()
