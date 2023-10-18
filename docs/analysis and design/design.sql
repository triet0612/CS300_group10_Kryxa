CREATE TABLE "Admin" (
    "AdminID" INTEGER NOT NULL CHECK("AdminID" >= 0) UNIQUE,
    "Fullname" TEXT NOT NULL,
    "Phone" TEXT NOT NULL,
    "Password" TEXT NOT NULL,
    PRIMARY KEY("AdminID")
);
CREATE TABLE "PCs" (
    "PcID" INTEGER NOT NULL CHECK("PcID" >= 0) UNIQUE,
    "Password" TEXT NOT NULL CHECK(LENGTH("Password") == 6),
    "MAC" TEXT NOT NULL UNIQUE,
    "TimeUsage" INTEGER,
    PRIMARY KEY("PcID")
);
CREATE TABLE "SaleItem" (
    "ItemID" INTEGER NOT NULL CHECK("ItemID" > 0) UNIQUE,
    "Name" TEXT NOT NULL,
    "Price" REAL NOT NULL CHECK("Price" > 1000),
    "Category" TEXT NOT NULL,
    PRIMARY KEY("ItemID")
);
CREATE TABLE "Bill" (
    "PcID" INTEGER NOT NULL,
    "Datetime" TEXT NOT NULL CHECK("Datetime" == datetime("Datetime")),
    "AdminID" INTEGER NOT NULL,
    "Status" TEXT NOT NULL CHECK("Status" IN ("In progress", "Completed", "Denied")),
    "Note" TEXT,
    FOREIGN KEY("PcID") REFERENCES "PCs"("PcID"),
    FOREIGN KEY("AdminID") REFERENCES "Admin"("AdminID"),
    PRIMARY KEY("PcID","Datetime")
);
CREATE TABLE "Cart" (
    "PcID" INTEGER NOT NULL,
    "DateTime" TEXT NOT NULL,
    "ItemID" INTEGER NOT NULL,
    "Count" INTEGER NOT NULL CHECK("Count" > 0),
    PRIMARY KEY("PcID","DateTime"),
    FOREIGN KEY("PcID") REFERENCES "Bill"("PcID"),
    FOREIGN KEY("DateTime") REFERENCES "Bill"("Datetime")
);
