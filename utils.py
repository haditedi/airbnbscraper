from datetime import datetime, timedelta

def addOneDay(element, min_nights):
    arrivalDate = datetime.strptime(element,"%Y-%m-%d")
    arrivalDate += timedelta(days=1)
    nights = timedelta(days=min_nights)
    departureDate = arrivalDate+nights
    departureDate = departureDate.strftime("%Y-%m-%d")
    arrivalDate = arrivalDate.strftime("%Y-%m-%d")
    return {"arrivalDate":arrivalDate, "departureDate":departureDate}

