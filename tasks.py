import logging
from scrappers.la_times import LATimesRPA
from utils.utils import setup_logging, get_search_config

# Initialize logging
setup_logging()

# Get search configuration
SEARCH_PHASE, TOPIC = get_search_config()


if __name__ == "__main__":
    rpa = LATimesRPA(phrase=SEARCH_PHASE, topic=TOPIC)
    """Run the RPA process."""
    try:
        rpa.open_site()
        rpa.search_phrase()
        rpa.select_topic()
        rpa.get_news_data()
        rpa.store_in_excel()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        rpa.close_browser()
