# Intro to SQL | Week 00 - Querying

- SQL: Structured Query Language

## Commands used in the lesson

- `ls`: list files on current folder
- `sqlite3 db.db` : open db in the terminal
- `CTRL + L`: clear the terminal
- `.quit`: quits the terminal
- `cat log.sql | sqlite3 packages.db > output.txt`: export output of sql queries

## SQL Commands

-  `SELECT` ... `FROM`... `LIMIT`
- `IS NULL`
- `WHERE column LIKE '%term%' `: doesn't consider case sensitive
- `WHERE column = 'term'`: here case matters
- `LIKE 'abc__'` : each _ represents a character
- `BETWEEN date_01 AND date_01`
- `ORDER BY`
- `SELECT AVG("rating") from db`
- `SELECT ROUND (AVG("rating"), 2) AS "average rating"`
- `SELECT COUNT(*) FROM "db"`
- `SELECT DISTINCT "column" from db`
- `SELECT COUNT(DISTINCT "column") FROM db`

