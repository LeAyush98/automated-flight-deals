import data_manager
import flight_data
import flight_search
import notification_manager

sheet_data = data_manager.DataManager()
flight_fill_sheet = flight_data.FlightData(sheet_data)
flight_search_object = flight_search.FlightSearch(sheet_data)
send_mail = notification_manager.NotificationManager()

# dict_to_add_IATA = flight_fill_sheet.print_dict()

# flight_fill_sheet.getIATA(dict_to_add_IATA)

#flight_search_object.get_flights()

#flight_search_object.get_price_dict()

message_list = flight_search_object.get_flights(flight_search_object.get_price_dict())

send_mail.send_flight_mail(message_list)
