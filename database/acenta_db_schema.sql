-- Çelebi Seyehat Acentası Tablo Şeması

-- DROP TABLE customer;
CREATE TABLE customer (
	cName    			varchar(25) not null, 
	cSurname    	    varchar(30) not null,
	cID                 bigint not null primary key,
    cPoint              int not null
);

-- DROP TABLE otel;
CREATE TABLE otel (
	oName    			varchar(25) not null, 
	oRegion    	        varchar(30) not null,
	oPrice              int not null,
    oID                 bigint not null primary key
);

-- DROP TABLE rezervation;
CREATE TABLE rezervation (
	rCustomerID         bigint not null primary key,
	rOtelName    	    varchar(30) not null,
	rTime               time not null
);

-- DROP TABLE transportation;
CREATE TABLE transportation (
	tCompany    	    varchar(25) not null,
	tPrice              int not null,
    tFrom               varchar(25) not null,
    tTo                 varchar(25) not null,
    tBonus              numeric(2,2) not null
);

-- DROP TABLE booking;
CREATE TABLE booking (
    bCustomerID         bigint not null primary key,
	bCompanyName    	varchar(25) not null,
    bTime               time not null,
    bFrom               varchar(25) not null,
    bTo                 varchar(25) not null
);