-- write a SQL query to find cities with 3 or fewer public schools.
-- Your query should return the names of the cities and the number of public schools within them,
-- ordered from greatest number of public schools to least.
--If two cities have the same number of public schools, order them alphabetically.

SELECT
    "city",
    COUNT("city") AS "number of schools"
FROM
    "schools"
WHERE
    "type" LIKE '%public school%'
GROUP BY
    "city"
HAVING
    "number of schools" < 4
ORDER BY
    "number of schools" DESC, "city" ASC;