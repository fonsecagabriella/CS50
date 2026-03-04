-- write a SQL query to display the names of all school districts
-- and the number of pupils enrolled in each.
SELECT
    "districts"."name",
    "expenditures"."pupils"
FROM
    "districts"
RIGHT JOIN
    "expenditures"
    ON
    "districts"."id" = "expenditures"."district_id";
