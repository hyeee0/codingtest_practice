-- 코드를 입력하세요
SET @HOUR = -1; # SET :=은 대입연산자 SET @변수 := VALUE;
SELECT (@HOUR := @HOUR +1) AS HOUR, (SELECT COUNT(*)
                                    FROM ANIMAL_OUTS
                                    WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23
GROUP BY HOUR
