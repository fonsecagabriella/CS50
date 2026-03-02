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