-- task4
-- script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
