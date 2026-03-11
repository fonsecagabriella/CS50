--  This view should contain all listings that have exactly one bedroom
CREATE VIEW "one_bedrooms" AS
SELECT  "id",
        "property_type",
        "host_name",
        "accommodates"
FROM "listings"
WHERE "bedrooms" = 1;