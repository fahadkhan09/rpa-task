#  LA Times News Scraper RPA

This project contains a Robotic Process Automation (RPA) script designed to scrape news articles from the LA Times website based on a specified search phrase and topic. The scraped data, including article titles, dates, descriptions, and images, is stored in an Excel file.

## Project Structure

- **config.py**: Contains the XPath locators used for web scraping.
- **task.py**: The task script that runs the RPA process.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **utils/**: Contains utility scripts.
  - **browser_wrapper.py**: A wrapper class for Selenium browser interactions.
  - **utils.py**: Utility functions for downloading images, logging setup, and environment-based configuration.


## Prerequisites

- Python 3.8+
- Pip (Python package installer)
- [Robocorp Lab](https://robocorp.com/robocorp-lab) (Optional, for running in Robocorp Cloud)

## Setup Instructions

- Clone the repository
`git clone git@github.com:fahadkhan09/rpa-task.git
cd rpa-task`

- Create a virtual environment 

`python -m venv venv
source venv/bin/activate` 

- Install dependencies:

`pip install -r requirements.txt
`

## Usage
To run the automation task locally with default parameters, execute:
1. Run the `tasks.py` script.