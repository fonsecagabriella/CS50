-- write a SQL query to find the 10 least expensive players per hit in 2001.
SELECT
    "players"."first_name",
    "players"."last_name",
    "salaries"."salary" / "performances"."H" AS "dollars_per_hit"
FROM
    "players"
JOIN
    "performances" ON "players"."id" = "performances"."player_id"
JOIN
    "salaries" ON "players"."id" = "salaries"."player_id"
WHERE
    "performances"."H" > 0
    AND
    "performances"."year" = 2001
    AND
    "salaries"."year" = 2001
ORDER BY
    "dollars_per_hit" ASC,
    "players"."first_name" ASC,
    "players"."last_name" ASC
LIMIT 10;