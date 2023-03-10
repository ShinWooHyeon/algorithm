-- 코드를 입력하세요
SELECT 
    FH.FLAVOR
FROM 
    FIRST_HALF AS FH 
LEFT JOIN (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
) AS  JU 
ON FH.FLAVOR = JU.FLAVOR
ORDER BY (FH.TOTAL_ORDER + JU.TOTAL_ORDER) DESC 
LIMIT 3;