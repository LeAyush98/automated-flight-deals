from data_manager import DataManager
import requests
import datetime
from dateutil.relativedelta import *

class FlightSearch:
    header = {
        "apikey" : "Ocyl0cxQrL0PsTnLY59TC-HYB1ETHxKx"
        }
    URL = "https://api.tequila.kiwi.com/v2/search"
    
    def __init__(self, data_manager_object: DataManager) -> None:
        self.data_manager_object = data_manager_object

    def get_flights(self, price_dict: dict):
        message_list = []
        for city, price in price_dict.items():
            #print(f"{city} has lowest price of {price} euros")
            date = datetime.datetime.now()
            date_in_half_year = date + relativedelta(months=+6)
            date = date.strftime("%d/%m/%Y")
            date_in_half_year = date_in_half_year.strftime("%d/%m/%Y")
            params = {
                "fly_from" : "airport:DEL", # Testing for london instead of delhi for now.
                "fly_to": city, #iataCode column in sheety
                "date_from": date,
                "date_to": date_in_half_year,
                "sort": "price",
                "limit": 5,
                "price_from": 10,
                "price_to": int(price) # lowest price column in sheety
            }
            self.response = requests.get(url=FlightSearch.URL, params=params, headers=FlightSearch.header)
            try:
                departure = self.response.json()["data"][0]["route"][0]["local_departure"]
                date_for_departure = departure[0:10]
                time_for_departure = departure[12:16]
                price = (int(self.response.json()["data"][0]["price"]) * 87.53)
            except IndexError: 
               message_list.append(f"All flights to {city} are over the budget")
            else:  
               message_list.append(f"You can go to {city} from Indira Gandhi International Airport, Delhi on {date_for_departure} at {time_for_departure} local time, for {price} INR")
        return message_list

    def get_price_dict(self):
       price_dict =  self.data_manager_object.make_dict_for_search()
       return price_dict