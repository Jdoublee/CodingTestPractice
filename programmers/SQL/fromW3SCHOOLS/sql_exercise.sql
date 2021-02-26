-- SELECT 문
-- The SELECT statement is used to select data from a database.

-- 1. get all the columns from the Customers table.
SELECT * FROM Customers;

-- 2. select the City column from the Customers table.
SELECT City FROM Customers;

--3. select all the different values from the Country column in the Customers table.
SELECT DISTINCT Country FROM Customers; -- 중복 제거


-- WHERE 절
-- The WHERE clause is used to filter records.

-- 1. select all records where the City column has the value "Berlin".
SELECT * FROM Customers WHERE City = 'Berlin';

--2. select all records where City is NOT "Berlin".
SELECT * FROM Customers WHERE NOT City='Berlin';

--3. select all records where the CustomerID column has the value 32.
SELECT * FROM Customers WHERE CustomerID=32;

--4. select all records where the City column has the value 'Berlin' and the PostalCode column has the value 12209.
SELECT * FROM Customers WHERE City='Berlin' AND PostalCode=12209;

--5. select all records where the City column has the value 'Berlin' or 'London'.
SELECT * FROM Customers WHERE City='Berlin' OR City='London';


-- ORDER BY
-- The ORDER BY keyword is used to sort the result-set in ascending or descending order.

-- 1.