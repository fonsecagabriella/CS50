-- This view should contain the sums for each numeric column in census,
-- across all districts and localities
CREATE VIEW "total" AS
SELECT  SUM("families"),
        SUM("households") AS "households",
        SUM("population"),
        SUM("male"),
        SUM("female")
FROM "census";