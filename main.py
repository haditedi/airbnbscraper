from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime, timedelta, date
from utils import getRates, locationName
import matplotlib.pyplot as plt

from competitorlist import sky, hunter, prince
from checkpagevalid import check_valid


def getBnb(datalist):
    graph_name = locationName(datalist)
    print(graph_name)
    if datalist == "sky":
        datalist = sky
    elif datalist == "prince":
        datalist = prince
    else:
        datalist = hunter

    # arrivalDate = input("date (dd-mm-yyyy) : ")
    # arrivalDate = "12-05-2024"
    # num_days = input("Number of days : ")
    num_days = 28
    # min_nights = int(input("Minimum nigths : "))
    min_nights = 4
    check_valid(datalist)
    desiredDate = date.today()
    addday = timedelta(days=1)
    arrivalDate = desiredDate + addday
    # arrivalDate = datetime.strptime(arrivalDate, "%d-%m-%Y")
    nights = timedelta(days=min_nights)
    arrFileName = arrivalDate.strftime("%d-%m-%Y")
    departureDate = arrivalDate + nights
    graphDays = timedelta(days=int(num_days))
    graphDepartureDate = arrivalDate + graphDays
    departureDate = departureDate.strftime("%Y-%m-%d")
    graphDepartureDate = graphDepartureDate.strftime("%d-%m-%Y")
    arrivalDate = arrivalDate.strftime("%Y-%m-%d")

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    getRates(
        datalist,
        arrivalDate,
        departureDate,
        min_nights,
        num_days,
        driver,
        graph_name,
        arrFileName,
        graphDepartureDate,
    )


# choice = input("Enter 'sky' for Sky Garden or 'hunter' for Hunter House or 'prince' : ")
mylist = ["sky", "hunter", "prince"]
for x in mylist:
    getBnb(x)
