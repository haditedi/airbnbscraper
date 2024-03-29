from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime, timedelta, date
from utils import addOneDay
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

#SKY
url_relocate="https://www.airbnb.co.uk/rooms/871040174926257448?source_impression_id=p3_1704450998_hM8uppOkkjhY8NdK&check_in="
url_skyline="https://www.airbnb.co.uk/rooms/893933063998940096?source_impression_id=p3_1704361618_0j1jiCryQcZYdVPl&check_in="
url_nineelms="https://www.airbnb.co.uk/rooms/991985177917763716?source_impression_id=p3_1704451278_Eah3CTzOxqWaHULc&check_in="
url_sky10="https://www.airbnb.co.uk/rooms/1046907771076731775?source_impression_id=p3_1704451469_3qliydVyTnmWa7FH&check_in="

#HUNTER
url_charm="https://www.airbnb.co.uk/rooms/919494818502148128?source_impression_id=p3_1705312955_Qq3gYbrhzJIcQ90A&check_in="
url_vintage="https://www.airbnb.co.uk/rooms/901306741280213973?source_impression_id=p3_1705312818_1cWKDpsOurb3ssZD&check_in="
url_hunter="https://www.airbnb.co.uk/rooms/903131518446432064?source_impression_id=p3_1705311821_p9worQnaTtWB52AA&check_in="
url_ours="https://www.airbnb.co.uk/rooms/991919969842748351?source_impression_id=p3_1705313120_c%2Fm2yGmapv9ksHVg&check_in="

def getRates(property_name,url_param,arrivalDate,departureDate, min_nights, num_days, driver):
    skyline_x=[]
    skyline_y=[]
    
    for x in range(int(num_days)):
        # print("ARRIVAL DATE", arrivalDate)

        try:      
            url=f"{url_param}{arrivalDate}&guests=4&adults=4&check_out={departureDate}"
            driver.get(url)
            # print("SKYLINE 2 BED 2 BATH")
            # print("URL", url)
            sleep(3)
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/section/div/div/div[2]/div/div[1]/button"))
                )
                element.click()
                sleep(3)
            except:
                pass
                # print("")
            # sleep(3)
            total_price = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/section/div[2]/div/span[2]/span[1]/span")
            # total_price = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/section/div[2]/div/span[2]/span[1]/span
            total_price = total_price.text.replace("£","")
            price_per_night=0
            if len(total_price) >3:
                price_per_night = int(total_price.replace(",",""))/min_nights
            else:
                price_per_night = int(total_price)/min_nights
            price_per_night = int(price_per_night)
            # print("Rate/night £",price_per_night)
            skyline_y.append(price_per_night)
            
        except Exception as e:
            # print(e)
            skyline_y.append(None)
        finally:
            # print("Arrival", arrivalDate)
            skyline_x.append(arrivalDate)
            result = addOneDay(arrivalDate, min_nights)
            arrivalDate = result["arrivalDate"]
            departureDate = result["departureDate"]
            # print("DEPARTURE",departureDate)

    print(property_name,skyline_x, skyline_y)
    return skyline_x, skyline_y   

def getSky():
    arrivalDate = input("date (dd-mm-yyyy) : ")
    num_days = input("Number of days : ")
    min_nights=int(input("Minimum nigths : "))
    arrivalDate = datetime.strptime(arrivalDate,"%d-%m-%Y")
    nights = timedelta(days=min_nights)
    arrFileName=arrivalDate.strftime("%d-%m")
    departureDate = arrivalDate+nights
    departureDate = departureDate.strftime("%Y-%m-%d")
    arrivalDate = arrivalDate.strftime("%Y-%m-%d")

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    
    plt.rcParams['figure.figsize'] = [12, 7]
    
    x, y = getRates("skyline",url_skyline,arrivalDate, departureDate,min_nights,num_days, driver)
    x = [ date.fromisoformat(i) for i in x]
    x=np.array(x)
    # print(x)
    y = np.array(y).astype(np.double)
    sky_mask = np.isfinite(y)
    plt.plot_date(x[sky_mask],y[sky_mask], "g",marker="o", label="Skyline")

    sky10_x, sky10_y = getRates("Sky10", url_sky10, arrivalDate, departureDate,min_nights,num_days,driver)
    sky10_y = np.array(sky10_y).astype(np.double)
    sky10_x = np.array(sky10_x)
    sky10_mask=np.isfinite(sky10_y)
    plt.plot_date(x[sky10_mask],sky10_y[sky10_mask],"r", marker="o", label="Sky10")
    
    nine_x, nine_y = getRates("NineElm",url_nineelms,arrivalDate, departureDate,min_nights,num_days,driver)
    nine_y = np.array(nine_y).astype(np.double)
    nine_mask=np.isfinite(nine_y)
    plt.plot_date(x[nine_mask],nine_y[nine_mask],"b", marker="o", label="Nine Elm")

    relocate_x, relocate_y = getRates("Relocate", url_relocate,arrivalDate, departureDate,min_nights,num_days,driver)
    relocate_y = np.array(relocate_y).astype(np.double)
    relocate_mask=np.isfinite(relocate_y)
    plt.plot_date(x[relocate_mask],relocate_y[relocate_mask], "y", marker="o", label="Relocate")
    
    plt.legend()
    plt.xlabel("DATE")
    plt.ylabel("RATE/NIGHT")
    plt.title(f"RATE COMPARISON {choice} From {arrFileName}",fontweight="bold")
    plt.ylim(100,500)
    plt.xticks(rotation=45)  
    myFmt = mdates.DateFormatter('%d / %m')
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.savefig(f"{choice} {arrFileName}.png")
    plt.show()

def getHunter():
    arrivalDate = input("date (dd-mm-yyyy) : ")
    num_days = input("Number of days : ")
    min_nights=int(input("Minimum nigths : "))
    arrivalDate = datetime.strptime(arrivalDate,"%d-%m-%Y")
    nights = timedelta(days=min_nights)
    arrFileName=arrivalDate.strftime("%d-%m")
    departureDate = arrivalDate+nights
    departureDate = departureDate.strftime("%Y-%m-%d")
    arrivalDate = arrivalDate.strftime("%Y-%m-%d")

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    
    plt.rcParams['figure.figsize'] = [12, 7]
    
    x, y = getRates("Charm",url_charm,arrivalDate, departureDate,min_nights,num_days, driver)
    x = [ date.fromisoformat(i) for i in x]
    x=np.array(x)
    # print(x)
    y = np.array(y).astype(np.double)
    charm_mask = np.isfinite(y)
    plt.plot_date(x[charm_mask],y[charm_mask], "g",marker="o", label="charm")

    vintagex, vintagey = getRates("vintage", url_vintage, arrivalDate, departureDate,min_nights,num_days,driver)
    vintagey = np.array(vintagey).astype(np.double)
    vintagex = np.array(vintagex)
    vintagemask=np.isfinite(vintagey)
    plt.plot_date(x[vintagemask],vintagey[vintagemask],"r", marker="o", label="vintage")
    
    oursx, oursy = getRates("Ours",url_ours,arrivalDate, departureDate,min_nights,num_days,driver)
    oursy = np.array(oursy).astype(np.double)
    oursmask=np.isfinite(oursy)
    plt.plot_date(x[oursmask],oursy[oursmask],"b", marker="o", label="ours")

    hunterx, huntery = getRates("Relocate", url_relocate,arrivalDate, departureDate,min_nights,num_days,driver)
    huntery = np.array(huntery).astype(np.double)
    huntermask=np.isfinite(huntery)
    plt.plot_date(x[huntermask],huntery[huntermask], "y", marker="o", label="hunter")
    
    plt.legend()
    plt.xlabel("DATE")
    plt.ylabel("RATE/NIGHT")
    plt.title(f"RATE COMPARISON {choice} From {arrFileName}",fontweight="bold")
    plt.ylim(100,500)
    plt.xticks(rotation=45)  
    myFmt = mdates.DateFormatter('%d / %m')
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.savefig(f"{choice} {arrFileName}.png")
    plt.show()
   
choice = input("Enter 'sky' for Sky Garden or 'hunt' for Hunter House : ")
if choice == "sky":
    choice = "SKY GARDEN"
    getSky()
else:
    choice = "HUNTER HOUSE"
    getHunter()


