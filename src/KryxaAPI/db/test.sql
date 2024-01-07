INSERT INTO Pc VALUES (0, "2023-11-13T10:46:00", "123", "192.168.0.2", 0);
INSERT INTO Pc VALUES (1, "2023-11-13T10:46:00", "124", "192.168.0.3", 0);
INSERT INTO SaleItem VALUES (2,"Com chien duong chau",20000,"Food",2);
INSERT INTO SaleItem VALUES (3,"Com ga xoi mo",50000,"Food",50);
INSERT INTO SaleItem VALUES (4,"Sting vang",10000,"Drink",23);
INSERT INTO SaleItem VALUES (5,"Sting do",10000,"Drink",21);
INSERT INTO SaleItem VALUES (6,"Mi indomie",12000,"Food",19);
INSERT INTO SaleItem VALUES (7,"Mi hao hao",10000,"Food",19);
INSERT INTO SaleItem VALUES (8,"The steam 5$",100000,"Other",19);
INSERT INTO SaleItem VALUES (9,"The Vinaphone 100K",100000,"Other",19);
INSERT INTO Bill VALUES(
    1, 0,"2023-11-13T10:46:00", "", 120000,
    "[{'id': 1, 'name': 'Time package', 'qt': 2, 'price': 10000, 'amount': 10000},{'id': 2, 'name': 'Com chien duong chau', 'qt': 1, 'price': 20000, 'amount': 20000}]"
);
INSERT INTO Bill VALUES(
    2, 1,"2023-11-14T10:46:00", "", 40000,
    "[{'id': 1, 'name': 'Time package', 'qt': 2, 'price': 10000, 'amount': 10000}]"
);
INSERT INTO Bill VALUES(
    3, 1,"2023-11-14T10:46:00", "", 42000,
    "[{'id': 1, 'name': 'Time package', 'qt': 3, 'price': 10000, 'amount': 30000},{'id': 6, 'name': 'Mi indomie', 'qt': 1, 'price': 12000, 'amount': 12000}]"
);
INSERT INTO Bill VALUES(
    4, 1,"2023-11-14T10:46:00", "", 20000,
    "[{'id': 1, 'name': 'Time package', 'qt': 1, 'price': 10000, 'amount': 10000},{'id': 5, 'name': 'Sting do', 'qt': 1, 'price': 10000, 'amount': 10000}]"
);
INSERT INTO Bill VALUES(
    5, 1,"2023-11-14T10:46:00", "", 162000,
    "[{'id': 1, 'name': 'Time package', 'qt': 5, 'price': 10000, 'amount': 50000},{'id': 8, 'name': 'The steam 5$', 'qt': 1, 'price': 100000, 'amount': 100000},{'id': 6, 'name': 'Mi indomie', 'qt': 1, 'price': 12000, 'amount': 12000}]"
);
