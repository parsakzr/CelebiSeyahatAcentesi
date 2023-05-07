from app import app
from Domain import BookingOptions, Ticket, HotelBooking, TravelCompany, Hotel

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/ticket')
def ticket():
    # returns json of ticket
    return "Ticket"