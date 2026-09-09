import pytest
from playwright.sync_api import Page
from pageObjects.web.loginPage import LoginPage
from pageObjects.web.dashboardPage import DashboardPage


class TestSuite01:
    """Test Suite 01 - Login and Product Search Flow"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture to initialize page objects"""
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        yield

    def test_login_and_product_search(self, page: Page):
        """Test case: Navigate to login page, perform valid login, verify user profile, search product and add to cart, navigate to cart"""
        # Step 1: Navigate to the login page
        self.loginPage.go_to()

        # Step 2: Perform valid login with username and password
        self.loginPage.valid_login()

        # Step 3: Verify user profile name is visible in dashboard header
        self.dashboardPage.verify_user_profile_name_visible()

        # Step 4: Search for product and add to cart
        self.dashboardPage.search_product_add_cart()

        # Step 5: Navigate to cart page
        self.dashboardPage.navigate_to_cart()