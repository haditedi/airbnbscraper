from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def check_valid(args):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()

    print("Checking if properties are still active ,,,")

    for x in args:
        # ini_url="https://www.airbnb.co.uk/rooms/736788404696913896?source_impression_id=p3_1723431436_P3sSYsoqENOVl5H5"
        ini_url = x["url"].split("&")[0]
        property_name = x["name"]
        # print(ini_url)
        try:
            driver.get(ini_url)
            driver.implicitly_wait(5)
            if "Girl has dropped her ice cream." in driver.page_source:
                print("ERROR", property_name)
            else:
                print("OK", property_name)

        except Exception as e:
            print("EXCEPTIONM", e)

    driver.quit()
