-- write a SQL query to find the name of the player who’s been paid the highest salary,
-- of all time, in Major League Baseball.
SELECT
    "players"."first_name",
    "players"."last_name"
FROM
    "players"
JOIN
    "salaries"
    ON
    "players"."id" = "salaries"."player_id"
ORDER BY
    "salaries". "salary" DESC
LIMIT 1;