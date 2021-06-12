-- Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical. Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order.

SELECT CONCAT(NAME,'(',SUBSTRING(OCCUPATION,1,1),')') FROM OCCUPATIONS ORDER BY NAME;
SELECT CONCAT('There are a total of ',COUNT(OCCUPATION),' ',LOWER(OCCUPATION),'s.') FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY COUNT(OCCUPATION);