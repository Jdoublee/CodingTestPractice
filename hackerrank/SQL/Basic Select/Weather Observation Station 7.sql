-- Query the list of CITY names ending with vowels from STATION. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[aeiou]$';