import requests
from data_manager import DataManager

class FlightData:
    header = {
        "apikey" : "Ocyl0cxQrL0PsTnLY59TC-HYB1ETHxKx"
    }
    URL = "https://api.tequila.kiwi.com"
   
    def __init__(self, data_manager_object: DataManager) -> None:
        self.data_manager_object = data_manager_object

    def getIATA(self, dict_to_add_IATA: dict):
        for city,id in dict_to_add_IATA.items():
            self.payload = {
            "term" : city
            }
            response = requests.get(url = f"{FlightData.URL}/locations/query", params = self.payload, headers = FlightData.header)
            IATA_code = response.json()["locations"][0]["code"]
            self.data_manager_object.postIATA(id, IATA_code)

    def print_dict(self):
        city_dict = self.data_manager_object.getJson()    
        return city_dict