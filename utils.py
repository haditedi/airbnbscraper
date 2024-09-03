import csv

from datetime import datetime, timedelta, date
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def addOneDay(element, min_nights):
    arrivalDate = datetime.strptime(element, "%Y-%m-%d")
    arrivalDate += timedelta(days=1)
    nights = timedelta(days=int(min_nights))
    departureDate = arrivalDate + nights
    departureDate = departureDate.strftime("%Y-%m-%d")
    arrivalDate = arrivalDate.strftime("%Y-%m-%d")
    return {"arrivalDate": arrivalDate, "departureDate": departureDate}


def locationName(graph):
    if graph == "sky":
        return "Nine Elms"
    elif graph == "hunter":
        return "Bloomsbury"
    else:
        return "Queensway"


def writeToCsv(skyline_x, skyline_y, property_name, date, time):
    fields = ["Date", "Rate/night"]
    merged_list = []
    for i in range(len(skyline_x)):
        thelist = []
        thelist.append(skyline_x[i])
        thelist.append(skyline_y[i])
        merged_list.append(thelist)
    filename = f"csv/{property_name} {date} {time}.csv"
    # writing to csv file
    with open(filename, "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(merged_list)


def getRates(
    listProperty,
    arrivalDate,
    departureDate,
    min_nights,
    num_days,
    driver,
    graph_name,
    arrFileName,
    graphDepartureDate,
):
    min_nights = int(min_nights)
    file_time = datetime.now().strftime("%H-%M-%S")
    today_date = datetime.now().strftime("%d-%m-%Y")

    for index in range(len(listProperty)):
        for key in listProperty[index]:
            property_name = listProperty[index]["name"]
            line_color = listProperty[index]["line_color"]
            if key == "url":
                url = listProperty[index][key]
                print("PROPERTY", property_name)
                # print("LINE COLOR", line_color)
                skyline_x = []
                skyline_y = []
                initArrDate = arrivalDate
                initDepDate = departureDate

                for _ in range(int(num_days)):
                    # print("ARRIVAL DATE", arrivalDate)

                    try:
                        new_url = f"{url}{arrivalDate}&guests=4&adults=4&check_out={departureDate}"

                        driver.get(new_url)

                        try:
                            total_price = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located(
                                    (
                                        By.XPATH,
                                        "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/section/div[2]/div/span[2]/span[1]/span",
                                    )
                                )
                            )
                            total_price = total_price.get_attribute("innerHTML")
                            total_price = total_price.replace("£", "")

                            price_per_night = 0
                            if len(total_price) > 3:
                                total_price = total_price.replace(",", "")
                                total_price = int(total_price.strip())
                                price_per_night = total_price / min_nights
                            else:
                                total_price = int(total_price.strip())
                                price_per_night = total_price / min_nights

                            print("Rate/night £", price_per_night)
                            skyline_y.append(price_per_night)

                        except Exception as e:
                            # print("EXCEPTION - possibly No rate")
                            skyline_y.append(None)

                        # total_price = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/section/div[2]/div/span[2]/span[1]/span")
                        # print("TOTAL PRICE", total_price.text)

                    except Exception as e:
                        # print("EXCEPTION possible URL error", e)
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
                print(property_name, skyline_x, skyline_y)

                x_data = [date.fromisoformat(i) for i in skyline_x]
                x_data = np.array(x_data)

                y_data = np.array(skyline_y).astype(np.double)
                # plt.ylim(min(y_data),500)
                sky_mask = np.isfinite(y_data)
                plt.plot_date(
                    x_data[sky_mask],
                    y_data[sky_mask],
                    line_color,
                    marker="o",
                    label=property_name,
                )
                writeToCsv(skyline_x, skyline_y, property_name, today_date, file_time)

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

    plt.savefig(
        f"graph/{graph_name} {arrFileName} updated {today_date} {file_time}.svg"
    )
    print("DONE")
    plt.close()
    # plt.show()
    driver.quit()
    return
