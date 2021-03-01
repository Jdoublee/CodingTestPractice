-- SELECT 문
-- The SELECT statement is used to select data from a database.

-- 1. get all the columns from the Customers table.
SELECT * FROM Customers;

-- 2. select the City column from the Customers table.
SELECT City FROM Customers;

-- 3. select all the different values from the Country column in the Customers table.
SELECT DISTINCT Country FROM Customers; -- 중복 제거


-- WHERE 절
-- The WHERE clause is used to filter records.

-- 1. select all records where the City column has the value "Berlin".
SELECT * FROM Customers WHERE City = 'Berlin';

-- 2. select all records where City is NOT "Berlin".
SELECT * FROM Customers WHERE NOT City='Berlin';

-- 3. select all records where the CustomerID column has the value 32.
SELECT * FROM Customers WHERE CustomerID=32;

-- 4. select all records where the City column has the value 'Berlin' and the PostalCode column has the value 12209.
SELECT * FROM Customers WHERE City='Berlin' AND PostalCode=12209;

-- 5. select all records where the City column has the value 'Berlin' or 'London'.
SELECT * FROM Customers WHERE City='Berlin' OR City='London';


-- ORDER BY
-- The ORDER BY keyword is used to sort the result-set in ascending or descending order.

-- 1. select all records from the Customers table, sort the result alphabetically by the column City.
SELECT * FROM Customers ORDER BY City;

-- 2. select all records from the Customers table, sort the result reversed alphabetically by the column City.
SELECT * FROM Customers ORDER BY City DESC;

-- 3. select all records from the Customers table, sort the result alphabetically, first by the column Country, then, by the column City.
SELECT * FROM Customers ORDER BY Country, City;


-- INSERT
-- The INSERT INTO statement is used to insert new records in a table.

-- 1. insert a new record in the Customers table.
INSERT INTO Customers (CustomerName, Address, City, PostalCode, Country) VALUES ('Hekkan Burger', 'Gateveien 15', 'Sandnes', '4306', 'Norway');


-- NULL
-- A field with a **NULL value** is a field with no value.

-- 1. select all records from the Customers where the PostalCode column is empty.
SELECT * FROM Customers WHERE PostalCode IS NULL;

-- 2. select all records from the Customers where the PostalCode column is NOT empty.
SELECT * FROM Customers WHERE PostalCode IS NOT NULL;


-- FUNCTIONS
-- MIN, MAX, COUNT, AVG, SUM

-- 1. select the record with the smallest value of the Price column.
SELECT MIN(Price) FROM Products;

-- 2. select the record with the highest value of the Price column.
SELECT MAX(Price) FROM Products;

-- 3. return the number of records that have the Price value set to 18.
SELECT COUNT(*) FROM Products WHERE Price=18;

-- 4. calculate the average price of all products.
SELECT AVG(Price) FROM Products;

-- 5. calculate the sum of all the Price column values in the Products table.
SELECT SUM(Price) FROM Products;


-- LIKE
-- The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

-- 1. select all records where the value of the City column starts with the letter "a".
SELECT * FROM Customers WHERE City LIKE 'a%';

-- 2. select all records where the value of the City column ends with the letter "a".
SELECT * FROM Customers WHERE City LIKE '%a';

-- 3. select all records where the value of the City column contains the letter "a".
SELECT * FROM Customers WHERE City LIKE '%a%';

-- 4. select all records where the value of the City column starts with letter "a" and ends with the letter "b".
SELECT * FROM Customers WHERE City LIKE 'a%b';

-- 5. select all records where the value of the City column does NOT start with the letter "a".
SELECT * FROM Customers WHERE City NOT LIKE 'a%';


-- WILDCARDS
-- A wildcard character is used to substitute one or more characters in a string.

-- 1. select all records where the second letter of the City is an "a".
SELECT * FROM Customers WHERE City LIKE '_a%';

-- 2. select all records where the first letter of the City is an "a" or a "c" or an "s".
SELECT * FROM Customers WHERE City LIKE '[acs]%';

-- 3. select all records where the first letter of the City starts with anything from an "a" to an "f".
SELECT * FROM Customers WHERE City LIKE '[a-f]%';

-- 4. select all records where the first letter of the City is NOT an "a" or a "c" or an "f".
SELECT * FROM Customers WHERE City LIKE '[^acf]%';


-- IN
-- The IN operator allows you to specify multiple values in a WHERE clause.

-- 1. select all the records where Country is either "Norway" or "France".
SELECT * FROM Customers WHERE Country IN ('Norway', 'France');

-- 2. select all the records where Country is NOT "Norway" and NOT "France".
SELECT * FROM Customers WHERE Country NOT IN ('Norway', 'France');


-- BETWEEN
-- The BETWEEN operator selects values within a given range. The values can be numbers, text, or dates.

-- 1. select all the records where the value of the Price column is between 10 and 20.
SELECT * FROM Products WHERE Price BETWEEN 10 AND 20;

-- 2. select all the records where the value of the Price column is NOT between 10 and 20.
SELECT * FROM Products WHERE Price NOT BETWEEN 10 AND 20;

-- 3. select all the records where the value of the ProductName column is alphabetically between 'Geitost' and 'Pavlova'.
SELECT * FROM Products WHERE ProductName BETWEEN 'Geitost' AND 'Pavlova';
