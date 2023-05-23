-- Çelebi Seyehat Acentası Tablo Şeması

-- DROP TABLE customer;
CREATE TABLE customer (
	cID                 serial not null primary key,
	cName    			varchar(64) not null, 
    totalPoints         int not null
);


-- DROP TABLE hotel;
CREATE TABLE hotel (
	hID                 serial not null primary key,
	hName    			varchar(64) not null, 
	region    	        varchar(64) not null,
	address            	varchar(64),
	bonus             	numeric(2,2) not null
);

-- DROP TABLE travelCompany;
CREATE TABLE travelCompany (
	tcID                serial not null primary key,
	tcName    			varchar(64) not null, 
	wayOfTravel    		varchar(16) not null, 
	bonus              	numeric(2,2) not null
);


-- DROP TABLE hotelStay;
CREATE TABLE hotelStay (
	hsID   	    		serial not null primary key,
	hotel				integer not null references hotel(hID),
	hsPrice             int not null -- per night per person
);

-- DROP TABLE transport;
CREATE TABLE transport (
	tID   	    		serial not null primary key,
	travelCompany		integer not null references travelCompany(tcID),
    tFrom               varchar(64) not null,
    tTo                 varchar(64) not null,
	tDatetime			timestamp not null,
	tPrice              int not null -- per person
);

-- DROP TABLE booking;
CREATE TABLE booking (
	bID				    serial not null primary key,
    customerID         	integer not null references customer(cID),
	typeOfBooking       char not null, -- 'H' for hotel, 'T' for transport
	hotelStay         	integer references hotelStay(hsID),
	transport			integer references transport(tID),
	fromDate			timestamp not null,
	toDate				timestamp not null,
	numOfPassengers    	int not null,
	totalPrice		  	int,
	totalBonus          numeric(2,2)
);