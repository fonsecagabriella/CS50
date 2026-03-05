-- write a SQL query to return the top 5 teams,
-- sorted by the total number of hits by players in 2001.
SELECT
    "teams"."name",
    SUM("performances"."H") AS "total hits"
FROM
    "teams"
JOIN
    "performances"
    ON
    "teams"."id" = "performances"."team_id"
WHERE
    "performances"."year" = 2001
GROUP BY
    "teams"."name"
ORDER BY
    "total hits" DESC
LIMIT 5;