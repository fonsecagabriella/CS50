-- write a SQL query to find Cal Ripken Jr.’s salary history.
SELECT
    "salaries"."salary",
    "salaries"."year"
FROM
    "salaries"
INNER JOIN
    "players"
    ON
    "salaries"."player_id" = "players"."id"
WHERE
    "players"."first_name" LIKE '%Cal%'
    AND
    "players"."last_name" LIKE '%Ripken%'
ORDER BY
    "salaries"."year" DESC;