-- write a SQL query to find all teams that Satchel Paige played for.
SELECT
    "teams"."name"
FROM
    "teams"
JOIN
    "performances"
    ON
    "teams"."id" = "performances"."team_id"
JOIN
    "players"
    ON
    "performances"."player_id" = "players"."id"
WHERE
    "players"."first_name" LIKE 'Satchel'
    AND "players"."last_name" LIKE 'Paige'
GROUP BY
    "teams"."name";