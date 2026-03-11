--
CREATE VIEW "june_vacancies" AS
SELECT "listings"."id",
        "listings"."property_type",
        "listings"."host_name",
        COUNT("availabilities"."id") AS "days_vacant"
FROM "listings", "availabilities"
WHERE
    ("availabilities"."date" BETWEEN '2023-06-01' AND '2023-06-30') AND
    "listings"."id" = "availabilities"."listing_id" AND
    "availabilities"."available" = 'TRUE'
GROUP BY "listings"."id";