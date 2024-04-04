from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

try:      
    new_url="https://www.airbnb.co.uk/rooms/1002010727603598593?source_impression_id=p3_1712153527_mBbNtthTyJ1n0cuu&check_in=2024-05-08&guests=4&adults=4&check_out=2024-05-12"
    print("NEWURL",new_url)
    driver.get(new_url)
    # print("SKYLINE 2 BED 2 BATH")
    # print("URL", url)
    # sleep(7)
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/section/div/div/div[2]/div/div[1]/button"))
    #     )
    #     element.click()
    #     sleep(3)
    # except:
    #     print("EXCEPTIOON IN CLICKABLE")
    #     pass
    try:
        total_price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/section/div[2]/div/span[2]/span[1]/span")))
        total_price=total_price.get_attribute("innerHTML")
        total_price = total_price.replace("£","")
        print(total_price)    
        # price_per_night=0
        # if len(total_price) >3:
        #     total_price = total_price.replace(",","")
        #     total_price = int(total_price.strip())
        #     price_per_night = total_price/min_nights
        # else:
        #     total_price = int(total_price.strip())
        #     price_per_night = total_price/min_nights
        
        # print("Rate/night £",price_per_night)
    except Exception as e:
        print("EXCEPTIOooo")
        
except Exception as e:
    print("EXCEPTIONM")
    