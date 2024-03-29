from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime, timedelta
from utils import getRates
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


#SKY
sky=[
    {"name":"Relocate", "url":"https://www.airbnb.co.uk/rooms/871040174926257448?source_impression_id=p3_1704450998_hM8uppOkkjhY8NdK&check_in=","line_color":"r"},
     {"name":"Skyline","url":"https://www.airbnb.co.uk/rooms/893933063998940096?source_impression_id=p3_1704361618_0j1jiCryQcZYdVPl&check_in=","line_color":"g"},
     {"name":"Nineelms","url":"https://www.airbnb.co.uk/rooms/991985177917763716?source_impression_id=p3_1704451278_Eah3CTzOxqWaHULc&check_in=","line_color":"b"},
     {"name":"Ours","url":"https://www.airbnb.co.uk/rooms/1046907771076731775?source_impression_id=p3_1704451469_3qliydVyTnmWa7FH&check_in=","line_color":"y"}
     ]

#HUNTER
hunter=[
    {"name":"Charm", "url":"https://www.airbnb.co.uk/rooms/919494818502148128?source_impression_id=p3_1705312955_Qq3gYbrhzJIcQ90A&check_in=","line_color":"r"},
     {"name":"Vintage","url":"https://www.airbnb.co.uk/rooms/901306741280213973?source_impression_id=p3_1705312818_1cWKDpsOurb3ssZD&check_in=","line_color":"g"},
     {"name":"Hunter","url":"https://www.airbnb.co.uk/rooms/903131518446432064?source_impression_id=p3_1705311821_p9worQnaTtWB52AA&check_in=","line_color":"b"},
     {"name":"Ours","url":"https://www.airbnb.co.uk/rooms/991919969842748351?source_impression_id=p3_1705313120_c%2Fm2yGmapv9ksHVg&check_in=","line_color":"y"}
     ]


def getBnb(datalist):
   
    if datalist == "sky":
        datalist = sky
    else:
        datalist = hunter
    # print("DATALIST", datalist)
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

    getRates(datalist,arrivalDate, departureDate,min_nights,num_days,driver)
    
    plt.rcParams['figure.figsize'] = [12, 7]    
    plt.legend()
    plt.xlabel("DATE",fontweight="bold")
    plt.ylabel("RATE/NIGHT",fontweight="bold")
    plt.title(f"RATE COMPARISON {choice} From {arrFileName}",fontweight="bold")
    plt.ylim(100,500)
    plt.xticks(rotation=45)  
    myFmt = mdates.DateFormatter('%d / %m')
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.savefig(f"{choice} {arrFileName}.png")
    plt.show()


choice = input("Enter 'sky' for Sky Garden or 'hunt' for Hunter House : ")
getBnb(choice)



