
"""
Wrapper for Selenium browser interactions.
"""
from datetime import timedelta

from RPA.Browser.Selenium import Selenium
import logging


class BrowserWrapper:
    """A wrapper class for Selenium browser interactions."""

    def __init__(self) -> None:
        """Initialize the BrowserWrapper class."""
        self.browser = Selenium()
        self.browser.set_selenium_implicit_wait(value=timedelta(seconds=5))

    def open_browser(self, url):
        """
        Open the browser and navigate to the specified URL.

        Args:
            url (str): The URL to open.
        """
        logging.info(f"Opening browser and navigating to {url}")
        self.browser.open_available_browser(url)
        logging.info("Browser opened.")

    def close_browser(self) -> None:
        """Close the browser."""
        logging.info("Closing browser.")
        self.browser.close_browser()
        logging.info("Browser closed.")

    def click_element(self, locator) -> None:
        """
        Click an element specified by the locator.

        Args:
            locator (str): The XPath locator of the element to click.
        """
        logging.info(f"Clicking element with locator: {locator}")
        self.browser.wait_until_page_contains_element(locator)
        self.browser.find_element(locator).click()
        logging.info("Element clicked.")

    def select_from_dropdown(self, locator, value) -> None:
        """
        Select a value from a dropdown specified by the locator.

        Args:
            locator (str): The XPath locator of the dropdown.
            value (str): The value to select from the dropdown.
        """
        logging.info(f"Selecting value from dropdown with locator: {locator}")
        self.browser.wait_until_page_contains_element(locator)
        self.browser.select_from_list_by_value(locator, value)
        logging.info("Value selected.")



