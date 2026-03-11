-- This view should contain, in order from greatest to least,
-- the most populated districts in Nepal.

CREATE VIEW "most_populated" AS
SELECT "district",
        SUM("families"),
        SUM("households"),
        SUM("population") AS "sum_population",
        SUM("male"),
        SUM("female")
FROM "census"
GROUP BY "district"
ORDER BY "sum_population" DESC;