import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.support_page import SupportPage
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_submit_support_request(page, request):
    # TestRail ID: C102
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    loginPage = LoginPage(page, scenario)
    dashboardPage = DashboardPage(page, scenario)
    supportPage = SupportPage(page, scenario)
    
    loginPage.go_to()
    loginPage.valid_login(test_data["username"], test_data["password"])

    dashboardPage.scroll_to_footer()
    dashboardPage.click_support_link()
    
    supportPage.navigate_to_support_portal()
    supportPage.input_subject(test_data.get("support_subject", "Test Subject"))
    supportPage.input_message(test_data.get("support_message", "Test Message"))
    supportPage.click_submit_button()
    
    supportPage.locate_confirmation_message()
    supportPage.wait_for_confirmation_message()
    supportPage.verify_confirmation_message_displayed()
