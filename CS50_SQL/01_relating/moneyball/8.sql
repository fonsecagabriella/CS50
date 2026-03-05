-- write a SQL query to find the 2001 salary of the player who hit the most home runs in 2001.
SELECT
    "salaries"."salary"
FROM
    "salaries"
JOIN
    "performances"
    ON
    "salaries"."player_id" = "performances"."player_id"
    AND "salaries"."team_id" = "performances"."team_id"
WHERE
    "salaries"."year" = 2001
ORDER BY
    "performances"."HR" DESC
LIMIT 1;