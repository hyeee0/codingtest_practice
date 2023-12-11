-- 코드를 입력하세요
SELECT YEAR(B.SALES_DATE) AS YEAR, MONTH(B.SALES_DATE) AS MONTH, 
COUNT(DISTINCT(A.USER_ID)) AS PUCHASED_USERS, ROUND(COUNT(DISTINCT(A.USER_ID)) / (SELECT COUNT(DISTINCT(USER_ID)) 
                                                                                  FROM USER_INFO 
                                                                                  WHERE JOINED LIKE '2021%'), 1) AS PUCHASED_RATIO
FROM USER_INFO A
JOIN ONLINE_SALE B
ON A.USER_ID = B.USER_ID
WHERE A.JOINED LIKE '2021%'
GROUP BY MONTH
ORDER BY 1, 2