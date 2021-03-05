-- 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE ANIMAL_TYPE='Dog' AND NAME LIKE '%el%' ORDER BY NAME;