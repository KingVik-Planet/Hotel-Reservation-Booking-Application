# **Hotel Reservation Booking Application.**
![Alt](https://groups360.com/wp-content/uploads/2022/01/groupsync-home-group-travel.jpg) Source :Group360

# Planning
1. Showing the user the list of the Hotel
2. Allow user to book the hotel of their choice
3. Send  the confirmation of the user's Hotel reservation

# Classes:
1. User
2. Hotel
3. Ticket Confirmation




# **Flight  Booking Application.**
![Alt](https://cdn.dribbble.com/users/7843013/screenshots/17245752/media/34f43714ccd28bb8beceb6f837d3ff5e.png) Source: UI Zone

## Planning Summary:
## Planning
- Showing the user the list of available flights
- Allow user to book the flight of their choice
- Send the confirmation of the user's flight reservation

## Classes:
- User
- Flight
- Ticket Confirmation




# **Planning**
## User Registration and Login;
this allows User to do the following:
1. Allow users to create an account or log in if they already have one.
2. Ensure secure authentication and user data protection.

## Showing the List of Available Flights
1. Provide a search interface for users to enter their travel details (departure, destination, dates, number of passengers, etc.).
2. Display a list of available flights based on the search criteria, with details like airline, flight number, departure/arrival time, and price.

## Flight Details and Selection

1. Allow users to click on a flight to view more details, such as seat availability, layovers, baggage policy, etc.
2. Enable users to select a flight and proceed to booking.

## Booking Process

1. Collect necessary passenger information (name, age, passport number, etc.).
2. Provide options for seat selection and additional services (e.g., meal preferences, extra baggage).
3. Display a summary of the booking details for user confirmation.


## Payment Integration

1. Integrate with payment gateways to securely process payments.
2. Allow multiple payment options (credit/debit cards, digital wallets, etc.).
3. Ensure secure handling of payment information.

## Ticket Confirmation and Receipt

1. Generate a booking confirmation once the payment is successful.
2. Send the booking confirmation and e-ticket to the user's email.
3. Allow users to download or print the ticket from their account.

## User Profile and Booking History

1. Provide a user profile section where users can update their personal information.
2. Allow users to view their booking history and manage upcoming trips.
C

# Classes:
#### User
- Attributes: userID, username, password, email, phoneNumber, address, paymentDetails
- Methods: register(), login(), updateProfile(), viewBookingHistory()


#### Flight
- Attributes: flightID, airline, flightNumber, departure, destination, departureTime, arrivalTime, price, seatAvailability
- Methods: searchFlights(), viewFlightDetails(), selectFlight()


#### Booking
- Attributes: bookingID, userID, flightID, passengerDetails, seatSelection, additionalServices, totalPrice, paymentStatus
- Methods: createBooking(), viewBookingSummary(), confirmBooking()


#### Payment
- Attributes: paymentID, bookingID, amount, paymentMethod, paymentStatus
- Methods: processPayment(), verifyPayment()


#### Ticket Confirmation
- Attributes: ticketID, bookingID, userID, flightDetails, passengerDetails, seatNumber, issueDate
- Methods: generateTicket(), sendConfirmationEmail(), downloadTicket()


## Detailed Class Explanations:
### User Class

- register(): Allows a new user to create an account by providing necessary details.
- login(): Authenticates the user based on the username and password.
- updateProfile(): Enables the user to update their personal information.
- viewBookingHistory(): Retrieves and displays the user's past and upcoming bookings.

### Flight Class

 - searchFlights(): Searches for available flights based on user input.
- viewFlightDetails(): Displays detailed information about a selected flight.
- selectFlight(): Allows the user to select a flight for booking.

### Booking Class

- createBooking(): Initiates a new booking by collecting passenger details and selected services.
- viewBookingSummary(): Provides a summary of the booking details for user confirmation.
- confirmBooking(): Finalizes the booking and updates the booking status.

### Payment Class

- processPayment(): Handles the payment process using the selected payment method.
- verifyPayment(): Verifies the payment status and updates the booking accordingly.

### Ticket Confirmation Class
- generateTicket(): Generates an e-ticket once the booking is confirmed.
- sendConfirmationEmail(): Sends the booking confirmation and e-ticket to the user's email.
- downloadTicket(): Allows the user to download or print the e-ticket from their account.
