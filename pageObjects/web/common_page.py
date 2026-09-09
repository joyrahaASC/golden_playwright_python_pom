from .common_scenario import CommonScenario

class CommonPage:
    def __init__(self, page, scenario: CommonScenario):
        self.page = page
        self.scenario = scenario

    def get_value(self, key: str):
        return self.scenario.get_value(key)

    def set_value(self, key: str, value: str):
        self.scenario.set_value(key, value)

    def take_screenshot(self, name: str):
        self.scenario.take_screenshot(name)

    def scroll_to_footer(self):
        """Scroll the page to the footer section.
        
        Waits for the footer section to be present in DOM, scrolls it into viewport
        using JavaScript, and waits for it to be visible.
        """
        footer_locator = self.get_value('footer_section')
        footer = self.page.locator(footer_locator)
        footer.wait_for(state='attached')
        footer.scroll_into_view_if_needed()
        footer.wait_for(state='visible')

    def click_contact_support_link(self):
        """Click the Contact Us or Support link in the footer.
        
        Waits for the contact support link to be visible and clickable,
        then performs a click action.
        """
        contact_link_locator = self.get_value('contact_support_link')
        contact_link = self.page.locator(contact_link_locator)
        contact_link.wait_for(state='visible')
        contact_link.click()

    def verify_support_portal_visible(self):
        """Verify that the Support Portal section is visible.
        
        Waits for the support portal section to be visible and asserts
        that it is displayed on the page.
        
        Returns:
            bool: True if the support portal section is visible.
        """
        support_portal_locator = self.get_value('support_portal_section')
        support_portal = self.page.locator(support_portal_locator)
        support_portal.wait_for(state='visible')
        assert support_portal.is_visible(), "Support portal section is not visible"
        return True

    def input_subject(self, subject_text):
        """Input text into the Subject field.
        
        Waits for the subject input field to be visible and interactable,
        clears any existing text, and inputs the provided subject text.
        
        Args:
            subject_text (str): The subject text to input.
        """
        subject_locator = self.get_value('subject_input_field')
        subject_field = self.page.locator(subject_locator)
        subject_field.wait_for(state='visible')
        subject_field.clear()
        subject_field.fill(subject_text)

    def input_message(self, message_text):
        """Input text into the Message field.
        
        Waits for the message textarea field to be visible and interactable,
        clears any existing text, and inputs the provided message text.
        
        Args:
            message_text (str): The message text to input.
        """
        message_locator = self.get_value('message_textarea_field')
        message_field = self.page.locator(message_locator)
        message_field.wait_for(state='visible')
        message_field.clear()
        message_field.fill(message_text)

    def click_submit_button(self):
        """Click the Submit button in the support form.
        
        Waits for the submit button to be visible and clickable,
        then performs a click action to submit the form.
        """
        submit_button_locator = self.get_value('submit_button')
        submit_button = self.page.locator(submit_button_locator)
        submit_button.wait_for(state='visible')
        submit_button.click()

    def locate_confirmation_message(self):
        """Locate and return the confirmation message element.
        
        Waits for the confirmation message element to be present in DOM
        and returns the locator object for further operations.
        
        Returns:
            Locator: The confirmation message element locator.
        """
        confirmation_locator = self.get_value('confirmation_message_element')
        confirmation_element = self.page.locator(confirmation_locator)
        confirmation_element.wait_for(state='attached')
        return confirmation_element

    def wait_for_confirmation_message_visible(self, timeout=10):
        """Wait for the confirmation message to be visible.
        
        Waits for the confirmation message element to be visible on the page
        after form submission with a configurable timeout.
        
        Args:
            timeout (int): Maximum time to wait in seconds (default: 10).
        
        Returns:
            bool: True if the confirmation message becomes visible within timeout.
        
        Raises:
            TimeoutError: If the confirmation message is not visible within timeout.
        """
        confirmation_locator = self.get_value('confirmation_message_element')
        confirmation_element = self.page.locator(confirmation_locator)
        try:
            confirmation_element.wait_for(state='visible', timeout=timeout * 1000)
            return True
        except Exception as e:
            raise TimeoutError(f"Confirmation message not visible within {timeout} seconds") from e

    def verify_confirmation_message_visible(self):
        """Verify that the confirmation message is visible.
        
        Waits for the confirmation message element to be visible and asserts
        that it is displayed on the page. Optionally retrieves the message text.
        
        Returns:
            str: The text content of the confirmation message.
        """
        confirmation_locator = self.get_value('confirmation_message_element')
        confirmation_element = self.page.locator(confirmation_locator)
        confirmation_element.wait_for(state='visible')
        assert confirmation_element.is_visible(), "Confirmation message is not visible"
        message_text = confirmation_element.text_content()
        return message_text
