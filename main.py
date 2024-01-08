# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep


# options = Options()
# options.headless = True
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options)
# driver.get("https://www.airbnb.co.uk/rooms/1046907771076731775?")
# sleep(3)
# print(driver.current_url)

def mycoba(param,arrivalDate="2024-01-05"):
    arrivalDate = arrivalDate
    url = param
    new_url = f"{url}"
    print(new_url)
mycoba("https://www.airbnb.co.uk/rooms/893933063998940096?source_impression_id=p3_1704361618_0j1jiCryQcZYdVPl&check_in={arrivalDate}&guests=4&adults=4&check_out={departureDate}")