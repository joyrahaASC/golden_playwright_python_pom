import pytest
from playwright.sync_api import Page
from pageObjects.web.LoginPage import LoginPage
from pageObjects.web.DashboardPage import DashboardPage
from pageObjects.web.CartPage import CartPage


class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        self.cartPage = CartPage(page)

    def test_checkout(self, page: Page):
        # Navigate to e-commerce application URL
        self.loginPage.go_to()
        
        # Input username, Input password, Click Sign In button
        self.loginPage.valid_login()
        
        # Search product and Click Add To Cart button for product
        self.dashboardPage.search_product_add_cart()
        
        # Click cart icon and Navigate to Cart page
        self.dashboardPage.navigate_to_cart()
        
        # Assert selected product is displayed in cart
        self.cartPage.verify_product_is_displayed()
        
        # Click Checkout button
        self.cartPage.click_checkout()
