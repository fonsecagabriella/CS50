-- Temp table to load meteorites.csv file
CREATE TABLE "meteorites_temp"(
    "name" TEXT,
    "id" INTEGER,
    "nametype" TEXT,
    "class" TEXT,
    "mass" REAL,
    "discovery" TEXT,
    "year" INTEGER,
    "lat" REAL,
    "long" REAL
);

CREATE TABLE IF NOT EXISTS "meteorites"(
    "id" INTEGER,
    "name" TEXT,
    "class" VARCHAR(100),
    "mass" DECIMAL(10,2),
    "discovery" INTEGER,
    "year" INTEGER,
    "lat" DECIMAL(10,2),
    "long" DECIMAL(10,2),

    PRIMARY KEY ("id"),
    CONSTRAINT "chk_discovery" CHECK (  "discovery" IS NULL OR
                                    "discovery" LIKE '%fell%' OR
                                    "discovery" LIKE '%found') -- “Fell” or “Found” for discovery,
    CONSTRAINT "chk_year" CHECK ("year" IS NULL OR "year" > 100) -- constraint for year

);

-- import meteorites.csv skipping the first column
-- if done in terminal, use
.import --csv --skip 1 meteorites.csv meteorites_temp

-- clean mass column
UPDATE "meteorites_temp"
SET "mass" = NULL
WHERE "mass" = 0;

-- clean year column
UPDATE "meteorites_temp"
SET "year" = NULL
WHERE "year" = 0;

UPDATE "meteorites_temp"
SET "year" = NULL
WHERE "year" = '';

-- clean lat column
UPDATE "meteorites_temp"
SET "lat" = NULL
WHERE "lat" = 0;

-- clean long column
UPDATE "meteorites_temp"
SET "long" = NULL
WHERE "long" = 0;

-- round mass values to 2 decimal places
UPDATE "meteorites_temp"
SET "mass" = ROUND("mass", 2);

-- round lat to 2 decimal places
UPDATE "meteorites_temp"
SET "lat" = ROUND("lat", 2);

-- round long values to 2 decimal places
UPDATE "meteorites_temp"
SET "long" = ROUND("long", 2);

-- clean "nametype" to all lower case
--UPDATE "meteorites_temp"
--SET "nametype" = LOWER("nametype");

-- clean "name" to all lower case
--UPDATE "meteorites_temp"
--SET "name" = LOWER("name");

-- clean "class" to all lower case
--UPDATE "meteorites_temp"
--SET "class" = LOWER("class");

-- clean "discovery" to all lower case
--UPDATE "meteorites_temp"
--SET "discovery" = LOWER("discovery");

-- drop meteorites with nametype 'relict'
DELETE FROM "meteorites_temp"
WHERE "nametype" LIKE '%relict%';

-- update id values, from year and name
WITH "sorted_meteorites" AS
    (
        SELECT "id",
        ROW_NUMBER() OVER (ORDER BY "year" ASC, "name" ASC) AS "new_id"
        FROM "meteorites_temp"
    )
UPDATE "meteorites_temp"
SET "id" = "sorted_meteorites"."new_id"
FROM "sorted_meteorites"
WHERE "meteorites_temp"."id" = "sorted_meteorites"."id";


INSERT INTO "meteorites" ("id", "name", "class", "mass", "discovery", "year", "lat", "long")
SELECT "id", "name", "class", "mass", "discovery", "year", "lat", "long" FROM "meteorites_temp";

DROP TABLE "meteorites_temp";

DROP TABLE IF EXISTS "sorted_meteorites";