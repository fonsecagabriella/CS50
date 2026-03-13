CREATE VIEW "message" AS

WITH "list_of_codes"("A", "B", "C") AS (
    VALUES
        (14, 98, 4), -- sentence id, start position, number of characters
        (114, 3, 5),
        (618, 72, 9),
        (630, 7, 3),
        (932, 12, 5),
        (2230, 50, 7),
        (2346, 44, 10),
        (3041, 14, 5)
)
SELECT
    SUBSTR ("sentences"."sentence", "list_of_codes"."B", "list_of_codes"."C") AS "phrase"
FROM "sentences"
JOIN "list_of_codes" ON "sentences"."id" = "list_of_codes"."A";