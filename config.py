# config.py

"""
Configuration constants for the RPA script.
"""

LA_TIMES_OUTPUT_DIR = "output"
NEWS_DATA = "news_data.xlsx"

# XPaths
SEARCH_BUTTON = '//button[@data-element="search-button"]'
SELECT_TOPIC = "//span[text()='{}']"
SEARCH_FORM_INPUT = '//input[@data-element="search-form-input"]'
SEARCH_SUBMIT_BUTTON = '//button[@data-element="search-submit-button"]'
SEARCH_FILTER = "//div[@class='search-filter']//p[contains(text(), 'Topics')]/parent::*"
SEE_ALL_TEXT = "//span[@class='see-all-text']"
SEARCH_RESULTS = '//ul[@class="search-results-module-results-menu"]//li'
ARTICLE_ELEMENT = "//ul[@class='search-results-module-results-menu']//li"
ARTICLE_IMAGE = ".//img"
ARTICLE_TITLE = ".//h3//a[@class='link']"
ARTICLE_DATE = ".//p[@class='promo-timestamp']"
ARTICLE_DESCRIPTION = ".//p[@class='promo-description']"
SORTING_AREA = "//select[@class='select-input']"
