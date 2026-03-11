-- This view should contain the 100 most frequently reviewed listings,
-- sorted from most- to least-frequently reviewed.
CREATE VIEW "frequently_reviewed" AS

SELECT
    "listings"."id" AS "listing_id",
    COUNT("reviews"."id") AS "total_reviews",
    "listings"."property_type" AS "property_type",
    "listings"."host_name" AS "host_name"
FROM "reviews" JOIN "listings"
WHERE "reviews"."listing_id" = "listings"."id"
GROUP BY "listings"."id"
ORDER BY "total_reviews" DESC, "listings"."property_type" ASC, "listings"."host_name" ASC
LIMIT 100;