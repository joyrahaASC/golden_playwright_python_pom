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

def test_suite_01_scripts(page, request):
    # TestRail ID: C101
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    loginPage = LoginPage(page, scenario)
    dashboardPage = DashboardPage(page, scenario)
    
    loginPage.go_to()
    loginPage.valid_login(test_data["username"], test_data["password"])

    dashboardPage.locate_profile_name_element()
    dashboardPage.assert_user_profile_name_visible()
    dashboardPage.search_product_add_cart("Zara Coat 3")
    dashboardPage.navigate_to_cart()
