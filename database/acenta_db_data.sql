-- -- Çelebi Seyehat Acentası Tablo Şeması Data

-- datas of customer table
--                          (cName, cSurname, cID, cPoint)
INSERT INTO customer VALUES ('Tom','Hanks',18034035,10);
INSERT INTO customer VALUES ('Jack','Nicholson',22054045,20);
INSERT INTO customer VALUES ('Benedict','Cumberbatch',12054042,5);
INSERT INTO customer VALUES ('Leonardo','DiCaprio',42054545,8);
INSERT INTO customer VALUES ('Christian','Bale',25089404,8);
INSERT INTO customer VALUES ('Natalie','Portman',14254054,4);
INSERT INTO customer VALUES ('Lena','Headey',10283892,4);

-- datas of otel table
--                      (oName, oRegion, oPrice, oID)
INSERT INTO otel VALUES ('Burj Al Arab','Dubai',1000,1414);
INSERT INTO otel VALUES ('Bellagio','Las Vegas',800,8625);
INSERT INTO otel VALUES ('The Plaza','New York',600,7423);
INSERT INTO otel VALUES ('Marina Bay Sands Hotel','Singapur',800,9596);
INSERT INTO otel VALUES ('Çırağan Kempinski','İstanbul',1500,3434);

-- datas of transportation table
--                                (tCompany, tPrice, tFrom, tTo, tBonus)
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'İstanbul','Singapur',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'İstanbul','New York',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'İstanbul','Las Vegas',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'İstanbul','Dubai',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Dubai','Las Vegas',0.2);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Dubai','New York',0.2);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Dubai','Singapur',0.2);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Dubai','İstanbul',0.2);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Las Vegas','Dubai',0.12);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Las Vegas','New York',0.12);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Las Vegas','Singapur',0.12);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Las Vegas','İstanbul',0.12);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'New York','Dubai',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'New York','Las Vegas',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'New York','Singapur',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'New York','İstanbul',0.1);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Singapur','Dubai',0.3);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Singapur','Las Vegas',0.3);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Singapur','New York',0.3);
INSERT INTO transportation VALUES ('Uçan Türk Özel Havayolu',500,'Singapur','İstanbul',0.3);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'İstanbul','Singapur',0.4);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'İstanbul','New York',0.4);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'İstanbul','Las Vegas',0.4);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'İstanbul','Dubai',0.4);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Dubai','Las Vegas',0.35);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Dubai','New York',0.35);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Dubai','Singapur',0.35);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Dubai','İstanbul',0.35);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Las Vegas','Dubai',0.26);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Las Vegas','New York',0.26);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Las Vegas','Singapur',0.26);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Las Vegas','İstanbul',0.26);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'New York','Dubai',0.18);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'New York','Las Vegas',0.18);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'New York','Singapur',0.18);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'New York','İstanbul',0.18);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Singapur','Dubai',0.32);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Singapur','Las Vegas',0.32);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Singapur','New York',0.32);
INSERT INTO transportation VALUES ('Devlet Demir Yolları',400,'Singapur','İstanbul',0.32);
INSERT INTO transportation VALUES ('YTUR',450,'İstanbul','Singapur',0.16);
INSERT INTO transportation VALUES ('YTUR',450,'İstanbul','New York',0.16);
INSERT INTO transportation VALUES ('YTUR',450,'İstanbul','Las Vegas',0.16);
INSERT INTO transportation VALUES ('YTUR',450,'İstanbul','Dubai',0.16);
INSERT INTO transportation VALUES ('YTUR',450,'Dubai','Las Vegas',0.09);
INSERT INTO transportation VALUES ('YTUR',450,'Dubai','New York',0.09);
INSERT INTO transportation VALUES ('YTUR',450,'Dubai','Singapur',0.09);
INSERT INTO transportation VALUES ('YTUR',450,'Dubai','İstanbul',0.09);
INSERT INTO transportation VALUES ('YTUR',450,'Las Vegas','Dubai',0.5);
INSERT INTO transportation VALUES ('YTUR',450,'Las Vegas','New York',0.5);
INSERT INTO transportation VALUES ('YTUR',450,'Las Vegas','Singapur',0.5);
INSERT INTO transportation VALUES ('YTUR',450,'Las Vegas','İstanbul',0.5);
INSERT INTO transportation VALUES ('YTUR',450,'New York','Dubai',0.35);
INSERT INTO transportation VALUES ('YTUR',450,'New York','Las Vegas',0.35);
INSERT INTO transportation VALUES ('YTUR',450,'New York','Singapur',0.35);
INSERT INTO transportation VALUES ('YTUR',450,'New York','İstanbul',0.35);
INSERT INTO transportation VALUES ('YTUR',450,'Singapur','Dubai',0.32);
INSERT INTO transportation VALUES ('YTUR',450,'Singapur','Las Vegas',0.32);
INSERT INTO transportation VALUES ('YTUR',450,'Singapur','New York',0.32);
INSERT INTO transportation VALUES ('YTUR',450,'Singapur','İstanbul',0.32);

-- datas of rezervation table
--                             (rCustomerID, rOtelName, rTime)
INSERT INTO rezervation VALUES (18034035,'Bellagio','09:30:00');

-- datas of booking table
--                         (bCustomerID, bCompanyName, bTime, bFrom, bTo)
INSERT INTO booking VALUES (18034035,'YTUR','08:30:00','Dubai','New York');