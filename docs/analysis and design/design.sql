CREATE TABLE PC(
    PCID INTEGER,
    Password TEXT,
    MAC TEXT,
    time_usage INTEGER,
    PRIMARY KEY(PCID)
);

CREATE TABLE Admin(
    AdminID INTEGER,
    Fullname TEXT,
    Phone TEXT,
    Password TEXT,
    PRIMARY KEY(AdminID)
);

CREATE TABLE Item(
    ItemID INTEGER,
    Name TEXT,
    Price REAL,
    Category TEXT,
    PRIMARY KEY(ItemID)
);

CREATE TABLE Bill(
    PCID INTEGER PRIMARY KEY,
    bill_datetime TEXT PRIMARY KEY,
    Status INTEGER DEFAULT 0,
    AdminID INTEGER,
    FOREIGN KEY(PCID) REFERENCES PC(PCID),
    FOREIGN KEY(AdminID) REFERENCES Admin(AdminID),
);

CREATE TABLE Cart(
    PCID INTEGER PRIMARY KEY,
    Cart_datetime TEXT PRIMARY KEY,
    ItemID INTEGER,
    Amount INTEGER DEFAULT 0,
    FOREIGN KEY(PCID) REFERENCES Bill(PCID),
    FOREIGN KEY(Cart_datetime) REFERENCES Bill(bill_datetime),
    FOREIGN KEY(ItemID) REFERENCES Item(ItemID),
);