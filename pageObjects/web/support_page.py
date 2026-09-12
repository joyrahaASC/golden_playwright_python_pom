import json
import os
from playwright.sync_api import expect
from .common_page import CommonPage

def load_locator(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    locator_path = os.path.join(base_dir, "locators", "web", filename)
    with open(locator_path) as f:
        return json.load(f)

class Support(CommonPage):
    flow_name = "support_page"
    
    def __init__(self, page, scenario):
        """Initialize the Support page object.
        
        Args:
            page: Playwright page object for browser interactions.
            scenario: Scenario object for test context and reporting.
        """
        super().__init__(page, scenario)
        self.locators = load_locator("support_page.json")
    
    def verify_support_portal_loaded(self):
        """Verify that the support portal page has loaded successfully.
        
        Waits for the support portal header to be visible and asserts its presence.
        Optionally verifies the header text contains expected content.
        """
        support_header = self.page.locator(self.locators["support_portal_header"])
        support_header.wait_for(state="visible")
        expect(support_header).to_be_visible()
        header_text = support_header.inner_text()
        assert "Support" in header_text or "Help" in header_text, f"Expected support portal header, got: {header_text}"
    
    def input_subject(self, subject_text):
        """Input subject text into the subject field.
        
        Args:
            subject_text (str): The subject line for the support request.
        """
        subject_field = self.page.locator(self.locators["subject_input_field"])
        subject_field.wait_for(state="visible")
        subject_field.clear()
        subject_field.fill(subject_text)
    
    def input_message(self, message_text):
        """Input message text into the message textarea.
        
        Args:
            message_text (str): The detailed message content for the support request.
        """
        message_field = self.page.locator(self.locators["message_textarea"])
        message_field.wait_for(state="visible")
        message_field.clear()
        message_field.fill(message_text)
    
    def click_submit_button(self):
        """Click the submit button to submit the support request.
        
        Waits for the submit button to be visible and enabled before clicking.
        """
        submit_btn = self.page.locator(self.locators["submit_button"])
        submit_btn.wait_for(state="visible")
        expect(submit_btn).to_be_enabled()
        submit_btn.click()
    
    def wait_for_confirmation_message(self):
        """Wait for the success confirmation message to become visible.
        
        Uses an explicit wait with appropriate timeout for the confirmation message element.
        """
        confirmation = self.page.locator(self.locators["confirmation_message"])
        confirmation.wait_for(state="visible", timeout=10000)
    
    def verify_confirmation_message_displayed(self):
        """Assert that the success confirmation message is displayed.
        
        Verifies the confirmation message is visible and contains expected confirmation content.
        """
        confirmation = self.page.locator(self.locators["confirmation_message"])
        confirmation.wait_for(state="visible")
        expect(confirmation).to_be_visible()
        confirmation_text = confirmation.inner_text()
        assert "submitted" in confirmation_text.lower() or "success" in confirmation_text.lower(), f"Expected confirmation message, got: {confirmation_text}"