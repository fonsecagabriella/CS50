-- Users table
CREATE TABLE IF NOT EXISTS "users"(
    "id" INTEGER,
    "first_name" VARCHAR(50) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "username" VARCHAR(16) UNIQUE NOT NULL,
    "password" HASH(255) NOT NULL,

    PRIMARY KEY ("id")
);

-- Schools and Universities table
CREATE TABLE IF NOT EXISTS "schools" (
    "id" INTEGER,
    "name" VARCHAR(255) NOT NULL,
    "type" VARCHAR(255) NOT NULL,
    "location" VARCHAR(255) NOT NULL,
    "year_founded" INTEGER(4) NOT NULL,

    PRIMARY KEY ("id"),
    CONSTRAINT "chk_type" CHECK ("type" IN
                                ('Elementary School', 'Middle School', 'High School',
                                'Lower School', 'Upper School', 'College', 'University')),

    CONSTRAINT "chk_year_founded" CHECK ("year_founded" >= 1000 AND "year_founded" <= 9999)

);

-- Companies table
CREATE TABLE IF NOT EXISTS "companies" (
    "id" INTEGER,
    "name" VARCHAR(255) NOT NULL,
    "industry" VARCHAR(255) NOT NULL,
    "location" VARCHAR(255) NOT NULL,

    PRIMARY KEY ("id")
);

-- People connections table
CREATE TABLE IF NOT EXISTS "user_connections" (
    "id" INTEGER,
    "user_id" INTEGER NOT NULL,
    "connection_id" INTEGER NOT NULL,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("connection_id") REFERENCES "users"("id")
);

-- School connections table
CREATE TABLE IF NOT EXISTS "school_connections" (
    "id" INTEGER,
    "user_id" INTEGER NOT NULL,
    "school_id" INTEGER NOT NULL,
    "start_date_affiliation" DATE NOT NULL,
    "end_date_affiliation" DATE,
    "type_affiliation" VARCHAR(10) NOT NULL,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("school_id") REFERENCES "schools"("id")
);

-- Company connections table
CREATE TABLE IF NOT EXISTS "company_connections" (
    "id" INTEGER,
    "user_id" INTEGER NOT NULL,
    "company_id" INTEGER NOT NULL,
    "start_date_affiliation" DATE NOT NULL,
    "end_date_affiliation" DATE,
    "title" VARCHAR(10) NOT NULL,

    PRIMARY KEY ("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("company_id") REFERENCES "companies"("id")
);