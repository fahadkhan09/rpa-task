import logging
import os
import time

from openpyxl import Workbook
from selenium.webdriver.common.by import By

from config import *
from utils.utils import setup_logging, download_image, get_field_value, verify_title_has_amount
from utils.browser_wrapper import BrowserWrapper


class LATimesRPA(BrowserWrapper):
    """A class to perform RPA operations on the LA Times website."""

    def __init__(self, phrase: str, topic: str) -> None:
        """Initialize the LATimesRPA class."""
        self.articles = []
        self.phrase = phrase
        self.topic = topic
        self.workbook = Workbook()


        super().__init__()

    def open_site(self) -> None:
        """Open the LA Times website."""
        self.open_browser("https://www.latimes.com/")

    def search_phrase(self) -> None:
        """
        Search for a given phrase on the LA Times website.
        """
        logging.info(f"Searching for phrase: {self.phrase}")
        self.browser.wait_until_page_contains_element(SEARCH_BUTTON)
        self.browser.find_element(SEARCH_BUTTON).click()
        self.browser.wait_until_page_contains_element(SEARCH_FORM_INPUT)
        self.browser.find_element(SEARCH_FORM_INPUT).send_keys(self.phrase)
        self.browser.wait_until_page_contains_element(SEARCH_SUBMIT_BUTTON)
        self.browser.find_element(SEARCH_SUBMIT_BUTTON).click()
        logging.info("Search submitted.")

    def select_topic(self) -> None:
        """
        Select a specific topic on the LA Times search results page.

        Args:
            topic (str): The topic to select.
        """
        self.click_element(SEARCH_FILTER)
        self.click_element(SEE_ALL_TEXT)
        self.click_element(SELECT_TOPIC.format(self.topic))
        self.select_from_dropdown(SORTING_AREA, '1')

    def get_news_data(self) -> None:
        """
        Extract news data from the search results page.

        Returns:
            list: A list of dictionaries containing news article data.
        """
        self.browser.wait_until_page_contains_element('//div[@class="promo-wrapper"]//img', limit=10)
        self.browser.wait_until_page_contains_element(ARTICLE_ELEMENT)
        article_elements = self.browser.find_elements(ARTICLE_ELEMENT)

        for idx, element in enumerate(article_elements, start=1):
            img_name = f'article_{idx}'
            element.find_element(By.XPATH, ARTICLE_IMAGE)
            img_src = element.find_element(By.XPATH, ARTICLE_IMAGE).get_attribute('src') if element.find_element(By.XPATH, ARTICLE_IMAGE) else ''
            post_title = get_field_value(element, ARTICLE_TITLE)
            post_description = get_field_value(element, ARTICLE_DESCRIPTION)
            post_date = get_field_value(element, ARTICLE_DATE)

            post_has_amount = verify_title_has_amount(post_title)
            if not post_has_amount:
                post_has_amount = verify_title_has_amount(post_description)

            article_data_map = {
                "title": post_title,
                "date": post_date,
                "description": post_description,
                "profile_picture": img_name,
                "amount": 'True' if post_has_amount else 'False'
            }
            if img_src:
                download_image(img_src, img_name, LA_TIMES_OUTPUT_DIR)
            self.articles.append(article_data_map)

    def store_in_excel(self) -> None:
        """
        Store the extracted news data in an Excel file.
        """
        sheet = self.workbook.active
        sheet.title = "Articles"
        sheet.append(["Title", "Date", "Description", "Post Thumbnail", "Has amount"])

        for item in self.articles:
            row_data = (item['title'], item['date'], item['description'], item['profile_picture'], item['amount'])
            sheet.append(row_data)

        if not os.path.exists(LA_TIMES_OUTPUT_DIR):
            os.makedirs(LA_TIMES_OUTPUT_DIR)

        self.workbook.save(f'{LA_TIMES_OUTPUT_DIR}/{NEWS_DATA}')
