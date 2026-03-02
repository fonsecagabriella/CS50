
-- *** The Lost Letter ***
SELECT "scans"."action", 
        "scans"."timestamp", 
        "addresses"."address", 
        "addresses"."type"
FROM "scans" JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
WHERE "scans"."package_id" = (
    -- address of the lost letter
    SELECT id
    FROM "packages"
    WHERE "packages"."from_address_id" = (
        -- address of the lost letter
        SELECT id
        FROM "addresses"
        WHERE "addresses"."address" = '900 Somerville Avenue'
        )
    )
ORDER BY "scans"."timestamp" DESC;

-- *** The Devious Delivery ***
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

-- *** The Forgotten Gift ***
SELECT "scans"."action", 
        "scans"."timestamp",
        "packages"."contents",
        "addresses"."address",
        "addresses"."type"
FROM "scans" JOIN "packages" ON "scans"."package_id" = "packages"."id"
             JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
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

