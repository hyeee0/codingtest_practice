-- 코드를 입력하세요
SELECT A.APNT_NO, B.PT_NAME, A.PT_NO, A.MCDP_CD, C.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A JOIN PATIENT B ON A.PT_NO = B.PT_NO JOIN DOCTOR C ON A.MDDR_ID = C.DR_ID
WHERE A.MCDP_CD LIKE 'CS'AND A.APNT_CNCL_YN LIKE 'N'AND A.APNT_YMD LIKE '2022-04-13%'
ORDER BY A.APNT_YMD