# Importing Modules
import pandas as pd

#Reading the File
df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books the hotel and changes the availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks the availability of the hotel"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class TicketConfirmation:
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel = hotel_name

    def generate(self):
        content = f"""
        Thank you for your booking our hotel!
        Here are your booking details:
        Name:{self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content


# Credit Card Class
class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = CreditCard(number="1234")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        TicketConfirmation = TicketConfirmation(customer_name=name, hotel_name=hotel)
        print(TicketConfirmation.generate())
    else:
        print("There was a problem with your Payment")

else:
    print("Hotel is not available.")
