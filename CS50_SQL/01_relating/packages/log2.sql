-- *** The Devious Delivery ***
SELECT "scans"."action", 
        "scans"."timestamp",
        "packages"."contents",
        "addresses"."address",
        "addresses"."type"
FROM "scans"    JOIN "packages" ON "scans"."package_id" = "packages"."id"
                JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
WHERE "packages"."from_address_id" IS NULL
ORDER BY "scans"."timestamp" DESC;