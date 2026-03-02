-- write a SQL query to count how many prints by Hokusai include “Fuji” in the English title.
SELECT COUNT(*) AS contain_fuji
FROM "views"
WHERE "english_title" LIKE '%Fuji%' AND "artist" = 'Hokusai';