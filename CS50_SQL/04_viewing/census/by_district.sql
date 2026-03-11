-- This view should contain the sums for each numeric column in census, grouped by district.
CREATE VIEW "by_district" AS
SELECT  "district",
        SUM("families") AS "families",
        SUM("households") AS "households",
        SUM("population"),
        SUM("male"),
        SUM("female")
FROM "census"
GROUP BY "district";