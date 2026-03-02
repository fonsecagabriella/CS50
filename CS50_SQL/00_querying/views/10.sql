-- My query: Select top 5 works with the highest entropy, with 'fuji' in the title,
--, showing the english_title, entropy and artist 
SELECT "english_title" AS 'title of the work',
         "entropy" AS 'entropy of the work',
         "artist" AS 'artist of the work'
FROM "views"
WHERE "english_title" LIKE '%fuji%'
ORDER BY "entropy" DESC
LIMIT 5;