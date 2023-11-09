
CREATE TABLE "Admin" (
    "AdminID" INTEGER NOT NULL CHECK("AdminID" >= 0) UNIQUE,
    "Fullname" TEXT NOT NULL,
    "Phone" TEXT NOT NULL,
    "Password" TEXT NOT NULL,
    PRIMARY KEY("AdminID")
);
CREATE TABLE "Pc" (
    "PcID" INTEGER NOT NULL CHECK("PcID" >= 0) UNIQUE,
    "Password" TEXT NOT NULL CHECK(LENGTH("Password") == 3),
    "MAC" TEXT NOT NULL UNIQUE,
    "IPv4" TEXT NOT NULL UNIQUE,
    "TimeUsage" INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY("PcID")
);
CREATE TABLE "SaleItem" (
    "ItemID" INTEGER NOT NULL CHECK("ItemID" > 0) UNIQUE,
    "Name" TEXT NOT NULL,
    "Price" REAL NOT NULL,
    "Category" TEXT NOT NULL,
    "ItemStatus" TEXT NOT NULL CHECK ("ItemStatus" IN ("Deprecated", "On sale")),
    "Stock" INTEGER NOT NULL CHECK ("Stock" >= 0),
    PRIMARY KEY("ItemID")
);
CREATE TABLE "Bill" (
    "PcID" INTEGER NOT NULL,
    "Datetime" TEXT NOT NULL,
    "AdminID" INTEGER NOT NULL,
    "Status" TEXT NOT NULL CHECK("Status" IN ("In progress", "Completed", "Denied")),
    "Note" TEXT CHECK (LENGTH("Note") <= 100),
    "Total" REAL NOT NULL DEFAULT 0,
    "Cart" TEXT NOT NULL,
    FOREIGN KEY("PcID") REFERENCES "Pc"("PcID"),
    FOREIGN KEY("AdminID") REFERENCES "Admin"("AdminID"),
    PRIMARY KEY("PcID","Datetime")
);
INSERT INTO Admin VALUES (0, "Default Admin", "(+84)1234567", "1234");
INSERT INTO Pc VALUES (0, "123", "11-22-33-44-55-66", "192.168.0.2", 0);
INSERT INTO SaleItem VALUES (1,"Com ga 1",50000,"Food","On sale",2);
INSERT INTO SaleItem VALUES (2,"Com ga 2",50000,"Food","On sale",1);
INSERT INTO SaleItem VALUES (3,"Com ga 3",50000,"Food","On sale",3);
INSERT INTO SaleItem VALUES (4,"Com ga 1",50000,"Food","On sale",2);
INSERT INTO SaleItem VALUES (5,"Com ga 2",50000,"Food","On sale",1);
INSERT INTO SaleItem VALUES (6,"Com ga 3",50000,"Food","On sale",3);
INSERT INTO SaleItem VALUES (7,"Com ga 1",50000,"Food","On sale",2);
INSERT INTO SaleItem VALUES (8,"Com ga 2",50000,"Food","On sale",1);
INSERT INTO SaleItem VALUES (9,"Com ga 3",50000,"Food","On sale",3);
INSERT INTO SaleItem VALUES (10,"Com ga 1",50000,"Drink","On sale",2);
INSERT INTO SaleItem VALUES (11,"Com ga 2",50000,"Drink","On sale",1);
INSERT INTO SaleItem VALUES (12,"Com ga 3",50000,"Drink","On sale",3);
INSERT INTO SaleItem VALUES (13,"Com ga 1",50000,"Drink","On sale",2);
INSERT INTO SaleItem VALUES (14,"Com ga 2",50000,"Drink","On sale",1);
INSERT INTO SaleItem VALUES (15,"Com ga 3",50000,"Drink","On sale",3);
INSERT INTO SaleItem VALUES (16,"Com ga 1",50000,"Time","On sale",2);
INSERT INTO SaleItem VALUES (17,"Com ga 2",50000,"Time","On sale",1);
INSERT INTO SaleItem VALUES (18,"Com ga 3",50000,"Time","On sale",3);
INSERT INTO SaleItem VALUES (19,"Com ga 2",50000,"Time","On sale",1);
INSERT INTO SaleItem VALUES (20,"Com ga 3",50000,"Time","On sale",3);
INSERT INTO SaleItem VALUES (21,"Com ga 1",50000,"Time","On sale",2);
INSERT INTO SaleItem VALUES (22,"Com ga 2",50000,"Food","On sale",1);
INSERT INTO SaleItem VALUES (23,"Com ga 3",50000,"Food","On sale",3);
INSERT INTO SaleItem VALUES (24,"Com ga 1",50000,"Food","On sale",2);
INSERT INTO SaleItem VALUES (25,"Com ga 2",50000,"Food","On sale",1);
INSERT INTO SaleItem VALUES (26,"Com ga 3",50000,"Food","On sale",3);
