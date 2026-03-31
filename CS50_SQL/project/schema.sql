-- ============================================================
-- Cat Tracking Database — schema.sql
-- CS50 SQL Final Project
-- ============================================================


-- ============================================================
-- ENTITY: cats
-- Central table. Every other health/care record references this.
-- ============================================================
CREATE TABLE "cats" (
    "id"            INTEGER,
    "name"          TEXT    NOT NULL,
    "breed"         TEXT,                           -- NULL = unknown/mixed
    "sex"           TEXT    NOT NULL CHECK("sex" IN ('M', 'F')),
    "date_of_birth" DATE,                           -- NULL = unknown/estimated DOB
    "color"         TEXT,
    "microchip_id"  TEXT    UNIQUE,                 -- ISO 15-digit chip; UNIQUE enforced
    "neutered"      INTEGER NOT NULL DEFAULT 0
                            CHECK("neutered" IN (0, 1)),  -- 0 = no, 1 = yes
    "notes"         TEXT,
    "adopted_on"    DATE,
    "deceased_on"   DATE,                           -- NULL while alive
    PRIMARY KEY("id")
);


-- ============================================================
-- ENTITY: vets
-- Veterinary clinics and/or individual practitioners.
-- ============================================================
CREATE TABLE "vets" (
    "id"        INTEGER,
    "name"      TEXT    NOT NULL,
    "address"   TEXT,
    "phone"     TEXT,
    "email"     TEXT,
    "website"   TEXT,
    "notes"     TEXT,
    PRIMARY KEY("id")
);


-- ============================================================
-- ENTITY: vet_visits
-- One row per appointment per cat.
-- ============================================================
CREATE TABLE "vet_visits" (
    "id"            INTEGER,
    "cat_id"        INTEGER NOT NULL,
    "vet_id"        INTEGER NOT NULL,
    "visit_date"    DATE    NOT NULL DEFAULT (DATE('now')),
    "reason"        TEXT    NOT NULL,
    "diagnosis"     TEXT,
    "treatment"     TEXT,
    "follow_up_due" DATE,
    "cost"          FLOAT(10,2) CHECK("cost" >= 0) DEFAULT 0.00,
    "notes"         TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("cat_id") REFERENCES "cats"("id"),
    FOREIGN KEY("vet_id")  REFERENCES "vets"("id")
);


-- ============================================================
-- ENTITY: vaccinations
-- Each vaccine administered, with booster due date.
-- ============================================================
CREATE TABLE "vaccinations" (
    "id"                INTEGER,
    "cat_id"            INTEGER NOT NULL,
    "vet_visit_id"      INTEGER,                    -- NULL if not linked to a tracked visit
    "vaccine_name"      TEXT    NOT NULL,
    "administered_on"   DATE    NOT NULL,
    "next_due_on"       DATE,                       -- NULL if no booster required
    "batch_number"      TEXT,
    "notes"             TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("cat_id")       REFERENCES "cats"("id"),
    FOREIGN KEY("vet_visit_id") REFERENCES "vet_visits"("id")
);


-- ============================================================
-- ENTITY: weights
-- Periodic weight measurements for health trend monitoring.
-- ============================================================
CREATE TABLE "weights" (
    "id"            INTEGER,
    "cat_id"        INTEGER NOT NULL,
    "measured_on"   DATE    NOT NULL DEFAULT (DATE('now')),
    "weight_kg"     REAL    NOT NULL CHECK("weight_kg" > 0),
    "measured_by"   TEXT,                           -- e.g. "owner", "vet"
    "notes"         TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("cat_id") REFERENCES "cats"("id")
);


-- ============================================================
-- ENTITY: food
-- Catalogue of food products. Referenced by the feedings table.
-- ============================================================
CREATE TABLE "food" (
    "id"            INTEGER,
    "brand"         TEXT    NOT NULL,
    "product_name"  TEXT    NOT NULL,
    "type"          TEXT    NOT NULL
                    CHECK("type" IN ('dry', 'wet', 'raw', 'treat', 'supplement', 'other')),
    "flavour"       TEXT,
    "kcal_per_100g" REAL,
    "notes"         TEXT,
    PRIMARY KEY("id")
);


-- ============================================================
-- ENTITY: feedings
-- Log of what each cat ate, when, and how much.
-- ============================================================
CREATE TABLE "feedings" (
    "id"        INTEGER,
    "cat_id"    INTEGER NOT NULL,
    "food_id"   INTEGER NOT NULL,
    "fed_at"    DATETIME NOT NULL,
    "amount_g"  REAL    NOT NULL CHECK("amount_g" > 0),
    "fed_by"    TEXT,
    "notes"     TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("cat_id")  REFERENCES "cats"("id"),
    FOREIGN KEY("food_id") REFERENCES "food"("id")
);


-- ============================================================
-- ENTITY: medications
-- Catalogue of medications/treatments. Stores what a medication
-- IS, not how it is prescribed to a specific cat.
-- Dose amounts are expressed in the unit defined here.
-- ============================================================
CREATE TABLE "medications" (
    "id"    INTEGER,
    "name"  TEXT    NOT NULL,
    "type"  TEXT    NOT NULL
            CHECK("type" IN (
                'steroid', 'antibiotic', 'antiviral', 'antifungal',
                'antiparasitic', 'lubricant', 'supplement',
                'immunosuppressant', 'analgesic', 'other'
            )),
    "unit"  TEXT    NOT NULL,                       -- e.g. "mg", "ml", "drop", "tablet"
    "notes" TEXT,
    PRIMARY KEY("id")
);


-- ============================================================
-- ENTITY: cat_medication_plans
-- A prescribed course of a medication for a specific cat.
-- Captures the intended dose and frequency for a given period,
-- as decided by a vet or owner. Actual daily administration
-- is recorded in daily_medication_log.
-- ============================================================
CREATE TABLE "cat_medication_plans" (
    "id"            INTEGER,
    "cat_id"        INTEGER NOT NULL,
    "medication_id" INTEGER NOT NULL,
    "vet_visit_id"  INTEGER,                        -- NULL if not linked to a specific visit
    "dose"          REAL,                           -- intended dose in the medication's unit
    "frequency"     TEXT,                           -- e.g. "once daily", "every other day"
    "start_date"    DATE    NOT NULL,
    "end_date"      DATE,                           -- NULL = ongoing
    "reason"        TEXT,
    "notes"         TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("cat_id")        REFERENCES "cats"("id"),
    FOREIGN KEY("medication_id") REFERENCES "medications"("id"),
    FOREIGN KEY("vet_visit_id")  REFERENCES "vet_visits"("id")
);


-- ============================================================
-- ENTITY: daily_logs
-- One row per cat per day. Captures symptom scores and general
-- wellness observations. Medication administration for that day
-- is stored separately in daily_medication_log.
-- ============================================================
CREATE TABLE "daily_logs" (
    "id"                    INTEGER,
    "cat_id"                INTEGER NOT NULL,
    "log_date"              DATE    NOT NULL,
    "eye_status"            INTEGER CHECK("eye_status" BETWEEN 0 AND 5), -- 0 = normal, 5 = severe
    "discharge_type"        TEXT    CHECK("discharge_type" IN
                                ('Watery', 'Mucous', 'Gelatinous', 'None', NULL)),
    "squinting_notes"       TEXT,
    "lip_ulcer_severity"    INTEGER CHECK("lip_ulcer_severity" BETWEEN 0 AND 3), -- 0 = none, 3 = severe
    "vomiting"              INTEGER CHECK("vomiting" IN (0, 1)),  -- 0 = no, 1 = yes
    "vomiting_details"      TEXT,
    "appetite"              TEXT    CHECK("appetite" IN ('Normal', 'Reduced', 'Increased', NULL)),
    "energy_level"          TEXT    CHECK("energy_level" IN ('Normal', 'Reduced', 'Increased', NULL)),
    "potential_triggers"    TEXT,
    "general_notes"         TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("cat_id") REFERENCES "cats"("id"),
    UNIQUE("cat_id", "log_date")                    -- one log entry per cat per day
);


-- ============================================================
-- ENTITY: daily_medication_log
-- Records each individual administration of a medication on a
-- given day. Linked to daily_logs for context. The timestamp
-- captures when it was given (AM/PM deducible from time).
-- dose_given is expressed in the unit of the linked medication.
-- ============================================================
CREATE TABLE "daily_medication_log" (
    "id"            INTEGER,
    "daily_log_id"  INTEGER NOT NULL,
    "medication_id" INTEGER NOT NULL,
    "given_at"      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- full timestamp; AM/PM deducible
    "dose_given"    REAL    NOT NULL CHECK("dose_given" > 0),
    "notes"         TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("daily_log_id")  REFERENCES "daily_logs"("id"),
    FOREIGN KEY("medication_id") REFERENCES "medications"("id")
);


-- ============================================================
-- ENTITY: condition_periods
-- Narrative summaries of a cat's health status over a defined
-- period. Mirrors the "Period Summary" sheet in Milo's log.
-- Useful for communicating with vets and tracking phases.
-- ============================================================
CREATE TABLE "condition_periods" (
    "id"                INTEGER,
    "cat_id"            INTEGER NOT NULL,
    "label"             TEXT,                       -- human-readable period name
    "start_date"        DATE,
    "end_date"          DATE,                       -- NULL = ongoing
    "health_summary"    TEXT,                       -- combined eye + systemic observations
    "treatment_summary" TEXT,                       -- what was being given during this period
    "notes"             TEXT,
    PRIMARY KEY("id"),
    FOREIGN KEY("cat_id") REFERENCES "cats"("id")
);


-- ============================================================
-- INDEXES
-- ============================================================

-- cat_id FKs — most queries filter by cat
CREATE INDEX "idx_vet_visits_cat_id"          ON "vet_visits"("cat_id");
CREATE INDEX "idx_vaccinations_cat_id"        ON "vaccinations"("cat_id");
CREATE INDEX "idx_weights_cat_id"             ON "weights"("cat_id");
CREATE INDEX "idx_feedings_cat_id"            ON "feedings"("cat_id");
CREATE INDEX "idx_cat_medication_plans_cat"   ON "cat_medication_plans"("cat_id");
CREATE INDEX "idx_daily_logs_cat_id"          ON "daily_logs"("cat_id");
CREATE INDEX "idx_condition_periods_cat_id"   ON "condition_periods"("cat_id");

-- Date-range queries are very common
CREATE INDEX "idx_vet_visits_date"            ON "vet_visits"("visit_date");
CREATE INDEX "idx_daily_logs_date"            ON "daily_logs"("log_date");
CREATE INDEX "idx_daily_medication_log_time"  ON "daily_medication_log"("given_at");
CREATE INDEX "idx_weights_date"               ON "weights"("measured_on");

-- Booster reminders
CREATE INDEX "idx_vaccinations_next_due"      ON "vaccinations"("next_due_on");

-- Active medication plans
CREATE INDEX "idx_plans_end_date"             ON "cat_medication_plans"("end_date");

-- Medication lookup by name/type
CREATE INDEX "idx_medications_name"           ON "medications"("name");
CREATE INDEX "idx_medications_type"           ON "medications"("type");


-- ============================================================
-- VIEWS
-- ============================================================

-- Upcoming vaccinations due within the next 60 days
CREATE VIEW "upcoming_vaccinations" AS
    SELECT
        c."name"        AS cat_name,
        v."vaccine_name",
        v."next_due_on",
        CAST(julianday(v."next_due_on") - julianday('now') AS INTEGER) AS days_until_due
    FROM "vaccinations" v
    JOIN "cats" c ON c."id" = v."cat_id"
    WHERE v."next_due_on" IS NOT NULL
      AND v."next_due_on" >= DATE('now')
      AND v."next_due_on" <= DATE('now', '+60 days')
    ORDER BY v."next_due_on";


-- Currently active medication plans (end_date NULL or in the future)
CREATE VIEW "active_medication_plans" AS
    SELECT
        c."name"            AS cat_name,
        m."name"            AS medication,
        m."type"            AS medication_type,
        m."unit",
        p."dose",
        p."frequency",
        p."start_date",
        p."end_date",
        p."reason"
    FROM "cat_medication_plans" p
    JOIN "cats"        c ON c."id" = p."cat_id"
    JOIN "medications" m ON m."id" = p."medication_id"
    WHERE p."end_date" IS NULL
       OR p."end_date" >= DATE('now')
    ORDER BY c."name", p."start_date";


-- Latest recorded weight per cat
CREATE VIEW "latest_weights" AS
    SELECT
        c."name"        AS cat_name,
        w."weight_kg",
        w."measured_on"
    FROM "weights" w
    JOIN "cats" c ON c."id" = w."cat_id"
    WHERE w."measured_on" = (
        SELECT MAX(w2."measured_on")
        FROM "weights" w2
        WHERE w2."cat_id" = w."cat_id"
    )
    ORDER BY c."name";


-- 7-day rolling eye status average per cat (requires daily_logs data)
CREATE VIEW "eye_status_7day_avg" AS
    SELECT
        c."name"    AS cat_name,
        ROUND(AVG(dl."eye_status"), 2) AS avg_eye_status,
        MIN(dl."log_date")  AS period_start,
        MAX(dl."log_date")  AS period_end
    FROM "daily_logs" dl
    JOIN "cats" c ON c."id" = dl."cat_id"
    WHERE dl."log_date" >= DATE('now', '-7 days')
      AND dl."eye_status" IS NOT NULL
    GROUP BY dl."cat_id"
    ORDER BY c."name";


-- Daily medication summary: what each cat received on each day
CREATE VIEW "daily_medication_summary" AS
    SELECT
        c."name"            AS cat_name,
        dl."log_date",
        m."name"            AS medication,
        m."unit",
        SUM(dml."dose_given")           AS total_dose_given,
        COUNT(dml."id")                 AS administrations,
        GROUP_CONCAT(
            TIME(dml."given_at"), ' / '
        )                               AS times_given
    FROM "daily_medication_log" dml
    JOIN "daily_logs"   dl ON dl."id"  = dml."daily_log_id"
    JOIN "cats"         c  ON c."id"   = dl."cat_id"
    JOIN "medications"  m  ON m."id"   = dml."medication_id"
    GROUP BY dl."cat_id", dl."log_date", dml."medication_id"
    ORDER BY c."name", dl."log_date", m."name";


-- Most recent condition period per cat
CREATE VIEW "current_condition" AS
    SELECT
        c."name"            AS cat_name,
        cp."label",
        cp."start_date",
        cp."end_date",
        cp."health_summary",
        cp."treatment_summary",
        cp."notes"
    FROM "condition_periods" cp
    JOIN "cats" c ON c."id" = cp."cat_id"
    WHERE cp."start_date" = (
        SELECT MAX(cp2."start_date")
        FROM "condition_periods" cp2
        WHERE cp2."cat_id" = cp."cat_id"
    )
    ORDER BY c."name";


-- Flare-up days: days where eye_status >= 3
CREATE VIEW "flare_up_days" AS
    SELECT
        c."name"            AS cat_name,
        dl."log_date",
        dl."eye_status",
        dl."discharge_type",
        dl."squinting_notes",
        dl."general_notes"
    FROM "daily_logs" dl
    JOIN "cats" c ON c."id" = dl."cat_id"
    WHERE dl."eye_status" >= 3
    ORDER BY c."name", dl."log_date";