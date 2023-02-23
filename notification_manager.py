import smtplib
from flight_search import FlightSearch

class NotificationManager:
    def __init__(self) -> None:
        self.EMAIL = "ayu.sharma798@gmail.com"
        self.PASSWORD = "NotGonnaWriteMyPasswordHere"

    def send_flight_mail(self, message_list: list):
        for index, message in enumerate(message_list):
            message_list[index] = message + "\n\n"
        message_string = "".join(message_list)

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=self.EMAIL, password=self.PASSWORD)
        connection.sendmail(
            from_addr=self.EMAIL,
            to_addrs=self.EMAIL,
            msg=f"Subject:Pack your bags!\n\n{message_string}\n\nThanks and regards,\nPython Bot,\nAyush's Personal Assistant,\nInside the HDD,\nDelhi 110051,\nIndia"
        )
        connection.close()
