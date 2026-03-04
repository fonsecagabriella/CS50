-- Find districts with below average staff with needs_improvement or unsatisfactory ratings
-- but with higher than average pupil expenditure
-- print district name,  rate of staff with needs_improvement or unsatisfactory ratings, 
-- and pupil expenditure
SELECT
    "districts"."name",
    "staff_evaluations"."needs_improvement",
    "staff_evaluations"."unsatisfactory",
    "expenditures"."per_pupil_expenditure"
FROM
    "districts"
JOIN
    "staff_evaluations"
    ON
    "districts"."id" = "staff_evaluations"."district_id"
JOIN
    "expenditures"
    ON
    "districts"."id" = "expenditures"."district_id"
WHERE
    ("staff_evaluations"."needs_improvement" + "staff_evaluations"."unsatisfactory") < (
        SELECT
            AVG("staff_evaluations"."needs_improvement" + "staff_evaluations"."unsatisfactory")
        FROM
            "staff_evaluations"
    )
    AND "expenditures"."per_pupil_expenditure" > (
        SELECT
            AVG("expenditures"."per_pupil_expenditure")
        FROM
            "expenditures"
    )
ORDER BY
    "staff_evaluations"."needs_improvement" + "staff_evaluations"."unsatisfactory" DESC,
    "expenditures"."per_pupil_expenditure" DESC;