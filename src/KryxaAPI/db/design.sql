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
CREATE TRIGGER OneBillPerSessionInsert
BEFORE INSERT ON "Bill"
BEGIN
	SELECT CASE WHEN EXISTS (
		SELECT * FROM Bill
		WHERE Bill.PcID = NEW.PcID
		AND Bill.Datetime = ""
	) THEN
		RAISE(ABORT, "A bill in progress")
	END;
END;
INSERT INTO Admin VALUES ("1234");