-- question of choice: count the number of episodes per season.
SELECT "season", COUNT(*) AS "episodes_per_season"
FROM "episodes"
GROUP BY "season"
ORDER BY "season";