from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime, timedelta
from utils import getRates
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from competitorlist import sky, hunter, prince, bowden


def getBnb(datalist):
    graph_name = datalist.capitalize()
    if datalist == "sky":
        datalist = sky
    elif datalist == "prince":
        datalist = prince
    elif datalist == "bowden":
        datalist = bowden
    else:
        datalist = hunter
    # datalist = sky
    # print("DATALIST", datalist)
    arrivalDate = input("date (dd-mm-yyyy) : ")
    # arrivalDate = "12-05-2024"
    num_days = input("Number of days : ")
    # num_days = 4
    min_nights = int(input("Minimum nigths : "))
    # min_nights = 4
    arrivalDate = datetime.strptime(arrivalDate, "%d-%m-%Y")
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

    getRates(datalist, arrivalDate, departureDate, min_nights, num_days, driver)

    plt.rcParams["figure.figsize"] = [12, 7]
    plt.legend()
    plt.xlabel("DATE", fontweight="bold")
    plt.ylabel("RATE/NIGHT", fontweight="bold")
    plt.title(
        f"Rate Comparison {graph_name} From {arrFileName} until {graphDepartureDate}",
        fontweight="bold",
    )
    plt.ylim(150, 650)
    plt.xticks(rotation=45)
    myFmt = mdates.DateFormatter("%d / %m")
    plt.gca().xaxis.set_major_formatter(myFmt)
    file_time = datetime.now().strftime("%H-%M-%S")
    today_date = datetime.now().strftime("%d-%m-%Y")
    plt.savefig(
        f"graph/{graph_name} {arrFileName} updated {today_date} {file_time}.png"
    )
    print("DONE")
    plt.show()


choice = input("Enter 'sky' for Sky Garden or 'hunter' for Hunter House or 'prince' : ")
getBnb(choice)
