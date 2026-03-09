-- Passengers table
CREATE TABLE IF NOT EXISTS "passengers" (
    "id" INTEGER,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "age" INTEGER NOT NULL,

    PRIMARY KEY ("id")
);

-- Airlines table
CREATE TABLE IF NOT EXISTS "airlines" (
    "id" INTEGER,
    "name" VARCHAR(255) NOT NULL,
    "concourse" VARCHAR(2) NOT NULL,

    PRIMARY KEY ("id"),
    CONSTRAINT "chk_concourse" CHECK ("concourse" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T'))
);

-- Flights table
CREATE TABLE IF NOT EXISTS "flights" (
    "id" INTEGER,
    "number" INTEGER NOT NULL,
    "airline_id" INTEGER NOT NULL,
    "code_airport_departure" VARCHAR(255) NOT NULL,
    "code_airport_arrival" VARCHAR(255) NOT NULL,
    "datetime_departure_expected" DATETIME NOT NULL,
    "datetime_departure_actual" DATETIME,
    "datetime_arrival_expected" DATETIME NOT NULL,
    "datetime_arrival_actual" DATETIME,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("airline_id") REFERENCES "airlines"("id")
);

-- Check-ins table
CREATE TABLE IF NOT EXISTS "check_ins" (
    "id" INTEGER,
    "passenger_id" INTEGER NOT NULL,
    "flight_id" INTEGER NOT NULL,
    "datetime_checked_in" DATETIME NOT NULL,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY ("flight_id") REFERENCES "flights"("id")
);