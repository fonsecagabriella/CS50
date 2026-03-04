-- write a SQL query to find the name (or names) of the school district(s)
-- with the single least number of pupils. Report only the name(s).
SELECT
    "districts"."name"
FROM
    "districts"
RIGHT JOIN
    "expenditures"
    ON
    "districts"."id" = "expenditures"."district_id"
ORDER BY
    "expenditures"."pupils"ASC
LIMIT 1;