import requests

r = requests.get("https://www.airbnb.co.uk/rooms/1110055308129837928?adults=4&location=Queensway%2C%20London%2C%20UK&check_in=2024-04-12&source_impression_id=p3_1711535612_lPskQktlaRwouRSJ&previous_page_section_name=1001&federated_search_id=cab98d48-a759-4c4b-b85a-224b2ed8e54a&guests=1&check_out=2024-04-15")
print(r.content)