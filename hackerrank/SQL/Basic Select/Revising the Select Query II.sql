-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. 

SELECT NAME FROM CITY WHERE COUNTRYCODE='USA' AND POPULATION>120000;