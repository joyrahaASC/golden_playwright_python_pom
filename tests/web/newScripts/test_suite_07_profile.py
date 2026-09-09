import pytest
from playwright.sync_api import Page, expect
from pageObjects.web.LoginPage import LoginPage
from pageObjects.web.DashboardPage import DashboardPage


class TestSuite07Profile:
    """Test suite for user profile verification and product operations"""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup fixture to initialize page objects"""
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        yield

    def test_profile_verification_and_cart_operations(self, page: Page):
        """Test to verify user profile name visibility and perform cart operations"""
        # Navigate to the login page
        self.loginPage.go_to()

        # Perform valid login with username and password
        self.loginPage.valid_login()

        # Verify user profile name is visible in dashboard header
        self.dashboardPage.verify_user_profile_name_visible()

        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()

        # Navigate to the cart page
        self.dashboardPage.navigate_to_cart()
