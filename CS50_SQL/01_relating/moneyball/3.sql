-- write a SQL query to find Ken Griffey Jr.’s home run history.
SELECT
    "performances"."HR",
    "performances". "year"
FROM
    "performances"
INNER JOIN
    "players"
    ON
    "performances"."player_id" = "players"."id"
WHERE
    "players"."first_name" LIKE 'Ken' 
    AND "players"."last_name" LIKE '%Griffey%'
    AND "players"."birth_year" = 1969
ORDER BY
    "performances"."year" DESC;