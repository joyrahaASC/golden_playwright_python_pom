import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.support import Support
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_suite_03_scripts(page, request):
    # TestRail ID: C102
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    # Initialize Page Objects directly in the test
    loginPage = LoginPage(page, scenario)
    dashboardPage = DashboardPage(page, scenario)
    support = Support(page, scenario)
    
    loginPage.go_to()
    loginPage.valid_login(test_data["username"], test_data["password"])

    dashboardPage.scroll_to_footer_support_link()
    dashboardPage.click_footer_support_link()

    support.verify_support_portal_loaded()
    support.input_subject("Test Subject")
    support.input_message("This is a test message for support.")
    support.click_submit_button()
    support.wait_for_confirmation_message()
