import requests

class DataManager:
    URL = "https://api.sheety.co/515c8dde0411d2116707dbb91f6d6964/flightDeals/prices"
    header = {
        "Authorization": "Bearer ssajpperwluwnrxh"
    }
    
    def __init__(self) -> None:
        pass
    def postIATA(self, id, IATA_code):
        self.payload = {
            "price": 
            {
            "iataCode": IATA_code   
            }         
        }
        self.response = requests.put(url = f"{DataManager.URL}/{id}", json = self.payload,headers = DataManager.header)    

    def getJson(self):
        self.response = requests.get(url = DataManager.URL, headers = DataManager.header)
        data = self.response.json()
        return self.make_dict(data)

    def make_dict(self, data):
        city_dict = {values['city']:values['id'] for values in data["prices"]}    
        return city_dict

    def make_dict_for_search(self):
        self.response = requests.get(url = DataManager.URL, headers = DataManager.header)
        data = self.response.json()
        price_dict = {values['iataCode']:values['lowestPrice'] for values in data["prices"]}
        return price_dict
        