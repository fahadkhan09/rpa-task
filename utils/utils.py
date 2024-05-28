# utils/utils.py

"""
Utility functions for the RPA script.
"""

import os
import logging
import re
from RPA.HTTP import HTTP
from RPA.Robocorp.WorkItems import WorkItems
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

downloader = HTTP()

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_image(url, file_name, output_dir):
    """
    Download an image from the given URL and save it to the specified directory.

    Args:
        url (str): The URL of the image to download.
        file_name (str): The name to save the downloaded image as.
        output_dir (str): The directory to save the downloaded image.
    """
    logging.info(f"Downloading image from URL: {url}")
    try:

        downloader.download(url, f"{output_dir}/{file_name}.png")
        logging.info("Image downloaded.")
    except Exception as e:
        logging.error(f"Error downloading image: {e}")

def get_field_value(element, locator):
    """
    Get the text value of an element specified by the locator.

    Args:
        element (WebElement): The parent web element.
        locator (str): The XPath locator for the target element.

    Returns:
        str: The text value of the target element, or an empty string if not found.
    """
    try:
        return element.find_element(By.XPATH, locator).text
    except NoSuchElementException:
        return ''

def get_search_config():
    """
    Get the search configuration based on the environment variable.

    Returns:
        tuple: A tuple containing the search phase and topic.
    """
    if os.getenv("RPA_CLOUD"):
        work_items = WorkItems()
        work_items.get_input_work_item()
        variables = work_items.get_work_item_payload()
        search_phase = variables.get("SEARCH_PHASE")
        topic = variables.get("TOPIC")
    else:
        search_phase = "pak vs NZ"
        topic = "Sports"
    return search_phase, topic


def verify_title_has_amount(title):
    """
    Verify if the title contains a specified amount in dollars or mentions USD.

    Args:
        title (str): The title to verify.

    Returns:
        bool: True if the title contains the specified amount or mentions USD, False otherwise.
    """
    # Regular expression pattern to match the specified formats
    amount_pattern = r'\$[\d,.]+|\d+\s*(dollars|USD)'

    # Search for the pattern in the title
    match = re.search(amount_pattern, title)

    # Return True if a match is found, otherwise False
    return bool(match)


