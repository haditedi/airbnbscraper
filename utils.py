from datetime import datetime, timedelta, date
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import numpy as np
import matplotlib.pyplot as plt

def addOneDay(element, min_nights):
    arrivalDate = datetime.strptime(element,"%Y-%m-%d")
    arrivalDate += timedelta(days=1)
    nights = timedelta(days=min_nights)
    departureDate = arrivalDate+nights
    departureDate = departureDate.strftime("%Y-%m-%d")
    arrivalDate = arrivalDate.strftime("%Y-%m-%d")
    return {"arrivalDate":arrivalDate, "departureDate":departureDate}

def getRates(listProperty,arrivalDate,departureDate, min_nights, num_days, driver):
    
    for index in range(len(listProperty)):
        for key in listProperty[index]:
            property_name=listProperty[index]["name"]
            line_color=listProperty[index]["line_color"]
            if key == "url":
                url=listProperty[index][key]
                print("PROPERTY", property_name)
                # print("LINE COLOR", line_color)
                skyline_x=[]
                skyline_y=[]
                initArrDate=arrivalDate
                initDepDate=departureDate
                
                for _ in range(int(num_days)):
                    print("ARRIVAL DATE", arrivalDate)

                    try:      
                        new_url=f"{url}{arrivalDate}&guests=4&adults=4&check_out={departureDate}"
                        print("NEWURL",new_url)
                        driver.get(new_url)
                        # print("SKYLINE 2 BED 2 BATH")
                        # print("URL", url)
                        sleep(7)
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
                                 
                            price_per_night=0
                            if len(total_price) >3:
                                total_price = total_price.replace(",","")
                                total_price = int(total_price.strip())
                                price_per_night = total_price/min_nights
                            else:
                                total_price = int(total_price.strip())
                                price_per_night = total_price/min_nights
                            
                            print("Rate/night £",price_per_night)
                            skyline_y.append(price_per_night)
                            
                        except Exception as e:
                            print("EXCEPTIONM")
                            skyline_y.append(None)
                                            
                                                                     
                        # total_price = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/section/div[2]/div/span[2]/span[1]/span")
                        # print("TOTAL PRICE", total_price.text)
                        
                        
                    except Exception as e:
                        print("EXECEPTION",e)
                        skyline_y.append(None)
                    finally:
                        # print("Arrival", arrivalDate)
                        # print("DEPARTURE",departureDate)
                        skyline_x.append(arrivalDate)
                        result = addOneDay(arrivalDate, min_nights)
                        arrivalDate = result["arrivalDate"]
                        departureDate = result["departureDate"]
                arrivalDate = initArrDate
                departureDate = initDepDate
                print(property_name,skyline_x, skyline_y)
            
                x_data = [ date.fromisoformat(i) for i in skyline_x]
                x_data=np.array(x_data)
               
                y_data = np.array(skyline_y).astype(np.double)
                sky_mask = np.isfinite(y_data)
                plt.plot_date(x_data[sky_mask],y_data[sky_mask], line_color,marker="o", label=property_name)
            