CREATE TABLE "Admin" (
    "Password" TEXT NOT NULL
);
CREATE TABLE "Pc" (
    "PcID" INTEGER NOT NULL CHECK("PcID" >= 0) UNIQUE,
    "EndTime" TEXT,
    "Password" TEXT NOT NULL CHECK(LENGTH("Password") == 3),
    "IPv4" TEXT NOT NULL UNIQUE,
    "TimeUsage" INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY("PcID")
);
CREATE TABLE "SaleItem" (
    "ItemID" INTEGER NOT NULL CHECK("ItemID" > 0) UNIQUE,
    "Name" TEXT NOT NULL,
    "Price" REAL NOT NULL,
    "Category" TEXT NOT NULL,
    "Stock" INTEGER NOT NULL CHECK ("Stock" >= 0),
    PRIMARY KEY("ItemID")
);
CREATE TABLE "Bill" (
    "BillID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "PcID" INTEGER NOT NULL,
    "Datetime" TEXT NOT NULL,
    "Note" TEXT CHECK (LENGTH("Note") <= 100),
    "Total" REAL NOT NULL DEFAULT 0,
    "Cart" TEXT NOT NULL,
    FOREIGN KEY("PcID") REFERENCES "Pc"("PcID")
);
INSERT INTO Admin VALUES ("1234");
INSERT INTO Pc VALUES (0, "2024-11-13T10:46:00", "123", "192.168.0.2", 0);
INSERT INTO Pc VALUES (1, "2023-11-13T10:46:00", "124", "192.168.0.3", 0);
INSERT INTO SaleItem VALUES (1,"Com ga 1",50000,"Food",2);
INSERT INTO SaleItem VALUES (2,"Com ga 2",40000,"Food",2);
INSERT INTO SaleItem VALUES (3,"Sting Dau",20000,"Drink",2);
INSERT INTO SaleItem VALUES (4,"Red Bull",20000,"Drink",2);
INSERT INTO SaleItem VALUES (5,"1 Hour",10000,"Time",2);
INSERT INTO SaleItem VALUES (6,"2 Hour",20000,"Time",2);
INSERT INTO Bill VALUES(1,0,"2023-11-13T10:46:00","",0,"[{'id': 1, 'name': 'com chien duong chau', 'qt': 2, 'price': 20000, 'amount': 40000},{'id': 2, 'name': 'com chien duong chau', 'qt': 2, 'price': 20000, 'amount': 40000}]");
INSERT INTO Bill VALUES(2,0,"2023-11-13T10:46:00","",0,"[{'id': 1, 'name': 'com chien duong chau', 'qt': 2, 'price': 20000, 'amount': 40000}]");
INSERT INTO Bill VALUES(3,0,"2023-11-13T10:46:00","",0,"[{'id': 1, 'name': 'com chien duong chau', 'qt': 2, 'price': 20000, 'amount': 40000}]");
INSERT INTO Bill VALUES(4,0,"2023-11-13T10:46:00","",0,"[{'id': 1, 'name': 'com chien duong chau', 'qt': 2, 'price': 20000, 'amount': 40000}]");
INSERT INTO Bill VALUES(5,0,"2023-11-13T10:46:00","",0,"[{'id': 1, 'name': 'com chien duong chau', 'qt': 2, 'price': 20000, 'amount': 40000}]");
INSERT INTO Bill VALUES(6,0,"2023-11-13T10:46:00","",0,"[{'id': 1, 'name': 'com chien duong chau', 'qt': 2, 'price': 20000, 'amount': 40000}]");
