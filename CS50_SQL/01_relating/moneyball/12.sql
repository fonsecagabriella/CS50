--
SELECT -- players with the 10 least expensive players per hit in 2001
    "players"."first_name",
    "players"."last_name"
FROM
    "players"
WHERE
    "players"."id" IN (
        SELECT
            "performances"."player_id"
        FROM
            "performances"
        JOIN
            "salaries" ON "performances"."player_id" = "salaries"."player_id"
        WHERE
            "performances"."year" = 2001
            AND
            "performances"."H" > 0
            AND
            "salaries"."year" = 2001
        ORDER BY
            "salaries"."salary" / "performances"."H" ASC
        LIMIT 10
    )

INTERSECT

SELECT -- players with the 10 least expensive players per RBI in 2001
    "players"."first_name",
    "players"."last_name"
FROM
    "players"
WHERE
    "players"."id" IN (
        SELECT
            "performances"."player_id"
        FROM
            "performances"
        JOIN
            "salaries" ON "performances"."player_id" = "salaries"."player_id"
        WHERE
            "performances"."year" = 2001
            AND
            "performances"."RBI" > 0
            AND
            "salaries"."year" = 2001
        ORDER BY
            "salaries"."salary" / "performances"."RBI" ASC
        LIMIT 10
    )

ORDER BY
    "players"."last_name" ASC

;