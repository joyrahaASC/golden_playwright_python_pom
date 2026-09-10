import json
import os
from playwright.sync_api import expect
from .common_page import CommonPage

def load_locator(filename):
    """Load locator JSON file from the locators directory.
    
    Args:
        filename: Name of the JSON file containing locators
        
    Returns:
        Dictionary of locators
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    locator_path = os.path.join(base_dir, "locators", "web", filename)
    with open(locator_path) as f:
        return json.load(f)

class FooterNavigation(CommonPage):
    """Page Object Model for Footer Navigation.
    
    This class handles all interactions with the footer navigation section.
    """
    
    flow_name = "footer_navigation"
    
    def __init__(self, page, scenario):
        """Initialize the footer navigation page object.
        
        Args:
            page: Playwright page object
            scenario: Test scenario context
        """
        super().__init__(page, scenario)
        self.locators = load_locator("footer_navigation.json")
    
    def scroll_to_footer(self):
        """Scroll the page down to bring the footer section into view.
        
        Waits for footer section to be present in DOM, executes JavaScript scroll
        to bring footer into view, waits for visibility, and verifies display.
        """
        footer_element = self.page.locator(self.locators["footer_section"])
        footer_element.wait_for(state="attached")
        footer_element.scroll_into_view_if_needed()
        footer_element.wait_for(state="visible")
        expect(footer_element).to_be_visible()
    
    def click_contact_us_link(self):
        """Locate and click the Contact Us link in the footer section.
        
        Waits for the contact us link to be present and clickable before clicking,
        then verifies navigation completed successfully.
        """
        contact_us_element = self.page.locator(self.locators["contact_us_link"])
        contact_us_element.wait_for(state="visible")
        expect(contact_us_element).to_be_visible()
        contact_us_element.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_load_state("domcontentloaded")