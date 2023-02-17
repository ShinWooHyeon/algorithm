-- 코드를 입력하세요
SELECT MCDP_CD AS '진료과 코드' ,count(*) AS '5월예약건수' FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD,'%Y-%m-%d') between '2022-05-01' and '2022-05-31'
GROUP BY MCDP_CD
ORDER BY
   count(*),
    MCDP_CD;
