-- Question of choice using, AS, WHERE and ORDER BY
-- Calculate the average Weight and Height of players from
-- 2000s, per country, ordered alphabetically by country name. 
-- Return the columns with the name "Average Weight" and "Average Height", respectively.

SELECT ROUND(AVG("weight"),3) AS "Average Weight",
       ROUND(AVG("height"), 3) AS "Average Height",
       "birth_country" AS "Birth Country"
FROM "players"
WHERE "debut" >= '2000-01-01'
GROUP BY "birth_country"
ORDER BY "birth_country" ASC;