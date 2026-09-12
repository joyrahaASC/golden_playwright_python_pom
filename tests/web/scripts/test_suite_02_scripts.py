import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_suite_02_scripts(page, request):
    # TestRail ID: C101
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    loginPage = LoginPage(page, scenario)
    dashboardPage = DashboardPage(page, scenario)
    
    # Navigate to the application
    loginPage.go_to()
    
    # Load test data from JSON file
    test_data = load_test_data()
    
    # Perform valid login with username and password
    loginPage.valid_login(test_data["username"], test_data["password"])
    
    # Get user profile name from dashboard header
    user_profile_name = dashboardPage.get_user_profile_name()
    
    # Assert user profile name is visible in dashboard header
    dashboardPage.verify_user_profile_name_visible()
    assert user_profile_name is not None, "User profile name should be visible in dashboard header"
    
    # Search for product and add to cart
    dashboardPage.search_product_add_cart("Zara Coat 3")
    
    # Navigate to the cart page
    dashboardPage.navigate_to_cart()
    
    # Assert navigation to cart was successful
    cart_heading = page.locator("h1:has-text('My Cart')")
    assert cart_heading.is_visible(), "Cart page should be displayed after navigation"
