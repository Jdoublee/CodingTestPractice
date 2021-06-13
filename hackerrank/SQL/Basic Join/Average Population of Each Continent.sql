-- Given the CITY and COUNTRY tables, query the names of all the continents and their respective average city populations rounded down to the nearest integer.

SELECT COUNTRY.CONTINENT,FLOOR(AVG(CITY.POPULATION)) FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE=COUNTRY.CODE GROUP BY COUNTRY.CONTINENT;