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
INSERT INTO SaleItem VALUES (1,"Com ga 1",50000,"Food",2);
INSERT INTO SaleItem VALUES (2,"Com ga 2",50000,"Food",1);
INSERT INTO SaleItem VALUES (3,"Com ga 3",50000,"Food",3);
INSERT INTO SaleItem VALUES (4,"Com ga 1",50000,"Food",2);
INSERT INTO SaleItem VALUES (5,"Com ga 2",50000,"Food",1);
INSERT INTO SaleItem VALUES (6,"Com ga 3",50000,"Food",3);
INSERT INTO SaleItem VALUES (7,"Com ga 1",50000,"Food",2);
INSERT INTO SaleItem VALUES (8,"Com ga 2",50000,"Food",1);
INSERT INTO SaleItem VALUES (9,"Com ga 3",50000,"Food",3);
INSERT INTO SaleItem VALUES (10,"Com ga 1",50000,"Drink",2);
INSERT INTO SaleItem VALUES (11,"Com ga 2",50000,"Drink",1);
INSERT INTO SaleItem VALUES (12,"Com ga 3",50000,"Drink",3);
INSERT INTO SaleItem VALUES (13,"Com ga 1",50000,"Drink",2);
INSERT INTO SaleItem VALUES (14,"Com ga 2",50000,"Drink",1);
INSERT INTO SaleItem VALUES (15,"Com ga 3",50000,"Drink",3);
INSERT INTO SaleItem VALUES (16,"Com ga 1",50000,"Time",2);
INSERT INTO SaleItem VALUES (17,"Com ga 2",50000,"Time",1);
INSERT INTO SaleItem VALUES (18,"Com ga 3",50000,"Time",3);
INSERT INTO SaleItem VALUES (19,"Com ga 2",50000,"Time",1);
INSERT INTO SaleItem VALUES (20,"Com ga 3",50000,"Time",3);
INSERT INTO SaleItem VALUES (21,"Com ga 1",50000,"Time",2);
INSERT INTO SaleItem VALUES (22,"Com ga 2",50000,"Food",1);
INSERT INTO SaleItem VALUES (23,"Com ga 3",50000,"Food",3);
INSERT INTO SaleItem VALUES (24,"Com ga 1",50000,"Food",2);
INSERT INTO SaleItem VALUES (25,"Com ga 2",50000,"Food",1);
INSERT INTO SaleItem VALUES (26,"Com ga 3",50000,"Food",3);
