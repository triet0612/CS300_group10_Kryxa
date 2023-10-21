
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
    "Price" REAL NOT NULL CHECK("Price" >= 1000),
    "Category" TEXT NOT NULL,
    "ItemStatus" TEXT NOT NULL CHECK ("ItemStatus" IN ("Deprecated", "On sale")),
    "Stock" INTEGER NOT NULL CHECK ("Stock" >= 0),
    PRIMARY KEY("ItemID")
);
CREATE TABLE "Bill" (
    "PcID" INTEGER NOT NULL,
    "Datetime" TEXT NOT NULL CHECK("Datetime" == datetime("Datetime")),
    "AdminID" INTEGER NOT NULL,
    "Status" TEXT NOT NULL CHECK("Status" IN ("In progress", "Completed", "Denied")),
    "Note" TEXT CHECK (LENGTH("Note") <= 100),
    "Total" REAL NOT NULL DEFAULT 0,
    "Cart" TEXT NOT NULL,
    FOREIGN KEY("PcID") REFERENCES "Pc"("PcID"),
    FOREIGN KEY("AdminID") REFERENCES "Admin"("AdminID"),
    PRIMARY KEY("PcID","Datetime")
);