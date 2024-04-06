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
     {"name":"Bloomson","url":"https://www.airbnb.co.uk/rooms/1077423177222957828?source_impression_id=p3_1712150698_B9d6DRwQYwiSlIGc&check_in=","line_color":"b"},
     {"name":"Tracy","url":"https://www.airbnb.co.uk/rooms/1002010727603598593?source_impression_id=p3_1712153527_mBbNtthTyJ1n0cuu&check_in=", "line_color": "orange"},
     {"name":"Ours","url":"https://www.airbnb.co.uk/rooms/1046907771076731775?source_impression_id=p3_1704451469_3qliydVyTnmWa7FH&check_in=","line_color":"y"},
     ]

#HUNTER
hunter=[
    {"name":"Charm", "url":"https://www.airbnb.co.uk/rooms/919494818502148128?source_impression_id=p3_1705312955_Qq3gYbrhzJIcQ90A&check_in=","line_color":"r"},
     {"name":"Vintage","url":"https://www.airbnb.co.uk/rooms/901306741280213973?source_impression_id=p3_1705312818_1cWKDpsOurb3ssZD&check_in=","line_color":"g"},
     {"name":"Hunter","url":"https://www.airbnb.co.uk/rooms/903131518446432064?source_impression_id=p3_1705311821_p9worQnaTtWB52AA&check_in=","line_color":"b"},
     {"name":"Ours","url":"https://www.airbnb.co.uk/rooms/991919969842748351?source_impression_id=p3_1705313120_c%2Fm2yGmapv9ksHVg&check_in=","line_color":"y"}
     ]

prince=[
    {"name":"Richard", "url":"https://www.airbnb.co.uk/rooms/1089937683235156136?source_impression_id=p3_1711897692_9Muqcs%2FJe2CUBC%2Bp&check_in=","line_color":"r"},
     {"name":"James","url":"https://www.airbnb.co.uk/rooms/839049066394923811?source_impression_id=p3_1712155883_JxD%2FYJ282oelANG8&check_in=","line_color":"g"},
     {"name":"John","url":"https://www.airbnb.co.uk/rooms/1035252707118091218?source_impression_id=p3_1711898457_i1f8UFewhDAgVuDS&check_in=","line_color":"b"},
     {"name":"Anna","url":"https://www.airbnb.co.uk/rooms/41347455?source_impression_id=p3_1711898456_X8V6jGQbb5Mv9n4g&check_in=", "line_color": "orange"},
     {"name":"Gianni","url":"https://www.airbnb.co.uk/rooms/24349122?source_impression_id=p3_1711898457_5FlY9H4NthjB8G8M&check_in=", "line_color": "purple"},
     {"name":"Ours","url":"https://www.airbnb.co.uk/rooms/1110055308129837928?source_impression_id=p3_1711899452_VLF2b6atGPBzhTWn&check_in=","line_color":"y"},
]


def getBnb(datalist):
   
    if datalist == "sky":
        datalist = sky
    elif datalist == "prince":
        datalist = prince
    else:
        datalist = hunter
    # print("DATALIST", datalist)
    arrivalDate = input("date (dd-mm-yyyy) : ")
    num_days = input("Number of days : ")
    min_nights=int(input("Minimum nigths : "))
    arrivalDate = datetime.strptime(arrivalDate,"%d-%m-%Y")
    nights = timedelta(days=min_nights)
    arrFileName=arrivalDate.strftime("%m-%d-%Y")
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
    plt.title(f"Rate Comparison {choice} From {arrFileName}",fontweight="bold")
    plt.ylim(150,600)
    plt.xticks(rotation=45)  
    myFmt = mdates.DateFormatter('%m / %d')
    plt.gca().xaxis.set_major_formatter(myFmt)
    # plt.savefig(f"graph/{choice} {arrFileName}.png")
    plt.savefig(f"graph/test {arrFileName}.png")
    plt.show()


choice = input("Enter 'sky' for Sky Garden or 'hunt' for Hunter House or 'prince' : ")
getBnb(choice)



