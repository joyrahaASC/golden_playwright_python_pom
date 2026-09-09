import pytest
from pageObjects.web.LoginPage import LoginPage
from pageObjects.web.DashboardPage import DashboardPage


class TestSuite07BProfile:
    """Test suite for profile verification and product cart workflow"""

    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Setup fixture to initialize page objects"""
        self.loginPage = LoginPage(page)
        self.dashboardPage = DashboardPage(page)
        yield

    def test_profile_and_cart_workflow(self, page):
        """Test to verify profile name and product cart functionality"""
        # Navigate to the login page
        self.loginPage.go_to()

        # Perform valid login with username and password
        self.loginPage.valid_login()

        # Get dashboard header profile name
        profile_name = self.dashboardPage.get_header_profile_name()
        assert profile_name is not None, "Profile name should not be None"
        assert len(profile_name) > 0, "Profile name should not be empty"

        # Search for product and add to cart
        self.dashboardPage.search_product_add_cart()

        # Navigate to the cart page
        self.dashboardPage.navigate_to_cart()

        # Verify navigation to cart was successful
        assert page.url.__contains__("cart") or "cart" in page.url.lower(), "Should navigate to cart page"