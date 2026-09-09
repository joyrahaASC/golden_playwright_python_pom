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
            scenario: Scenario object for test context and utilities.
        """
        super().__init__(page, scenario)
        self.locators = load_locator("support_page_locators.json")
    
    def scroll_to_footer(self):
        """Scroll the page to the footer section to make footer elements visible and interactable.
        
        Waits for the footer section to be present, scrolls it into view, and waits for visibility.
        """
        footer = self.page.locator(self.locators["footer_section"])
        footer.wait_for(state="attached")
        footer.scroll_into_view_if_needed()
        footer.wait_for(state="visible")
    
    def click_contact_us_link(self):
        """Click the Contact Us or Support link in the footer section.
        
        Waits for the contact us link to be visible and clickable, then clicks it to navigate
        to the support portal.
        """
        contact_link = self.page.locator(self.locators["contact_us_link"])
        contact_link.wait_for(state="visible")
        contact_link.click()
    
    def assert_support_portal_visible(self):
        """Assert that the support portal container is visible on the page.
        
        Waits for the support portal container to be visible and asserts its visibility state
        to confirm successful navigation.
        """
        portal_container = self.page.locator(self.locators["support_portal_container"])
        portal_container.wait_for(state="visible")
        expect(portal_container).to_be_visible()
    
    def input_subject(self, subject_text):
        """Input text into the subject field of the support form.
        
        Args:
            subject_text: The subject text to input into the subject field.
        
        Waits for the subject input field to be visible and interactable, clears any existing
        text, and inputs the provided subject text.
        """
        subject_field = self.page.locator(self.locators["subject_input_field"])
        subject_field.wait_for(state="visible")
        subject_field.clear()
        subject_field.fill(subject_text)
    
    def input_message(self, message_text):
        """Input text into the message field of the support form.
        
        Args:
            message_text: The message text to input into the message textarea.
        
        Waits for the message textarea to be visible and interactable, clears any existing
        text, and inputs the provided message text.
        """
        message_field = self.page.locator(self.locators["message_textarea"])
        message_field.wait_for(state="visible")
        message_field.clear()
        message_field.fill(message_text)
    
    def click_submit_button(self):
        """Click the Submit button to submit the support request form.
        
        Waits for the submit button to be visible and clickable, then clicks it to submit
        the form.
        """
        submit_btn = self.page.locator(self.locators["submit_button"])
        submit_btn.wait_for(state="visible")
        submit_btn.click()
    
    def locate_success_message(self):
        """Locate and return the success confirmation message element.
        
        Returns:
            Locator: The success confirmation message element after form submission.
        
        Waits for the success confirmation message to be present in the DOM and returns
        the element.
        """
        success_msg = self.page.locator(self.locators["success_confirmation_message"])
        success_msg.wait_for(state="attached")
        return success_msg
    
    def wait_for_success_message(self):
        """Wait for the success confirmation message to become visible.
        
        Waits for the success confirmation message element to become visible on the page
        with an appropriate timeout.
        """
        success_msg = self.page.locator(self.locators["success_confirmation_message"])
        success_msg.wait_for(state="visible", timeout=10000)
    
    def assert_success_message_visible(self):
        """Assert that the success confirmation message is visible on the page.
        
        Waits for the success confirmation message to be visible and asserts its visibility
        to verify successful form submission.
        """
        success_msg = self.page.locator(self.locators["success_confirmation_message"])
        success_msg.wait_for(state="visible")
        expect(success_msg).to_be_visible()