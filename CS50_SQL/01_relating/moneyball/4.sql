-- write a SQL query to find the 50 players paid the least in 2001.
SELECT
    "salaries"."salary",
    "players"."first_name",
    "players"."last_name"
FROM
    "salaries"
JOIN
    "players"
    ON
    "salaries"."player_id" = "players"."id"
WHERE
    "salaries"."year" = 2001
ORDER BY
    "salaries"."salary" ASC,
    "players"."first_name" ASC,
    "players"."last_name" ASC
LIMIT 50;