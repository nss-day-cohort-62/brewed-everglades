CREATE TABLE `Products` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `price` decimal(2) NOT NULL
);

CREATE TABLE `Orders` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `product_id` INT NOT NULL,
    `employee_id` INT NOT NULL,
    `timestamp` datetime NOT NULL
);

CREATE TABLE `Employees` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `hourly_rate` DECIMAL(4, 2) NOT NULL
);

INSERT INTO `Products` VALUES (null, "espresso", 2.50);
INSERT INTO `Products` VALUES (null, "delicious coffee", 3.75);
INSERT INTO `Products` VALUES (null, "cappuccino", 4.00);

INSERT INTO `Employees` VALUES (null, "Stephen", "stephen@brewed.com", 48.38);
INSERT INTO `Employees` VALUES (null, "Jordan", "jordan@brewed.com", 49.47);

INSERT INTO `Orders` VALUES (null, 1, 1, "2023-03-30");
INSERT INTO `Orders` VALUES (null, 2, 2, "2023-04-07");
