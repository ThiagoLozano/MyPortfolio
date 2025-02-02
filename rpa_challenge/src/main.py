import os
from dotenv import load_dotenv
from web.chrome import WebChrome
from files.excel import FileExcel
from utils import pylog

load_dotenv()

def main():
    """
    Main function to automate the RPA Challenge.

    Steps:
    1. Load configuration from environment variables.
    2. Open the RPA Challenge website.
    3. Check if the Excel file exists, if not, download it.
    4. Read data from the Excel file.
    5. Fill the form on the website with the data from the Excel file.
    6. Submit the form and log the result.
    """
    # -------------------------------------- #
    # ----- Load environment variables ----- #
    # -------------------------------------- #

    DIR_EXCEL  = os.environ.get('DIR_EXCEL')
    NAME_EXCEL = os.environ.get('NAME_EXCEL')
    PATH_FULL  = fr"{DIR_EXCEL}\{NAME_EXCEL}"

    # ------------------------------------ #
    # ---- Create a WebChrome object ----- #
    # ------------------------------------ #

    web = WebChrome(dir_download=DIR_EXCEL)
    web.open_url(site_url='https://rpachallenge.com/')

    # ------------------------------- #
    # ----- Download Excel file ----- #
    # ------------------------------- #

    if not FileExcel().search_excel_file(path_file=PATH_FULL):
        xpath_download_excel_btn = '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a'
        web.click_element(xpath_element=xpath_download_excel_btn)
        pylog("Downloading Excel file")

        # Wait for the file to download.
        if not web.wait_download(path_dowload=DIR_EXCEL, file_name=NAME_EXCEL):
            pylog("Failed to download Excel file")
            return
        pylog("Excel file downloaded successfully")

    # -------------------------------------------- #
    # ----- Convert Excel file to dictionary ----- #
    # -------------------------------------------- #
    
    dic_df = FileExcel().convert_to_dict(path_file=PATH_FULL)
    pylog("Converted Excel file to dictionary")

    # ------------------------- #
    # ----- Fill the form ----- #
    # ------------------------- #
    
    # Click on the 'Start' button.
    web.click_element(xpath_element='/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
    pylog("Clicked 'Start' button")

    form_fields = {
        "First Name": "//input[@ng-reflect-name='labelFirstName']",
        "Last Name ": "//input[@ng-reflect-name='labelLastName']",
        "Email": "//input[@ng-reflect-name='labelEmail']",
        "Phone Number": "//input[@ng-reflect-name='labelPhone']",
        "Address": "//input[@ng-reflect-name='labelAddress']",
        "Company Name": "//input[@ng-reflect-name='labelCompanyName']",
        "Role in Company": "//input[@ng-reflect-name='labelRole']"
    }

    for info in dic_df:
        for field, xpath in form_fields.items():
            web.fill_element(xpath_element=xpath, text=info[field])
            pylog(f"Filled field '{field}' with value '{info[field]}'")

        # Click on the 'Submit' button.
        web.click_element(xpath_element='/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
        pylog("Clicked 'Submit' button")

    # Get and log the form submission message.
    text_msg = web.get_text_element(xpath_element='/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]')
    pylog(text_msg)

    # Close the browser.
    web.close()

if __name__ == "__main__":
    main()
