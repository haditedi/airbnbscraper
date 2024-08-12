from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime, timedelta
from utils import getRates
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# SKY
sky = [
    {
        "name": "Relocate",
        "url": "https://www.airbnb.co.uk/rooms/871040174926257448?source_impression_id=p3_1704450998_hM8uppOkkjhY8NdK&check_in=",
        "line_color": "r",
    },
    {
        "name": "Skyline",
        "url": "https://www.airbnb.co.uk/rooms/893933063998940096?source_impression_id=p3_1704361618_0j1jiCryQcZYdVPl&check_in=",
        "line_color": "g",
    },
    {
        "name": "Bloomson",
        "url": "https://www.airbnb.co.uk/rooms/1077423177222957828?source_impression_id=p3_1712150698_B9d6DRwQYwiSlIGc&check_in=",
        "line_color": "b",
    },
    {
        "name": "SkyGarden Eli",
        "url": "https://www.airbnb.co.uk/rooms/736788404696913896?source_impression_id=p3_1723431436_P3sSYsoqENOVl5H5&check_in=",
        "line_color": "orange",
    },
    {
        "name": "Can And Aleksandra",
        "url": "https://www.airbnb.co.uk/rooms/22352403?source_impression_id=p3_1723431823_P3Vr9Hboh3fp-dn6&check_in=",
        "line_color": "purple",
    },
    {
        "name": "SkyGarden F",
        "url": "https://www.airbnb.co.uk/rooms/1046907771076731775?source_impression_id=p3_1704451469_3qliydVyTnmWa7FH&check_in=",
        "line_color": "yellow",
    },
    {
        "name": "Xhorxhina",
        "url": "https://www.airbnb.co.uk/rooms/45266901?source_impression_id=p3_1723432519_P3VDb-I6ci56atQL&check_in=",
        "line_color": "pink",
    },
]

# HUNTER
hunter = [
    {
        "name": "Harry",
        "url": "https://www.airbnb.co.uk/rooms/901306741280213973?source_impression_id=p3_1705312818_1cWKDpsOurb3ssZD&check_in=",
        "line_color": "g",
    },
    {
        "name": "Oneil",
        "url": "https://www.airbnb.co.uk/rooms/903131518446432064?source_impression_id=p3_1705311821_p9worQnaTtWB52AA&check_in=",
        "line_color": "b",
    },
    #  {"name":"Hunter8","url":"https://www.airbnb.co.uk/rooms/991919969842748351?source_impression_id=p3_1705313120_c%2Fm2yGmapv9ksHVg&check_in=","line_color":"y"},
    {
        "name": "Dilen",
        "url": "https://www.airbnb.co.uk/rooms/612203853376860930?source_impression_id=p3_1715678296_x0bfS%2BYfuLm40ZcW&check_in=",
        "line_color": "orange",
    },
    {
        "name": "CStays",
        "url": "https://www.airbnb.co.uk/rooms/1123044516463216828?source_impression_id=p3_1715678482_2p1XGU5JyleogkTO&check_in=",
        "line_color": "purple",
    },
]

prince = [
    {
        "name": "Ramos",
        "url": "https://www.airbnb.co.uk/rooms/1160720252603364860?source_impression_id=p3_1712155883_JxD%2FYJ282oelANG8&check_in=",
        "line_color": "g",
    },
    {
        "name": "Haifi",
        "url": "https://www.airbnb.co.uk/rooms/1129020937604624995?source_impression_id=p3_1711898457_i1f8UFewhDAgVuDS&check_in=",
        "line_color": "b",
    },
    {
        "name": "Hassan",
        "url": "https://www.airbnb.co.uk/rooms/52406093?source_impression_id=p3_1711898456_X8V6jGQbb5Mv9n4g&check_in=",
        "line_color": "orange",
    },
    {
        "name": "Gianni",
        "url": "https://www.airbnb.co.uk/rooms/841073783967208304?source_impression_id=p3_1711898457_5FlY9H4NthjB8G8M&check_in=",
        "line_color": "purple",
    },
    {
        "name": "Lyandah",
        "url": "https://www.airbnb.co.uk/rooms/32623773?source_impression_id=p3_1717061367_sgv33kja84bav1HT&check_in=",
        "line_color": "r",
    },
    #  {"name":"Princes Sq","url":"https://www.airbnb.co.uk/rooms/1110055308129837928?source_impression_id=p3_1711899452_VLF2b6atGPBzhTWn&check_in=","line_color":"y"},
]

bowden = [
    {
        "name": "Dominic",
        "url": "https://www.airbnb.co.uk/rooms/1116057187762364001?source_impression_id=p3_1717739081_P3UYdriW0HcMgFZH&check_in=",
        "line_color": "g",
    },
    {
        "name": "Tim",
        "url": "https://www.airbnb.co.uk/rooms/1143484057714978646?source_impression_id=p3_1717739648_P3hJs4odKBU093-G&check_in=",
        "line_color": "b",
    },
    {
        "name": "Capital",
        "url": "https://www.airbnb.co.uk/rooms/1171602217690580795?source_impression_id=p3_1717739914_P3Q0fIyPfxJB2iI4&check_in=",
        "line_color": "orange",
    },
    {
        "name": "Ramona",
        "url": "https://www.airbnb.co.uk/rooms/44127966?&source_impression_id=p3_1717740580_P3_8EIp9PPYPKIB8&check_in=",
        "line_color": "purple",
    },
    {
        "name": "Alice",
        "url": "https://www.airbnb.co.uk/rooms/1161596523852226746?&source_impression_id=p3_1717740740_P3BlB0g2JGbY32sx&check_in=",
        "line_color": "r",
    },
]


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
