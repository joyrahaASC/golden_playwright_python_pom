import json
import os
from playwright.sync_api import expect
from .common_page import CommonPage

def load_locator(filename):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    locator_path = os.path.join(base_dir, "locators", "web", filename)
    with open(locator_path) as f:
        return json.load(f)

class SupportPage(CommonPage):
    flow_name = "support_page"
    
    def __init__(self, page, scenario):
        """Initialize the SupportPage with page and scenario objects.
        
        Args:
            page: Playwright page object for browser interactions.
            scenario: Scenario object for test context and accessibility analysis.
        """
        super().__init__(page, scenario)
        self.locators = load_locator("support_page.json")
    
    def navigate_to_support_portal(self):
        """Navigate to the Support Portal page and verify the support form is visible.
        
        This method navigates to the support portal URL, waits for the page to load,
        and verifies that the support form element is displayed on the page.
        """
        self.page.wait_for_load_state("domcontentloaded")
        support_form = self.page.locator(self.locators["support_form"])
        support_form.wait_for(state="visible")
        expect(support_form).to_be_visible()
    
    def input_subject(self, subject_text):
        """Input text into the Subject field of the support form.
        
        Args:
            subject_text (str): The subject text to be entered into the subject input field.
        """
        subject_field = self.page.locator(self.locators["subject_input_field"])
        subject_field.wait_for(state="visible")
        subject_field.clear()
        subject_field.fill(subject_text)
    
    def input_message(self, message_text):
        """Input text into the Message textarea of the support form.
        
        Args:
            message_text (str): The message text to be entered into the message textarea.
        """
        message_field = self.page.locator(self.locators["message_textarea"])
        message_field.wait_for(state="visible")
        message_field.clear()
        message_field.fill(message_text)
    
    def click_submit_button(self):
        """Click the Submit button on the support form.
        
        This method waits for the submit button to be visible and clickable,
        then clicks it to submit the support request.
        """
        submit_btn = self.page.locator(self.locators["submit_button"])
        submit_btn.wait_for(state="visible")
        submit_btn.click()
    
    def locate_confirmation_message(self):
        """Locate and return the confirmation message element.
        
        Returns:
            Locator: The Playwright locator object for the confirmation message element.
        """
        confirmation_msg = self.page.locator(self.locators["confirmation_message"])
        confirmation_msg.wait_for(state="attached")
        return confirmation_msg
    
    def wait_for_confirmation_message(self, timeout=10):
        """Wait for the confirmation message to become visible.
        
        Args:
            timeout (int): Maximum time in seconds to wait for the element (default: 10).
        """
        confirmation_msg = self.page.locator(self.locators["confirmation_message"])
        confirmation_msg.wait_for(state="visible", timeout=timeout * 1000)
        expect(confirmation_msg).to_be_visible()
    
    def verify_confirmation_message_displayed(self, expected_message=None):
        """Verify that the confirmation message is displayed and optionally validate its text.
        
        Args:
            expected_message (str, optional): The expected confirmation message text to validate.
        
        Returns:
            bool: True if the confirmation message is displayed and matches expected text (if provided).
        
        Raises:
            AssertionError: If the confirmation message is not displayed or text doesn't match.
        """
        confirmation_msg = self.page.locator(self.locators["confirmation_message"])
        confirmation_msg.wait_for(state="visible")
        expect(confirmation_msg).to_be_visible()
        
        if expected_message is not None:
            actual_text = confirmation_msg.inner_text()
            assert actual_text == expected_message, f"Expected message '{expected_message}' but got '{actual_text}'"
        
        return True