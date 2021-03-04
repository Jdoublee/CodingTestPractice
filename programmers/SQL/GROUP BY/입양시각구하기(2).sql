-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

SET @hour := -1; -- 변수 선언.  := 은 대입 연산자

SELECT (@hour := @hour + 1) as HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT FROM ANIMAL_OUTS WHERE @hour < 23;
-- 변수 선언 및 증가 연산 시행
-- 다시 보기*****