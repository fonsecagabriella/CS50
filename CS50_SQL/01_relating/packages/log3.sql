-- *** The Forgotten Gift ***
SELECT "scans"."action", 
        "scans"."timestamp",
        "packages"."contents",
        "addresses"."address",
        "addresses"."type",
        "drivers"."name"
FROM "scans" JOIN "packages" ON "scans"."package_id" = "packages"."id"
             JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
             JOIN "drivers" ON "scans"."driver_id" = "drivers"."id"
WHERE "packages"."from_address_id" = (
    SELECT id
    FROM "addresses"
    WHERE "addresses"."address" = '109 Tileston Street'
    ) AND
    "packages"."to_address_id" = (
        SELECT id
        FROM "addresses"
        WHERE "addresses"."address" = '728 Maple Place'
    )
ORDER BY "scans"."timestamp" DESC;