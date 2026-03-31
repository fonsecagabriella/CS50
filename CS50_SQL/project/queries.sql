-- ============================================================
-- Cat Tracking Database — queries.sql
-- Illustrative queries using a fictitious cat called Mimzi.
-- Covers all tables with sample INSERTs and common
-- SELECT / UPDATE / DELETE patterns.
-- ============================================================


-- ============================================================
-- INSERT — Cats
-- ============================================================

-- Add Mimzi, a 3-year-old female stray adopted in April 2018
INSERT INTO "cats" (
    "name", "breed", "sex", "date_of_birth", "color",
    "microchip_id", "neutered", "adopted_on", "notes"
) VALUES (
    'Mimzi', 'Mixed', 'F', '2022-04-10', 'Light gray',
    '528140000999001', 1, '2022-06-15',
    'Very vocal; dislikes strangers but affectionate with family'
);


-- ============================================================
-- INSERT — Vets
-- ============================================================

INSERT INTO "vets" ("name", "address", "phone", "email")
VALUES ('De Poezenkliniek', 'Keizersgracht 45, Amsterdam', '+31 20 555 0101', 'info@poezenkliniek.nl');


-- ============================================================
-- INSERT — Vet visits
-- ============================================================

-- Annual checkup for Mimzi
INSERT INTO "vet_visits" (
    "cat_id", "vet_id", "visit_date", "reason",
    "diagnosis", "treatment", "follow_up_due", "cost"
) VALUES (
    1, 1, '2024-06-10', 'Annual checkup',
    'Healthy; mild dental tartar noted', 'Dental hygiene advice; vaccination updated',
    '2025-06-10', 75.00
);


-- ============================================================
-- INSERT — Vaccinations
-- ============================================================

INSERT INTO "vaccinations" (
    "cat_id", "vet_visit_id", "vaccine_name", "administered_on", "next_due_on"
) VALUES (1, 1, 'FVRCP', '2024-06-10', '2025-06-10');

INSERT INTO "vaccinations" (
    "cat_id", "vet_visit_id", "vaccine_name", "administered_on", "next_due_on"
) VALUES (1, 1, 'Rabies', '2024-06-10', '2027-06-10');


-- ============================================================
-- INSERT — Weights
-- ============================================================

INSERT INTO "weights" ("cat_id", "measured_on", "weight_kg", "measured_by")
VALUES (1, '2024-06-10', 5.1, 'vet');

INSERT INTO "weights" ("cat_id", "measured_on", "weight_kg", "measured_by")
VALUES (1, '2025-01-15', 5.3, 'owner');


-- ============================================================
-- INSERT — Food catalogue
-- ============================================================

INSERT INTO "food" ("brand", "product_name", "type", "flavour", "kcal_per_100g")
VALUES ('Royal Canin', 'Indoor Adult', 'dry', 'Chicken', 341);

INSERT INTO "food" ("brand", "product_name", "type", "flavour", "kcal_per_100g")
VALUES ('Sheba', 'Perfect Portions', 'wet', 'Salmon', 72);


-- ============================================================
-- INSERT — Feedings
-- ============================================================

INSERT INTO "feedings" ("cat_id", "food_id", "fed_at", "amount_g", "fed_by")
VALUES (1, 1, '2025-03-28 08:00:00', 40, 'owner');

INSERT INTO "feedings" ("cat_id", "food_id", "fed_at", "amount_g", "fed_by")
VALUES (1, 2, '2025-03-28 18:30:00', 85, 'owner');


-- ============================================================
-- INSERT — Medications catalogue
-- ============================================================

-- Steroid tablet
INSERT INTO "medications" ("name", "type", "unit", "notes")
VALUES ('Prednisolone', 'steroid', 'mg', '5mg tablets; often halved for maintenance');

-- Lubricant eye drop
INSERT INTO "medications" ("name", "type", "unit", "notes")
VALUES ('Hylogel', 'lubricant', 'drop', 'Viscous eye gel for comfort');

-- Supplement chew
INSERT INTO "medications" ("name", "type", "unit", "notes")
VALUES ('L-lysine', 'supplement', 'mg', '250mg chews; supports immune response in FHV-1');


-- ============================================================
-- INSERT — Cat medication plans
-- ============================================================

-- Mimzi on a short course of Prednisolone after a flare
INSERT INTO "cat_medication_plans" (
    "cat_id", "medication_id", "vet_visit_id",
    "dose", "frequency", "start_date", "end_date", "reason"
) VALUES (
    1, 1, 1,
    5.0, 'once daily (PM)', '2024-06-10', '2024-06-24',
    'Mild allergic conjunctivitis'
);

-- Ongoing L-lysine supplementation
INSERT INTO "cat_medication_plans" (
    "cat_id", "medication_id",
    "dose", "frequency", "start_date", "reason"
) VALUES (
    1, 3,
    500, 'once daily', '2024-06-10',
    'Long-term immune support'
);


-- ============================================================
-- INSERT — Daily logs
-- ============================================================

INSERT INTO "daily_logs" (
    "cat_id", "log_date", "eye_status", "discharge_type",
    "squinting_notes", "lip_ulcer_severity", "vomiting",
    "appetite", "energy_level", "general_notes"
) VALUES (
    1, '2024-06-15', 2, 'Watery',
    'Mild squinting on left eye', 0, 0,
    'Normal', 'Normal', 'First day home after vet visit; calm'
);

INSERT INTO "daily_logs" (
    "cat_id", "log_date", "eye_status", "discharge_type",
    "squinting_notes", "lip_ulcer_severity", "vomiting",
    "appetite", "energy_level", "general_notes"
) VALUES (
    1, '2024-06-16', 1, 'Watery',
    'Minimal squinting', 0, 0,
    'Normal', 'Normal', 'Improving; more active today'
);


-- ============================================================
-- INSERT — Daily medication log
-- ============================================================

-- Prednisolone given in the evening on 2024-06-15
INSERT INTO "daily_medication_log" (
    "daily_log_id", "medication_id", "given_at", "dose_given"
) VALUES (1, 1, '2024-06-15 20:00:00', 5.0);

-- L-lysine given in the morning on 2024-06-15
INSERT INTO "daily_medication_log" (
    "daily_log_id", "medication_id", "given_at", "dose_given"
) VALUES (1, 3, '2024-06-15 08:00:00', 500);

-- Prednisolone given in the evening on 2024-06-16
INSERT INTO "daily_medication_log" (
    "daily_log_id", "medication_id", "given_at", "dose_given"
) VALUES (2, 1, '2024-06-16 20:00:00', 5.0);


-- ============================================================
-- INSERT — Condition periods
-- ============================================================

INSERT INTO "condition_periods" (
    "cat_id", "label", "start_date", "end_date",
    "health_summary", "treatment_summary", "notes"
) VALUES (
    1, 'Jun 2024 – ongoing', '2024-06-10', NULL,
    'Mild allergic conjunctivitis resolved within two weeks of treatment. Eyes stable since; minimal watery discharge in mornings.',
    'Short course of Prednisolone 5mg daily (2 weeks); ongoing L-lysine 500mg daily.',
    'Monitor for recurrence; recheck if eye_status reaches 3 or above'
);


-- ============================================================
-- SELECT — Common read queries
-- ============================================================

-- All living cats with their age in years
SELECT
    "name", "breed", "sex", "color",
    CAST((julianday('now') - julianday("date_of_birth")) / 365.25 AS INTEGER) AS age_years
FROM "cats"
WHERE "deceased_on" IS NULL
ORDER BY "name";


-- Full health profile for Mimzi
SELECT
    c."name", c."breed", c."sex", c."date_of_birth", c."color",
    c."microchip_id",
    CASE c."neutered" WHEN 1 THEN 'Yes' ELSE 'No' END AS neutered,
    c."adopted_on", c."notes"
FROM "cats" c
WHERE c."name" = 'Mimzi';


-- All vet visits for Mimzi, newest first
SELECT
    vv."visit_date",
    vt."name"       AS vet,
    vv."reason",
    vv."diagnosis",
    vv."treatment",
    vv."cost"
FROM "vet_visits" vv
JOIN "vets" vt ON vt."id" = vv."vet_id"
JOIN "cats" c  ON c."id"  = vv."cat_id"
WHERE c."name" = 'Mimzi'
ORDER BY vv."visit_date" DESC;


-- Vaccination status for Mimzi
SELECT
    v."vaccine_name",
    v."administered_on",
    v."next_due_on",
    CASE
        WHEN v."next_due_on" IS NULL               THEN 'No booster needed'
        WHEN v."next_due_on" < DATE('now')         THEN 'OVERDUE'
        WHEN v."next_due_on" <= DATE('now','+60 days') THEN 'Due soon'
        ELSE 'Up to date'
    END AS status
FROM "vaccinations" v
JOIN "cats" c ON c."id" = v."cat_id"
WHERE c."name" = 'Mimzi'
ORDER BY v."administered_on" DESC;


-- Daily log history for Mimzi over the last 30 days
SELECT
    dl."log_date",
    dl."eye_status",
    dl."discharge_type",
    dl."lip_ulcer_severity",
    CASE dl."vomiting" WHEN 1 THEN 'Yes' ELSE 'No' END AS vomiting,
    dl."appetite",
    dl."energy_level",
    dl."general_notes"
FROM "daily_logs" dl
JOIN "cats" c ON c."id" = dl."cat_id"
WHERE c."name" = 'Mimzi'
  AND dl."log_date" >= DATE('now', '-30 days')
ORDER BY dl."log_date" DESC;


-- What medications did Mimzi receive on a specific date?
SELECT
    m."name"            AS medication,
    m."unit",
    dml."dose_given",
    TIME(dml."given_at") AS time_given
FROM "daily_medication_log" dml
JOIN "daily_logs"  dl ON dl."id"  = dml."daily_log_id"
JOIN "medications" m  ON m."id"   = dml."medication_id"
JOIN "cats"        c  ON c."id"   = dl."cat_id"
WHERE c."name" = 'Mimzi'
  AND dl."log_date" = '2024-06-15'
ORDER BY dml."given_at";


-- Use the views
SELECT * FROM "upcoming_vaccinations";
SELECT * FROM "active_medication_plans";
SELECT * FROM "latest_weights";
SELECT * FROM "eye_status_7day_avg";
SELECT * FROM "daily_medication_summary" WHERE "cat_name" = 'Mimzi';
SELECT * FROM "current_condition";
SELECT * FROM "flare_up_days";


-- Eye status trend for Mimzi over time
SELECT
    dl."log_date",
    dl."eye_status",
    dl."discharge_type"
FROM "daily_logs" dl
JOIN "cats" c ON c."id" = dl."cat_id"
WHERE c."name" = 'Mimzi'
ORDER BY dl."log_date";


-- ============================================================
-- UPDATE — Common modifications
-- ============================================================

-- Update microchip ID
UPDATE "cats"
SET "microchip_id" = '528140000999002'
WHERE "name" = 'Mimzi';

-- Mark a medication plan as ended
UPDATE "cat_medication_plans"
SET "end_date" = '2024-06-24'
WHERE "cat_id" = (SELECT "id" FROM "cats" WHERE "name" = 'Mimzi')
  AND "medication_id" = (SELECT "id" FROM "medications" WHERE "name" = 'Prednisolone')
  AND "end_date" IS NULL;

-- Correct an eye status entry that was logged incorrectly
UPDATE "daily_logs"
SET "eye_status" = 1
WHERE "cat_id" = (SELECT "id" FROM "cats" WHERE "name" = 'Mimzi')
  AND "log_date" = '2024-06-16';


-- ============================================================
-- DELETE — Removing data
-- ============================================================

-- Remove an incorrectly logged feeding entry
DELETE FROM "feedings"
WHERE "id" = 2;

-- Remove a food product only if it has never been used in a feeding
DELETE FROM "food"
WHERE "id" = 2
  AND "id" NOT IN (SELECT DISTINCT "food_id" FROM "feedings");