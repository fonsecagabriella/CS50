-- write a SQL query to find the highest contrast value of prints by Hokusai. Name the column “Maximum Contrast”
SELECT MAX("contrast") AS 'Maximum Contrast'
FROM "views"
WHERE "artist"= 'Hokusai';