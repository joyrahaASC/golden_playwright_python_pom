import json
import os
from playwright.sync_api import expect
from .common_page import CommonPage

def load_locator(filename):
    """Load locator JSON file from the locators/web directory.
    
    Args:
        filename: Name of the locator JSON file
        
    Returns:
        Dictionary containing locator mappings
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    locator_path = os.path.join(base_dir, "locators", "web", filename)
    with open(locator_path) as f:
        return json.load(f)

class SupportPortal(CommonPage):
    flow_name = "support_portal_page"
    
    def __init__(self, page, scenario):
        """Initialize the SupportPortal page object.
        
        Args:
            page: Playwright page instance
            scenario: Scenario context for test execution
        """
        super().__init__(page, scenario)
        self.locators = load_locator("support_portal_page.json")
    
    def navigate_to_support_portal(self):
        """Navigate to the Support Portal page and wait for it to fully load.
        
        Handles page transitions and verifies the support portal page header is visible
        to confirm successful navigation.
        """
        self.page.wait_for_load_state("domcontentloaded")
        support_header = self.page.locator(self.locators["support_portal_page_header"])
        support_header.wait_for(state="visible")
        expect(support_header).to_be_visible()
    
    def input_subject(self, subject_text):
        """Input subject text into the subject input field.
        
        Clears any existing text, enters the provided subject text, and verifies
        the text was entered successfully.
        
        Args:
            subject_text: The subject text to enter into the field
        """
        subject_field = self.page.locator(self.locators["subject_input_field"])
        subject_field.wait_for(state="visible")
        expect(subject_field).to_be_enabled()
        subject_field.clear()
        subject_field.fill(subject_text)
        entered_value = subject_field.input_value()
        assert entered_value == subject_text, f"Expected '{subject_text}' but got '{entered_value}'"
    
    def input_message(self, message_text):
        """Input message text into the message textarea.
        
        Clears any existing text, enters the provided message text, and verifies
        the text was entered successfully.
        
        Args:
            message_text: The message text to enter into the textarea
        """
        message_field = self.page.locator(self.locators["message_textarea"])
        message_field.wait_for(state="visible")
        expect(message_field).to_be_enabled()
        message_field.clear()
        message_field.fill(message_text)
        entered_value = message_field.input_value()
        assert entered_value == message_text, f"Expected '{message_text}' but got '{entered_value}'"
    
    def click_submit_button(self):
        """Click the Submit button to send the support request.
        
        Waits for the button to be visible and enabled, clicks it, and handles
        any loading states that appear during submission.
        """
        submit_btn = self.page.locator(self.locators["submit_button"])
        submit_btn.wait_for(state="visible")
        expect(submit_btn).to_be_enabled()
        submit_btn.click()
        loading_indicator = self.page.locator(self.locators["loading_indicator"])
        if loading_indicator.is_visible():
            loading_indicator.wait_for(state="hidden", timeout=10000)
        self.page.wait_for_load_state("networkidle")
    
    def locate_success_confirmation_message(self):
        """Locate and return the success confirmation message element.
        
        Waits for the confirmation message to be visible after form submission
        and returns the locator for further validation.
        
        Returns:
            Playwright Locator object for the success confirmation message
        """
        confirmation_msg = self.page.locator(self.locators["success_confirmation_message"])
        confirmation_msg.wait_for(state="visible")
        expect(confirmation_msg).to_be_attached()
        return confirmation_msg
    
    def assert_confirmation_text(self, expected_text):
        """Assert that the confirmation message text matches the expected value.
        
        Retrieves the text from the confirmation message element, normalizes it,
        and asserts it matches the expected text. Raises an assertion error with
        a descriptive message if there is a mismatch.
        
        Args:
            expected_text: The expected confirmation text to validate against
        """
        confirmation_msg = self.page.locator(self.locators["success_confirmation_message"])
        confirmation_msg.wait_for(state="visible")
        actual_text = confirmation_msg.inner_text().strip()
        assert expected_text in actual_text, f"Expected confirmation text '{expected_text}' not found in '{actual_text}'"