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
    
    loginPage = LoginPage(page, scenario)
    dashboardPage = DashboardPage(page, scenario)
    cartPage = CartPage(page, scenario)
    
    loginPage.go_to()
    loginPage.valid_login(test_data["username"], test_data["password"])

    dashboardPage.search_product_add_cart("Zara Coat 3")
    dashboardPage.navigate_to_cart()

    cartPage.verify_product_is_displayed("Zara Coat 3")
    
    # Explicit assertion to verify product is displayed in cart
    product_locator = page.locator("h3:has-text('Zara Coat 3')")
    assert product_locator.is_visible(), "Product 'Zara Coat 3' should be visible in the cart"
    
    cartPage.click_checkout()
    
    # Verify checkout button was clicked and navigation occurred
    page.wait_for_load_state("networkidle")
    assert "review" in page.url or "checkout" in page.url, "Should navigate to checkout/review page after clicking checkout"
