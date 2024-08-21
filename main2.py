#Import pandas
import pandas as pd

#Load the datasets
df = pd.read_csv("hotels.csv", dtype={"id": str})

#Create class Hotel and define the functions
class Hotel:
    watermark = "The Real Estate"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Books the hotel and changes the availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)
    def available(self):
        """Checks the availability of the hotel"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

# "@" is used for declaring the decorator

#Class Method
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

#Magic Method
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


#Create class TicketConfirmation and define the functions
class TicketConfirmation:
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel = hotel_name
    def generate(self):
        content = f"""
        Thank you for booking our hotel!
        Here are your booking details:
        Name:{self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content

#Property Method
    @property
    def get_customer_name(self):
        name = self.customer_name.strip()
        name  = name.title()
        return name

#Static Method
    @staticmethod
    def convert(amount):
        return amount * 1.2

#Magic Method



hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.available())


print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.get_hotel_count(data =df))


#Property Method
ticket = TicketConfirmation(customer_name="john KELLY smith ", hotel_name= hotel1)
print(ticket.get_customer_name)
print(ticket.generate())

#Static Method
converted =TicketConfirmation.convert(1000)
print(converted)

############ NOTE ###########
"""
_Instant Method
 
_Instant Variable

Class Variable

_ Static Method - Use to help instant method like utilities
it used @staticmethod

_ Magic Method (.__eq__):  for equating when 1 object has 2 ID
like hotel 1 and hotel has room 188


_ () is used to call function
- Property  of Class works as a variable, it uses @Property
generate() -Method is inside the class and hidden until it is called
generate_customer = Callable, it is variable - 

"""