import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.cart_page import CartPage
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_suite_01_scripts(page, request):
    # TestRail ID: C100
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    # Initialize Page Objects directly in the test
    loginPage = LoginPage(page, scenario)
    dashboardPage = DashboardPage(page, scenario)
    cartPage = CartPage(page, scenario)
    
    # Navigate to the application
    loginPage.go_to()
    
    # Login with valid credentials
    loginPage.valid_login(test_data["username"], test_data["password"])
    
    # Search for product and add to cart
    dashboardPage.search_product_add_cart("Zara Coat 3")
    
    # Navigate to cart
    dashboardPage.navigate_to_cart()
    
    # Verify product is displayed in cart
    cartPage.verify_product_is_displayed("Zara Coat 3")
    
    # Assert product is visible in cart
    product_in_cart = page.locator("text=Zara Coat 3")
    assert product_in_cart.is_visible(), "Product 'Zara Coat 3' should be visible in the cart"
    
    # Click checkout button
    cartPage.click_checkout()
    
    # Assert checkout page is loaded
    checkout_indicator = page.locator(".payment__title")
    assert checkout_indicator.is_visible(), "Checkout page should be loaded successfully"
