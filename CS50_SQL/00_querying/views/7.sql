-- write a SQL query to list the English titles of the 5 brightest prints by Hiroshige, from most to least bright
SELECT "english_title"
FROM "views"
WHERE "artist" = 'Hiroshige'
ORDER BY "brightness" DESC
LIMIT 5;