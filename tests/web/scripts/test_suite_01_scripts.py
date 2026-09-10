import pytest
import json
import os
from playwright.sync_api import expect

from pageObjects.web.login_page import LoginPage
from pageObjects.web.dashboard_page import DashboardPage
from pageObjects.web.footer_navigation import FooterNavigation
from pageObjects.web.support_portal import SupportPortal
from pageObjects.web.common_scenario import CommonScenario

def load_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    with open(os.path.join(base_dir, "testData", "web", "test_data.json")) as f:
        return json.load(f)

def test_suite_01_scripts(page, request):
    # TestRail ID: C102
    test_data = load_test_data()
    scenario = CommonScenario(page, request)
    
    loginPage = LoginPage(page, scenario)
    dashboardPage = DashboardPage(page, scenario)
    footerNavigation = FooterNavigation(page, scenario)
    supportPortal = SupportPortal(page, scenario)
    
    loginPage.go_to()
    loginPage.valid_login(test_data["username"], test_data["password"])
    
    footerNavigation.scroll_to_footer()
    footerNavigation.click_contact_us_link()
    
    supportPortal.navigate_to_support_portal()
    supportPortal.input_subject()
    supportPortal.input_message()
    supportPortal.click_submit_button()
    
    supportPortal.locate_success_confirmation_message()
    dashboardPage.wait_for_success_message()
    dashboardPage.assert_success_message_visible()
    supportPortal.assert_confirmation_text()
