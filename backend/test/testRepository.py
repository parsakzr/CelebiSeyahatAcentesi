import app.Repository as Repository
from app.Domain import Customer, Hotel, HotelStay, Transport, TravelCompany
import pytest


@pytest.fixture
def repository():
    return Repository.Repository()


pytest.testCustomerID = 0
pytest.testTravelCompanyID = 0
pytest.testHotelID = 0
pytest.testTransportID = 0
pytest.testHotelStayID = 0


def test_createCustomer(repository):
    pytest.testCustomerID = repository.createCustomer("Test Customer")
    cur = repository.conn.cursor()
    cur.execute("SELECT cID FROM customer WHERE cName = 'Test Customer'")
    assert cur.fetchone()[0] == pytest.testCustomerID


def test_createTravelCompany(repository):
    pytest.testTravelCompanyID = repository.createTravelCompany(
        "Test Travel Company", "Flight", 0
    )
    cur = repository.conn.cursor()
    cur.execute("SELECT tcID FROM travelcompany WHERE tcName = 'Test Travel Company'")
    assert cur.fetchone()[0] == pytest.testTravelCompanyID


def test_createHotel(repository):
    pytest.testHotelID = repository.createHotel(
        "Test Hotel", "Test Region", "Test Address", 0
    )
    cur = repository.conn.cursor()
    cur.execute("SELECT hID FROM hotel WHERE hName = 'Test Hotel'")
    assert cur.fetchone()[0] == pytest.testHotelID


def test_createTransport(repository):
    print(f"On createTransport: {pytest.testTravelCompanyID=}")
    pytest.testTransportID = repository.createTransport(
        pytest.testTravelCompanyID, "Test From", "Test To", "2000-01-01 12:00:00", 1000
    )
    cur = repository.conn.cursor()
    cur.execute("SELECT tID FROM transport WHERE travelCompany = 1")
    assert cur.fetchone()[0] == pytest.testTransportID


def test_createHotelStay(repository):
    pytest.testHotelStayID = repository.createHotelStay(pytest.testHotelID, 1000)
    cur = repository.conn.cursor()
    cur.execute("SELECT hsID FROM hotelstay WHERE hotel = %s", (pytest.testHotelID,))
    assert cur.fetchone()[0] == pytest.testHotelStayID


def test_getCustomer(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM customer WHERE cID = %s", (pytest.testCustomerID,))
    result = Customer(*cur.fetchone())
    assert repository.getCustomer(pytest.testCustomerID) == result


def test_getCustomerByName(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM customer WHERE cName = 'Test Customer'")
    result = Customer(*cur.fetchone())
    assert repository.getCustomerByName("Test Customer") == result


def test_getTravelCompany(repository):
    cur = repository.conn.cursor()
    cur.execute(
        "SELECT * FROM travelcompany WHERE tcID = %s", (pytest.testTravelCompanyID,)
    )
    result = TravelCompany(*cur.fetchone())
    assert repository.getTravelCompany(pytest.testTravelCompanyID) == result


def test_getHotel(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM hotel WHERE hID = %s", (pytest.testHotelID,))
    result = Hotel(*cur.fetchone())
    assert repository.getHotel(pytest.testHotelID) == result


def test_getTransport(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM transport WHERE tID = %s", (pytest.testTransportID,))
    result = Transport(*cur.fetchone())
    assert repository.getTransport(pytest.testTransportID) == result


def test_getHotelStay(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM hotelstay WHERE hsID = 1")
    result = HotelStay(*cur.fetchone())
    assert repository.getHotelStay(1) == result


def test_getAllHotelStaysBy_region(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM hotel WHERE Region = 'Test Region'")
    assert repository.getAllHotelsBy("Test Region") == cur.fetchall()


def test_getAllTransportsBy_travelCompany(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM transport WHERE travelCompany = 1")
    assert repository.getAllTransportsBy("Test Travel Company") == cur.fetchall()


def test_getAllTransportsBy_tTotFrom(repository):
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM transport WHERE tFrom = 'Test From' AND tTo = 'Test To'")
    assert (
        repository.getAllTransportsBy(tFrom="Test From", tTo="Test To")
        == cur.fetchall()
    )


def test_DeleteCustomer(repository):
    repository.deleteCustomer(pytest.testCustomerID)
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM customer WHERE cID = %s", (pytest.testCustomerID,))
    assert cur.fetchone() is None


def test_DeleteTransport(repository):
    repository.deleteTransport(pytest.testTransportID)
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM transport WHERE tID = %s", (pytest.testTransportID,))
    assert cur.fetchone() is None


def test_DeleteHotelStay(repository):
    repository.deleteHotelStay(pytest.testHotelStayID)
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM hotelstay WHERE hsID = %s", (pytest.testHotelStayID,))
    assert cur.fetchone() is None


def test_DeleteTravelCompany(repository):
    repository.deleteTravelCompany(pytest.testTravelCompanyID)
    cur = repository.conn.cursor()
    cur.execute(
        "SELECT * FROM travelcompany WHERE tcID = %s", (pytest.testTravelCompanyID,)
    )
    assert cur.fetchone() is None


def test_DeleteHotel(repository):
    repository.deleteHotel(pytest.testHotelID)
    cur = repository.conn.cursor()
    cur.execute("SELECT * FROM hotel WHERE hID = %s", (pytest.testHotelID,))
    assert cur.fetchone() is None
