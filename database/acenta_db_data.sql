-- -- Çelebi Seyehat Acentası Tablo Şeması Data

-- data for customer table

INSERT INTO customer(cName, totalPoints) VALUES ('Tom Hanks', 0);
INSERT INTO customer(cName, totalPoints) VALUES ('Leonardo DiCaprio', 0);
INSERT INTO customer(cName, totalPoints) VALUES ('Brad Pitt', 0);
INSERT INTO customer(cName, totalPoints) VALUES ('Johnny Depp', 0);
INSERT INTO customer(cName, totalPoints) VALUES ('Robert Downey Jr.', 0);

-- data for hotel table

INSERT INTO hotel(hName, region, address, bonus) VALUES ('Burj Al Arab','Dubai','Jumeirah Beach Road, Dubai, United Arab Emirates',0.3);
INSERT INTO hotel(hName, region, address, bonus) VALUES ('Bellagio','Las Vegas','3600 S Las Vegas Blvd, Las Vegas, NV 89109, United States',0.2);
INSERT INTO hotel(hName, region, address, bonus) VALUES ('The Plaza','New York','768 5th Ave, New York, NY 10019, United States',0.2);
INSERT INTO hotel(hName, region, address, bonus) VALUES ('Marina Bay Sands Hotel','Singapur','10 Bayfront Ave, Singapore 018956',0.1);
INSERT INTO hotel(hName, region, address, bonus) VALUES ('Çırağan Kempinski','İstanbul','Çırağan Cd. 32, 34349 Beşiktaş/İstanbul',0.2);


-- data for travelCompany table
INSERT INTO travelCompany(tcName, wayOfTravel, bonus) VALUES ('Uçan Türk Özel Havayolu','Flight',0.1);
INSERT INTO travelCompany(tcName, wayOfTravel, bonus) VALUES ('TCDD','Train',0.2);
INSERT INTO travelCompany(tcName, wayOfTravel, bonus) VALUES ('YTUR','Bus',0.1);
INSERT INTO travelCompany(tcName, wayOfTravel, bonus) VALUES ('IDO','Ferry',0.1);


-- data for hotelStay table

INSERT INTO hotelStay(hotel, hsPrice) VALUES (1, 1500);
INSERT INTO hotelStay(hotel, hsPrice) VALUES (2, 1000);
INSERT INTO hotelStay(hotel, hsPrice) VALUES (3, 1500);
INSERT INTO hotelStay(hotel, hsPrice) VALUES (4, 1500);
INSERT INTO hotelStay(hotel, hsPrice) VALUES (5, 1500);
INSERT INTO hotelStay(hotel, hsPrice) VALUES (5, 1000);
INSERT INTO hotelStay(hotel, hsPrice) VALUES (5, 500);


-- data for transportation table

INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'İstanbul','Singapur','2020-12-12 08:30:00',1000);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'İstanbul','New York','2020-12-12 08:30:00',1500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'İstanbul','Las Vegas','2020-12-12 08:30:00',2000);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'İstanbul','Dubai','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Dubai','Las Vegas','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Dubai','New York','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Dubai','Singapur','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Dubai','İstanbul','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Las Vegas','Dubai','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Las Vegas','New York','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Las Vegas','Singapur','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'Las Vegas','İstanbul','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'New York','Dubai','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'New York','Las Vegas','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'New York','Singapur','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (1,'New York','İstanbul','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'İstanbul','Ankara','2020-12-12 08:30:00',200);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'İstanbul','İzmir','2020-12-12 08:30:00',300);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'İstanbul','Antalya','2020-12-12 08:30:00',400);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'İstanbul','Samsun','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'Ankara','İstanbul','2020-12-12 08:30:00',200);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'İzmir','İstanbul','2020-12-12 08:30:00',300);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'Antalya','İstanbul','2020-12-12 08:30:00',400);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (2,'Samsun','İstanbul','2020-12-12 08:30:00',500);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'İstanbul','Ankara','2020-12-12 08:30:00',100);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'İstanbul','İzmir','2020-12-12 08:30:00',200);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'İstanbul','Antalya','2020-12-12 08:30:00',300);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'İstanbul','Samsun','2020-12-12 08:30:00',400);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'Ankara','İstanbul','2020-12-12 08:30:00',100);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'İzmir','İstanbul','2020-12-12 08:30:00',200);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'Antalya','İstanbul','2020-12-12 08:30:00',300);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (3,'Samsun','İstanbul','2020-12-12 08:30:00',400);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (4,'İstanbul','Bursa','2020-12-12 08:30:00',100);
INSERT INTO transport(travelCompany, tFrom, tTo, tDatetime, tPrice) VALUES (4,'Bursa','İstanbul','2020-12-12 08:30:00',100);

