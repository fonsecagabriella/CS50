-- The general manager has asked you for a report which details each player’s name,
-- their salary for each year they’ve been playing,
-- and their number of home runs for each year they’ve been playing.
SELECT
    "players"."first_name",
    "players"."last_name",
    "salaries"."salary",
    "performances"."HR",
    "salaries"."year"
FROM
    "players"
JOIN
    "performances" ON "players"."id" = "performances"."player_id"
JOIN
    "salaries" ON "players"."id" = "salaries"."player_id"
WHERE
    "performances"."year" = "salaries"."year"
ORDER BY
    "players"."id" ASC,
    "salaries"."year" DESC,
    "performances"."HR" DESC,
    "salaries"."salary" DESC;