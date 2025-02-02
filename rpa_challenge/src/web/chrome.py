import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import pylog

class WebChrome:
    def __init__(self, *, dir_download:str=None):
        """
        Initialize the WebChrome class with Chrome options.

        Args:
            dir_download (str, optional): Directory path where files will be downloaded. Defaults to None.
        """
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option('prefs', {"download.default_directory": dir_download})

        self.driver = webdriver.Chrome(options=chrome_options)

    def open_url(self, *, site_url:str):
        """
        Open the specified URL in the browser.

        Args:
            site_url (str): The URL of the website to open.

        Raises:
            Exception: If the URL cannot be opened.
        """
        try:
            self.driver.get(site_url)
        except Exception as error:
            pylog(f"Failed to open URL {site_url}: {error}")
            raise

    def wait_element(self, *, timeout:int=30, xpath_element:str):
        """
        Wait for an element to be visible on the page.

        Args:
            timeout (int, optional): Maximum time to wait for the element. Defaults to 30 seconds.
            xpath_element (str): The XPath of the element to wait for.

        Returns:
            WebElement: The web element if found.

        Raises:
            TimeoutException: If the element is not found within the timeout period.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath_element))
            )
            return element
        except Exception as error:
            pylog(f"Element not visible or not found: {error}")
            raise

    def get_text_element(self, *, timeout:int=30, xpath_element:str):
        """
        Get the text of an element.

        Args:
            timeout (int, optional): Maximum time to wait for the element. Defaults to 30 seconds.
            xpath_element (str): The XPath of the element to get text from.

        Returns:
            str: The text of the element.

        Raises:
            Exception: If the text cannot be retrieved.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath_element))
            )
            return element.text if element else ""

        except Exception as error:
            pylog(f"Failed to get text from element: {error}")
            raise

    def click_element(self, *, timeout:int=30, xpath_element:str):
        """
        Click on an element.

        Args:
            timeout (int, optional): Maximum time to wait for the element. Defaults to 30 seconds.
            xpath_element (str): The XPath of the element to click.

        Raises:
            Exception: If the element cannot be clicked.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath_element))
            )
            if element:
                element.click()
        except Exception as error:
            pylog(f"Failed to click element: {error}")
            raise

    def fill_element(self, *, timeout:int=30, xpath_element:str, text:str):
        """
        Fill an element with text.

        Args:
            timeout (int, optional): Maximum time to wait for the element. Defaults to 30 seconds.
            xpath_element (str): The XPath of the element to fill.
            text (str): The text to fill the element with.

        Raises:
            Exception: If the element cannot be filled.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath_element))
            )
            if element:
                element.send_keys(text)
        except Exception as error:
            pylog(f"Failed to fill element: {error}")
            raise

    def wait_download(self, *, timeout:int=60, path_dowload:str, file_name:str):
        """
        Wait for a file to be downloaded.

        Args:
            timeout (int, optional): Maximum time to wait for the download. Defaults to 60 seconds.
            path_dowload (str): The directory path where the file will be downloaded.
            file_name (str): The name of the file to wait for.

        Returns:
            bool: True if the file is downloaded, False otherwise.

        Raises:
            Exception: If the download times out.
        """
        seg= 0
        while seg < timeout:
            if file_name in os.listdir(path_dowload):
                return True
            else:
                time.sleep(1)
                seg += 1

        pylog(f"Download timed out for file: {file_name}")
        return False

    def close(self):
        """
        Close the browser.
        """
        self.driver.close()
        pylog("Closing the browser")
