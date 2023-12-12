-- 코드를 입력하세요
# OUTER JOIN은 조인하는 여러테이블에서 한 쪽에는 데이터가 있고, 한 쪽에는 데이터가 없는 경우, 데이터가 있는 쪽 테이블의 내용을 모두 출력하는 것입니다. 즉, 조건에 맞지 않아도 해당하는 행을 출력하고 싶을 때 사용 
# WHERE 1 = 1 -> 주석처리 할 때 사용, WHERE 다음에 있는 AND를 바로 주석처리해도 에러X


SELECT HISTORY_ID, ROUND(DAILY_FEE*(DATEDIFF(END_DATE, START_DATE)+1)*(100-IF(DISCOUNT_RATE IS NULL, 0, DISCOUNT_RATE))/100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.CAR_ID = B.CAR_ID
LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON A.CAR_TYPE = C.CAR_TYPE
AND C.DURATION_TYPE = (CASE
                        WHEN DATEDIFF(B.END_DATE, B.START_DATE)+1 >= 90 THEN '90일 이상'
                        WHEN DATEDIFF(B.END_DATE, B.START_DATE)+1 >= 30 THEN '30일 이상'
                        WHEN DATEDIFF(B.END_DATE, B.START_DATE)+1 >= 7 THEN '7일 이상'
                        ELSE NULL
                        END)
WHERE 1 = 1
AND A.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC;